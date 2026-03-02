import os
import re
import mimetypes

from django.http import StreamingHttpResponse, HttpRequest
from django.views.decorators.cache import never_cache
from media.models import Movies

#Chunked generator to keep RAM usage near zero
def chunk_generator(path, start, end, chunk_size=16384): # 16KB chunks
    with open(path, 'rb') as f:
        f.seek(start)
        remaining = end - start + 1
        while remaining > 0:
            data = f.read(min(chunk_size, remaining))
            if not data:
                break
            yield data
            remaining -= len(data)

@never_cache
def stream_movie(request: HttpRequest, movie_id):
    # Fetch from the specific app model
    movie_db = Movies.objects.get(id=movie_id)
    movie_path = movie_db.movie_file.path
    
    # Auto-detect content type (e.g., video/mp4, video/x-matroska)
    content_type, _ = mimetypes.guess_type(movie_path)
    content_type = content_type or 'application/octet-stream'
    
    file_size = os.path.getsize(movie_path)

    '''
    Range header looks like this: 
        Example (First 500KB): Range: bytes=0-512000
        Example (From 2GB to the end): Range: bytes=2147483648-
        Example (A specific 1MB chunk): Range: bytes=1000000-2000000

        status 200 means: FULL FILE OK
        status 206 means: PARTIAL FILE CONTENT
    '''


    # Handle Range header for seeking/forwarding
    range_header = request.headers.get('Range', '').strip()
    range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)

    if range_match:
        start_byte, end_byte = range_match.groups()
        start_byte = int(start_byte)
        ##so if the range request doesnt have end_byte we just return file size minus one
        end_byte = int(end_byte) if end_byte else file_size - 1
        status_code = 206
    else:
        #this is for when we first open the movie file
        start_byte = 0
        end_byte = file_size - 1
        status_code = 200

    content_length = end_byte - start_byte + 1

    response = StreamingHttpResponse(
        chunk_generator(movie_path, start_byte, end_byte),
        status=status_code,
        content_type=content_type
    )

    ##TELLS THE BROWSER I SUPPORT SEEKING
    response['Accept-Ranges'] = 'bytes'

    response['Content-Range'] = f'bytes {start_byte}-{end_byte}/{file_size}'
    response['Content-Length'] = str(content_length)
    
    ##This should fix videos getting stuck in cache
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate, proxy-revalidate'
    response['Pragma'] = 'no-cache'  # For older browsers
    response['Expires'] = '0'        # Marks the content as immediately expired

    return response