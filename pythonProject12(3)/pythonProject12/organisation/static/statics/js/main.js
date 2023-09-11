$('.banner-carousel').owlCarousel({
    loop: true,
    items: 1,
    margin: 0,
    nav: false,
    dots: false,
    autoplay: true,
    responsive: {
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});
$('.mobile-recognition-carousel').owlCarousel({
    loop: true,
    items: 2,
    margin: 0,
    nav: false,
    autoplay: true,
    dots: false,

});



$('.mobile-achievements-carousel').owlCarousel({
    loop: true,
    items: 1,
    margin: 0,
    autoplay: true,
    nav: false,
    dots: true,

});

$('.placements-carousel').owlCarousel({
    loop: true,
    animateOut: 'fadeOut',
    autoplay: true,
    margin: 0,
    nav: false,
    dots: true,
    autoplay: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});
$('.our-recruiters-carousel').owlCarousel({
    loop: true,
    animateOut: 'fadeOut',
    autoplay: true,
    nav: false,
    autoplay: true,
    responsive: {

        0: {
            items: 2,
            dots: true,
            margin: 15,
        },
        991: {
            margin: 20,
        },

        992: {
            items: 1,
            dots: false,
        }
    }
});

$('.founder-project-carousel').owlCarousel({
    loop: true,
    animateOut: 'fadeOut',
    autoplay: true,
    margin: 0,
    items: 1,
    nav: true,
    dots: false,
    responsive: {


        600: {
            items: 1
        },
    }
});

$('.testimonials-carousel').owlCarousel({
    loop: true,
    animateOut: 'fadeOut',
    autoplay: true,
    margin: 20,
    items: 1,
    nav: false,
    autoplay: true,
    // loop:true,
    // animateOut: 'fadeOut',
    // autoplay:true,
    // margin:0,
    // items:1,
    // nav:false,
    // autoplay: true,
    // dots:true,
    responsive: {
        600: {
            items: 1,
            dots: true,
        },
        992: {
            items: 1,
        },
    }
});
$('.research-carousel').owlCarousel({
    loop: true,
    autoplay: false,
    margin: 0,
    nav: false,
    dots: true,
    autoplay: true,
    responsive: {

        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});
$('.research-fact-slider').owlCarousel({
    loop: true,
    margin: 0,
    nav: false,
    dots: true,
    autoplay: true,
    responsive: {

        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});
$('.p-highlight-carousel').owlCarousel({
    loop: true,
    autoplay: false,
    margin: 22,
    item: 3,
    nav: true,
    navText: ["<img src='/images/More-Button.png'>", "<img src='/images/More-Button.png'>"],
    dots: false,
    responsive: {
        0: {
            items: 1
        },
        575: {
            items: 2
        },
        1000: {
            items: 2
        },
        1100: {
            items: 3
        }

    }
});
$('.p-testimonials-carousel').owlCarousel({
    loop: true,
    animateOut: 'fadeOut',
    autoplay: true,
    margin: 0,
    nav: false,
    autoplay: true,
    responsive: {
        0: {
            items: 1
        },
        1000: {
            items: 1
        },
        600: {
            items: 1
        }
    }
});


$('.about_notable-carousel').owlCarousel({
    items: 1,
    loop: true,
    margin: 40,
    nav: true,
    navText: ["<img src='/images/More-Button.png'>", "<img src='/images/More-Button.png'>"],
    dots: false,
    responsive: {
        500: {
            items: 1
        },
        767: {
            items: 2.8,
        },
        1100: {
            items: 3.8
        },
        1649: {
            items: 3.8
        },
        1920: {
            items: 3.8
        }
    }
});

$('.program_industry-carousel').owlCarousel({
    item: 1,
    loop: true,
    margin: 0,
    nav: true,
    dots: false,
    responsive: {

        0: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});

$('.program_industry-carousel2').owlCarousel({
    item: 1,
    loop: true,
    margin: 0,
    nav: true,
    dots: false,
    responsive: {

        0: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});

$('.Research_Innovation_carousel').owlCarousel({
    item: 2,
    loop: true,
    margin: 15,
    nav: true,
    dots: false,
    responsive: {

        1000: {
            items: 2
        },
        300: {
            items: 1
        }
    }
});


$('.notice-panel_carousel').owlCarousel({
    item: 1,
    loop: true,
    margin: 15,
    nav: false,
    dots: true,
    responsive: {

        0: {
            items: 1
        },
        1000: {
            items: 1
        }

    }
});


// sticky-navbar
$(window).scroll(function() {
    var sticky = $('.header'),
        scroll = $(window).scrollTop();

    if (scroll >= 100) sticky.addClass('sticky');
    else sticky.removeClass('sticky');
});
// burger-menu
$(document).ready(function() {
    if (true) {
        $('.burger').click(function(event) {
            $(this).toggleClass('active');
            $('.menu-item').toggleClass('active')
        })
    } else {
        $('.burger').click(function(event) {
            $(this).removeClass('active')
            $('.menu-item').removeClass('active')


        })
    }

})



$(document).ready(function() {

    $('.active1').addClass('active')
    $('.active2').hover(function() {
        $('.mega-right-content.active-item2').css("display", "flex")
        $('.mega-right-content.active-item1').css("display", "none")
        $('.mega-right-content.active-item3').css("display", "none")
        $(this).addClass('active')
        $('.active1').removeClass('active')
        $('.active3').removeClass('active')
    })
    $('.active3').hover(function() {
        $('.mega-right-content.active-item2').css("display", "none")
        $('.mega-right-content.active-item1').css("display", "none")
        $('.mega-right-content.active-item3').css("display", "flex")
        $(this).addClass('active')
        $('.active1').removeClass('active')
        $('.active2').removeClass('active')
    })
    $('.active1').hover(function() {
        $('.mega-right-content.active-item2').css("display", "none")
        $('.mega-right-content.active-item1').css("display", "flex")
        $('.mega-right-content.active-item3').css("display", "none")
        $(this).addClass('active')
        $('.active3').removeClass('active')
        $('.active2').removeClass('active')
    })
})

// gallery-detail-crousle
var $owl = $('.gallery-detail-pannel .owl-carousel');

$owl.children().each(function(index) {
    $(this).attr('data-position', index); // NB: .attr() instead of .data()
});

$owl.owlCarousel({
    center: true,
    loop: true,
    item: 3,
    responsive: {

        1000: {
            items: 3
        },
        600: {
            items: 1
        },

    }
});

$(document).on('click', '.owl-item>div', function() {
    // see https://owlcarousel2.github.io/OwlCarousel2/docs/api-events.html#to-owl-carousel
    var $speed = 300; // in ms
    $owl.trigger('to.owl.carousel', [$(this).data('position'), $speed]);
});



$('.mobile-menu').click(function() {
    $('.mobile-notice-panel').toggleClass('show');
    $('.help-suppoert-panel').removeClass('show');
    $('.appointment-panel').removeClass('show');
    $('.call-panel').removeClass('show');
});
$('.close-btn').click(function() {
    $('.mobile-notice-panel').removeClass('show');
})

$('.help-support').click(function() {
    $('.help-suppoert-panel').toggleClass('show');
    $('.mobile-notice-panel').removeClass('show');
    $('.appointment-panel').removeClass('show');
    $('.call-panel').removeClass('show');
});
$('.close-btn').click(function() {
    $('.help-suppoert-panel').removeClass('show');

})

$('.appointments-li').click(function() {
    $('.appointment-panel').toggleClass('show');
    $('.mobile-notice-panel').removeClass('show');
    $('.help-suppoert-panel').removeClass('show');
    $('.call-panel').removeClass('show');
});
$('.close-btn').click(function() {
    $('.appointment-panel').removeClass('show');
})

$('.call-li').click(function() {
    $('.call-panel').toggleClass('show');
    $('.appointment-panel').removeClass('show');
    $('.mobile-notice-panel').removeClass('show');
    $('.help-suppoert-panel').removeClass('show');
});
$('.close-btn').click(function() {
    $('.call-panel').removeClass('show');
})



$('.mobile_menu_list li').click(function() {
    $('.active').removeClass('active');
    $(this).addClass('active');
});


$(".menu-bx-inn a").click(function() {
    var e = $(this),
        o = e.closest("ul"),
        s = o.find(".active"),
        a = e.closest("li"),
        i = a.hasClass("active"),
        t = 0;
    o.find("ul").slideUp(function() {
        ++t == o.find("ul").length && s.removeClass("active")
    }), i || (a.children("ul").slideDown(), a.addClass("active"))
})






//     $(document).ready(function(){
// $('.drop-menu').mouseenter(function(){
//      $('body').addClass('active');
// })
// $('.drop-menu').mouseleave(function(){
//      $('body').removeClass('active');
// })
// })

$(".drop-menu").hover(
    function() {
        $("header").toggleClass("header_hover");
    },
);



// tab-accordian
// $(document).ready(function () {
//     $('#heading-V').click(function () {
//         $('#collapse-V').toggleClass('show');
//         $('#collapse-B').removeClass('show')
//         $('#collapse-C').removeClass('show')
//         $('#collapse-D').removeClass('show')
//     })
//     $('#heading-B').click(function () {
//         $('#collapse-B').toggleClass('show');
//         $('#collapse-V').removeClass('show')
//         $('#collapse-C').removeClass('show')
//         $('#collapse-D').removeClass('show')
//     })
//     $('#heading-C').click(function () {
//         $('#collapse-C').toggleClass('show');
//         $('#collapse-V').removeClass('show')
//         $('#collapse-B').removeClass('show')
//         $('#collapse-D').removeClass('show')
//     })
//     $('#heading-D').click(function () {
//         $('#collapse-D').toggleClass('show');
//         $('#collapse-V').removeClass('show')
//         $('#collapse-B').removeClass('show')
//         $('#collapse-C').removeClass('show')

//     })

// })


$('.moreless-button').click(function() {
    $('.moretext').slideToggle();
    if ($('.moreless-button').text() == "+") {
        $(this).text("-")
    } else {
        $(this).text("+")
    }
});

$('.moreless-button1').click(function() {
    $('.moretext1').slideToggle();
    if ($('.moreless-button1').text() == "+") {
        $(this).text("-")
    } else {
        $(this).text("+")
    }
});

/*-----Sanjeev js-26-05-2023-end-------*/


/*-----Sanjeev js-26-05-2023-end-------*/


//--khurseed--24-05-2023--//

$('.acdlibrary_slider').owlCarousel({
    loop: true,
    autoplay: false,
    margin: 40,
    nav: false,
    dots: false,
    responsive: {
        0: {
            items: 2
        },
        400: {
            items: 3
        },
        600: {
            items: 3
        },
        1000: {
            items: 3
        },
        1500: {
            items: 3
        },
    }
});

//--Tab-accordian--25-05-2023--//
$(document).ready(function() {
    //its for horizontalTab tab by-Khurseed Ahmad-//
    $('.horizontalTab').easyResponsiveTabs({
        type: 'default', //Types: default, vertical, accordion
        width: 'auto', //auto or any width like 600px
        fit: true, // 100% fit in a container
        closed: 'accordion', // Start closed if in accordion view
        activate: function(event) { // Callback function if tab is switched
            var $tab = $(this);
            var $info = $('#tabInfo');
            var $name = $('span', $info);
            $name.text($tab.text());
            $info.show();
        }
    });
    //its for vertical tab by-Khurseed Ahmad-//
    $('.verticalTab').easyResponsiveTabs({
        type: 'vertical',
        width: 'auto',
        fit: true
    });
});

$('.program_overlist li').click(function() {
    $('.program_overlist li').removeClass('active');
    $(this).addClass('active');
});
//--active-class-program-overview--//

//   $(document).ready(function() {
// 	var s = $(".program_overlist");
// 	var pos = s.position();
// 	$(window).scroll(function() {
// 		var windowpos = $(window).scrollTop();
// 		if (windowpos >= pos.top & windowpos <=3800) {//--scroll amount according the sccroll remove--//
// 			s.addClass("sticky");
// 		} else {
// 			s.removeClass("sticky");
// 		}
// 	});
// });

$(document).ready(function() {
    $(window).scroll(function() {
        if (($(window).scrollTop() > 150) && ($(window).scrollTop() + $(window).height() < $(document).height() - 600)) {
            $(".program_overlist").addClass('sticky');
        } else {
            $(".program_overlist").removeClass('sticky');
        }
    });
});



//--add-stickeyon scroll--//
$('.program_testimonial').owlCarousel({
    loop: true,
    autoplay: false,
    nav: false,
    dots: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1500: {
            items: 1
        },
    }
});
//--khurseed--25-05-2023--end-//


// Sanjeev
$(document).ready(function() {
    $(".researchinnovationtree").owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        dots: true,
        //   autoplay: true,
        //   autoplayTimeout: 1000,
        //   autoplayHoverPause: true,
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>"
        ],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            768: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });


    $(".nest").on("click", function() {
        if ($(this).closest('li').hasClass("active1")) {
            $(this).closest('li').removeClass('active1')
            $(this).siblings('.inner').slideUp(300).removeClass('show')
        } else {
            $(this).closest('.accordion').find('.inner.show').removeClass('show').slideUp(300)
            $(this).closest('.accordion').find('li.active1').removeClass('active1')
            $(this).siblings('.inner').slideDown(300).addClass('show');
            $(this).closest('li').addClass('active1')
        }

    });

    $('.course-type').click(function() {
        $(this).addClass('active');
        let target = $(this).data('target');
        let layers = $(this).closest('.component').find('.side-menu');
        layers.removeClass('show-menu');
        $(`.component ${target}`).addClass('show-menu');
    })
    $('.close-layer').click(function(e) {
        e.preventDefault();
        $(this).closest('.side-menu').removeClass('show-menu');
        $('.course-type.active').removeClass('active')
    })
});


//-------Notices & Announcements------------//
$(document).ready(function() {
    $(window).scroll(function() {
        if (($(window).scrollTop() > 150) && ($(window).scrollTop() + $(window).height() < $(document).height() - 600)) {
            $(".filter-accord").addClass('fixed_top');
        } else {
            $(".filter-accord").removeClass('fixed_top');
        }
    });
});

//-------on click reacch section------------
$('.program_overlist li a').click(function() {
    $('html, body').animate({
        scrollTop: $($(this).attr('href')).offset().top - 100
    }, 0);
    return false;
});

//-------on click reacch section-end-----------

// ---------------search--------
function openSearch() {
    document.getElementById("myOverlay").style.display = "block";
}

function closeSearch() {
    document.getElementById("myOverlay").style.display = "none";
}