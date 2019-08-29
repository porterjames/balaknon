
$(function() {

    const container = document.querySelector("#readingCanvas");
    const ps = new PerfectScrollbar(container);

    $(".toggleFullscreen").click(function() {
        if ($.fullscreen.isFullScreen()) {
            $.fullscreen.exit();
            $(this).text("fullscreen");
        } else {
            $("html").fullscreen();
            $(this).text("exit");
        }
    })
})
