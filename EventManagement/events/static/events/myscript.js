function scrollDivRight(id) {
    var RtBtn = document.getElementById(id);
    RtBtn.parentElement.parentElement.firstElementChild.scrollBy({
        left: 700,
        behavior: 'smooth'
    });
}

function scrollDivLeft(id) {
    var LtBtn = document.getElementById(id);
    LtBtn.parentElement.parentElement.firstElementChild.scrollBy({
        left: -700,
        behavior: 'smooth'
    });
}

$(function() {
    $('[data-toggle="tooltip"]').tooltip()
})
