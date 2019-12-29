var textColor = '#dddddd';
var highlightColor = '#8822ff';

$(function() {
  $("span").hover(function() {
      $('#'.concat(this.id.substring(0, 3)).concat('a')).css('color', highlightColor);
      $('#'.concat(this.id.substring(0, 3)).concat('b')).css('color', highlightColor);
    },
    function() {
      $('#'.concat(this.id.substring(0, 3)).concat('a')).css('color', textColor);
      $('#'.concat(this.id.substring(0, 3)).concat('b')).css('color', textColor);
    });
});
