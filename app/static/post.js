
function submitForm() {
    newBody = $("#postEditor").html()
    $("input[name=body]").val(newBody)
    $("#postForm").submit()
}