
function updatePostData(newId, newBody, newTitle, newAuthor, newDateWritten, newUsername, newTimestamp,
                        next_id, prev_id) {
    $("#post").add("#postInfo").fadeOut(1000, function() {
        setTimeout(function() {
            $("#readingCanvas").scrollTop(0);
    }, 100);
        $("#post").html(newBody);
        $(".postTitle").text(newTitle);
        $(".postAuthor").text(newAuthor);
        $(".postDateWritten").text(newDateWritten);
        $(".createdBy").text("posted by " + newUsername + " on " + newTimestamp);
        $("#post").add("#postInfo").fadeIn(1000);
        if(next_id) {
            $("#nextArrow").removeClass("disabled").attr("href", "javascript:nextPost()");
        } else {
            $("#nextArrow").addClass("disabled").removeAttr("href");
        }
        if(prev_id) {
            $("#prevArrow").removeClass("disabled").attr("href", "javascript:prevPost()");
        } else {
            $("#prevArrow").addClass("disabled").removeAttr("href");
        }
        window.history.replaceState('post' + postId,'','/post/' + postId);
    });
    postId = newId;
}

function prevPost() {
    $.get('/post/' + postId + '/prev').done(function(response) {
        updatePostData(response.post.id, response.post.body, response.post.title, response.author.display_name,
            response.post.date_written, response.poster.username, response.post.timestamp,
            response.next_id, response.prev_id);
    }).fail(function() {
    })
}

function nextPost() {
    $.get('/post/' + postId + '/next').done(function(response) {
        updatePostData(response.post.id, response.post.body, response.post.title, response.author.display_name,
            response.post.date_written, response.poster.username, response.post.timestamp,
            response.next_id, response.prev_id);
    }).fail(function() {
    })
}
