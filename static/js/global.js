  $(document).ready(function() {
    $('.carousel').carousel();

    $('#list-group-sidebar .list-group-item').click(function(e) {
      $("#list-group-sidebar .list-group-item").removeClass('active');
      $(e.target).addClass('active');
    });

});
