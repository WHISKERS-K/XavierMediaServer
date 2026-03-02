def can_modify(user):
    return user.is_authenticated and user.profile.priv >= 1

def can_view(user):
    return user.is_authenticated and user.profile.priv >= 0

