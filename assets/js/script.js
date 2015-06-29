$(document).ready(function(){
    
    $('.photo1').hover(function() {
        $(this).hide();
        $(this).parent().find('.photo2').show();
    });
    
    $('.photo2').hover(function() {
    }, function() {
        $(this).hide();
        $(this).parent().find('.photo1').show();
    });

    var navbarTop = $('#navbar').offset().top
    $(document).scroll(function() {
        var windowTop = $(window).scrollTop();
        var diff = navbarTop - windowTop;
        var isTop = $('#navbar').hasClass('navbar-top');
        if (diff < 0 && !isTop) {
            $('#navbar').removeClass('navbar-middle').addClass('navbar-top');
        } else if (diff >= 0 && isTop) {
            $('#navbar').removeClass('navbar-top').addClass('navbar-middle');
        }
    });

});
