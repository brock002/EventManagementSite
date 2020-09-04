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

function nav_icons_style() {
    nav_icons = document.querySelectorAll(".nav-icon");
    for (let i = 0; i < nav_icons.length; i++) {
        nav_icons[i].addEventListener('mouseover', function () {
            nav_icons[i].lastElementChild.style.display = "inline";
        });
        nav_icons[i].addEventListener('mouseout', function () {
            nav_icons[i].lastElementChild.style.display = "none";
        });
    }
}

nav_icons_style();