var swiper = new Swiper('.swiper.testimoni', {
    spaceBetween: 30,
    freeMode: true,
    navigation: {
        nextEl: '.arrow.next-testimoni',
        prevEl: '.arrow.prev-testimoni',
    },
    breakpoints: {
        0: {
            slidesPerView: 1
        },
        991: {
            slidesPerView: 2
        }
    }
});
var swiper = new Swiper('.swiper.service', {
    spaceBetween: 30,
    freeMode: true,
    navigation: {
        nextEl: '.arrow.next-services',
        prevEl: '.arrow.prev-services',
    },
    breakpoints: {
        0: {
            slidesPerView: 1
        },
        991: {
            slidesPerView: 3
        }
    }
});

$(this).on('scroll', function() {
    if ($(this).scrollTop() >= 50) {
        $('.sticky-top').addClass('sticky-shadow');
        $('#services').addClass('pt-6');
        $('#about').addClass('pt-6');
        $('#project').addClass('pt-6');
        $('#blog').addClass('pt-6');
        $('#contact').addClass('pt-6');
    } else {
        $('#services').removeClass('pt-6');
        $('#about').removeClass('pt-6');
        $('#project').removeClass('pt-6');
        $('#blog').removeClass('pt-6');
        $('#contact').removeClass('pt-6');
        $('.sticky-top').removeClass('sticky-shadow');
    }
});