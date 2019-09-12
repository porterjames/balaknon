
$(function() {
    $.ajax({
        url: '/country/autocomplete'
    }).done(function(data) {
        $('#nasod').autocomplete({
            source: data.country_names,
            minlength: 1
        });
    });

    $("#photo").change(function() {
        if (this.files && this.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                $("#authorPhoto").attr('src', e.target.result);
            }

            reader.readAsDataURL(this.files[0]);
        }
    });
});