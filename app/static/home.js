
function updatePostData(newId, newBody, newTitle, newAuthor, newDateWritten, newUsername, newTimestamp) {
    $("#post").add("#postInfo").fadeOut(1000, function() {
        setTimeout(function() {
            $("#readingCanvas").scrollTop(0);
    }, 100);
        $("#post").text(newBody);
        $(".postTitle").text(newTitle);
        $(".postAuthor").text(newAuthor);
        $(".postDateWritten").text(newDateWritten);
        $(".createdBy").text("posted by " + newUsername + " on " + newTimestamp);
        $("#post").add("#postInfo").fadeIn(1000);
    });
    postId = newId;
}

function prevPost() {
    $.get('/post/prev/' + postId).done(function(response) {
        updatePostData(response.post.id, response.post.body, response.post.title, response.author.display_name,
            response.post.date_written, response.poster.username, response.post.timestamp);
    }).fail(function() {
    })
}

function nextPost() {
    $.get('/post/next/' + postId).done(function(response) {
        updatePostData(response.post.id, response.post.body, response.post.title, response.author.display_name,
            response.post.date_written, response.poster.username, response.post.timestamp);
    }).fail(function() {
    })
}
