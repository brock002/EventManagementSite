$("#copybtn").tooltip('disable');
var clipboard = new ClipboardJS('#copybtn', {
    container: document.getElementById('shareButtonModal')
});
clipboard.on('success', function() {
    $("#copybtn").tooltip('enable');
    $("#copybtn").tooltip('show');
    $("#copybtn").tooltip('disable');
});

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
    $('.alwaysOnTooltips').tooltip()
})