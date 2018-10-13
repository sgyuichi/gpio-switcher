$(function() {
    $('.switch').bind('click', function() {
      $.ajax({
        url: $SCRIPT_ROOT + '/switch',
        method: 'POST'
      }, function(data) {
      });
      return false;
    });
});
