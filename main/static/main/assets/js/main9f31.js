(function ($) {
    "use strict";

    // One Page Nav
    var top_offset = $('.header-area').height() - 100;
    $('.main-menu nav ul').onePageNav({
        currentClass: 'active',
        scrollOffset: top_offset,
    });

    // skill
    $(".skill-per").each(function () {
        var $this = $(this);
        var per = $this.attr("per");
        $this.css("width", per + "%");
        $({
            animatedValue: 0
        }).animate({
            animatedValue: per
        }, {
            duration: 1000,
            step: function () {
                $this.attr("per", Math.floor(this.animatedValue) + "%");
            },
            complete: function () {
                $this.attr("per", Math.floor(this.animatedValue) + "%");
            }
        });
    });


    // sticky
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 200) {
            $("#header-sticky").removeClass("sticky-menu");
        } else {
            $("#header-sticky").addClass("sticky-menu");
        }
    });

    // RESPONSIVE MENU
    $('.responsive').on('click', function (e) {
        $('#mobile-menu').slideToggle();
    });

    // meanmenu
    $('#mobile-menu').meanmenu({
        meanMenuContainer: '.mobile-menu',
        meanScreenWidth: "992"
    });

    $('.info-bar').on('click', function () {
        $('.extra-info').addClass('info-open');
    })

    $('.close-icon').on('click', function () {
        $('.extra-info').removeClass('info-open');
    })

    // offcanvas menu
    $(".menu-tigger").on("click", function () {
        $(".offcanvas-menu,.offcanvas-overly").addClass("active");
        return false;
    });
    $(".menu-close,.offcanvas-overly").on("click", function () {
        $(".offcanvas-menu,.offcanvas-overly").removeClass("active");
    });



    // menu toggle
    $(".main-menu li a").on('click', function () {
        if ($(window).width() < 1200) {
            $("#mobile-menu").slideUp();
        }
    });

    // smoth scroll
    $(function () {
        $('a.smoth-scroll').on('click', function (event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - 100
            }, 1000);
            event.preventDefault();
        });
    });

    // counterUp

    $('.count').counterUp({
        delay: 100,
        time: 1000
    });


    // scrollToTop
    $.scrollUp({
        scrollName: 'scrollUp',
        topDistance: '300',
        topSpeed: 300,
        animation: 'fade',
        animationInSpeed: 200,
        animationOutSpeed: 200,
        scrollText: '<i class="fas fa-level-up-alt"></i>',
        activeOverlay: false,
    });

    //for menu active class
    $('.button-group > button').on('click', function (event) {
        $(this).siblings('.active').removeClass('active');
        $(this).addClass('active');
        event.preventDefault();
    });

    // validate contact form 
    $('.cf-form').validate({
        errorClass: "is-invalid",
        error: "invalid-feedback",
    });

    $(".cf-form").on("submit", function (e) {

        var dataString = $(this).serialize();

        // alert(dataString); return false;

        $.ajax({
            type: "POST",
            url: "/contact/",
            data: dataString,
            success: function (data) {
                $(".form-response").text(data.message).removeClass("d-none");
            }
        });

        e.preventDefault();
    });


    // set active nav
    $("nav a").each((element) => {
        $(element).removeClass("current-tab");
    });
    switch (window.location.pathname) {
        case "/":
            $("nav a.home").addClass("current-tab");
            break;
        case "/about/":
            $("nav a.about").addClass("current-tab");
            break;
        case "/services/":
            $("nav a.services").addClass("current-tab");
            break;
        case "/contact/":
            $("nav a.contact").addClass("current-tab");
            break;
    };

})(jQuery);