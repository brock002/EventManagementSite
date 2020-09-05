$("#copybtn").tooltip('disable');
var clipboard = new ClipboardJS('#copybtn', {
    container: document.getElementById('shareButtonModal')
});
clipboard.on('success', function() {
    $("#copybtn").tooltip('enable');
    $("#copybtn").tooltip('show');
    $("#copybtn").tooltip('disable');
});