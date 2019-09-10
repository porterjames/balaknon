
$(function() {
    $.ajax({
        url: '/author/autocomplete'
    }).done(function(data) {
        $('#author_display_name').autocomplete({
            source: data.author_names,
            minlength: 1
        });
    });
});

function submitForm() {
    let newBody = $("#postEditor").html();
    $("input[name=body]").val(newBody);
    $("#postForm").submit();
}