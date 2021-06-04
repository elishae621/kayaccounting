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

    /* magnificPopup img view */
    $('.popup-image').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        }
    });

    /* magnificPopup video view */
    $('.popup-video').magnificPopup({
        type: 'iframe'
    });

    // paroller
    if ($('.paroller').length) {
        $('.paroller').paroller();
    }

    //* Parallaxmouse js
    function parallaxMouse() {
        if ($('#parallax').length) {
            var scene = document.getElementById('parallax');
            var parallax = new Parallax(scene);
        };
    };
    parallaxMouse();

    // service active
    $('.s-single-services').on('mouseenter', function () {
        $(this).addClass('active').parent().siblings().find('.s-single-services').removeClass('active');
    })

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


    // isotop
    $('.grid').imagesLoaded(function () {
        // init Isotope
        var $grid = $('.grid').isotope({
            itemSelector: '.grid-item',
            percentPosition: true,
            masonry: {
                // use outer width of grid-sizer for columnWidth
                columnWidth: 1
            }
        });

        // filter items on button click
        $('.button-group').on('click', 'button', function () {
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({
                filter: filterValue
            });
        });

    });
    // isotop
    $(".element").each(function () {
            var a = $(this);
            a.typed({
                strings: a.attr("data-elements").split(","),
                typeSpeed: 100,
                backDelay: 3e3
            })
        }),
        //for menu active class
        $('.button-group > button').on('click', function (event) {
            $(this).siblings('.active').removeClass('active');
            $(this).addClass('active');
            event.preventDefault();
        });

    // WOW active
    new WOW().init();

    //Tabs Box
    if ($('.tabs-box').length) {
        $('.tabs-box .tab-buttons .tab-btn').on('click', function (e) {
            e.preventDefault();
            var target = $($(this).attr('data-tab'));

            if ($(target).is(':visible')) {
                return false;
            } else {
                target.parents('.tabs-box').find('.tab-buttons').find('.tab-btn').removeClass('active-btn');
                $(this).addClass('active-btn');
                target.parents('.tabs-box').find('.tabs-content').find('.tab').fadeOut(0);
                target.parents('.tabs-box').find('.tabs-content').find('.tab').removeClass('active-tab animated fadeIn');
                $(target).fadeIn(300);
                $(target).addClass('active-tab animated fadeIn');
            }
        });
    }

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