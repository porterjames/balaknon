
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

function prevPost() {
    $.get('/post/prev/' + postId).done(function(response) {
        let post_elem = "#post" + postId;
        $(post_elem).text(response.post.body);
        postId = response.post.id;
        $(post_elem).prop("id", "post" + postId);
        $(".postTitle").text(response.post.title);
        $(".postAuthor").text(response.author.display_name);
        $(".postDateWritten").text(response.post.date_written);
        $(".createdBy").text("posted by " + response.poster.username + " at " + response.post.timestamp);
    }).fail(function() {

    })
}

function nextPost() {
    $.get('/post/next/' + postId).done(function(response) {
        let post_elem = "#post" + postId;
        $(post_elem).text(response.post.body);
        postId = response.post.id;
        $(post_elem).prop("id", "post" + postId);
        $(".postTitle").text(response.post.title);
        $(".postAuthor").text(response.author.display_name);
        $(".postDateWritten").text(response.post.date_written);
        $(".createdBy").text("posted by " + response.poster.username + " at " + response.post.timestamp);
    }).fail(function() {

    })
}