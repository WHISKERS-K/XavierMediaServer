function do_x(a, b, fun) {
    let v = fun(a, b);
    return v;
}

function main() {
    let result = do_x(1, 2, function (c, d) {
        return c + d;
    });

    console.log(result);
}

document.addEventListener('DOMContentLoaded', main);