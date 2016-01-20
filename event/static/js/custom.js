$(document).ready(function () {
    $('#imaps').addClass('scrolloff'); // set the pointer events to none on doc ready
    $('#mcanvas').on('click', function () {
        $('#imaps').removeClass('scrolloff'); // set the pointer events true on click
    });

    // you want to disable pointer events when the mouse leave the canvas area;

    $("#imaps").mouseleave(function () {
        $('#imaps').addClass('scrolloff'); // set the pointer events to none when mouse leaves the map area
    });

    //Smooth Scroll
    //-----------------------------------------------
    if ($(".smooth-scroll").length>0) {
        $('.smooth-scroll a[href*=#]:not([href=#]), a[href*=#]:not([href=#]).smooth-scroll').click(function() {
            if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top-151
                    }, 1000);
                    return false;
                }
            }
        });
    }

    // Animations
    //-----------------------------------------------
    if (($("[data-animation-effect]").length>0) && !Modernizr.touch) {
        $("[data-animation-effect]").each(function() {
            var $this = $(this),
            animationEffect = $this.attr("data-animation-effect");
            if(Modernizr.mq('only all and (min-width: 768px)') && Modernizr.csstransitions) {
                $this.appear(function() {
                    setTimeout(function() {
                        $this.addClass('animated object-visible ' + animationEffect);
                    }, 400);
                }, {accX: 0, accY: -130});
            } else {
                $this.addClass('object-visible');
            }
        });
    };

	// Isotope filters
	//-----------------------------------------------
	if ($('.isotope-container').length>0) {
		$(window).load(function() {
			$('.isotope-container').fadeIn();
			var $container = $('.isotope-container').isotope({
				itemSelector: '.isotope-item',
				layoutMode: 'masonry',
				transitionDuration: '0.6s',
				filter: "*"
			});
			// filter items on button click
			$('.filters').on( 'click', 'ul.nav li a', function() {
				var filterValue = $(this).attr('data-filter');
				$(".filters").find("li.active").removeClass("active");
				$(this).parent().addClass("active");
				$container.isotope({ filter: filterValue });
				return false;
			});
		});
	};

	//Modal
	//-----------------------------------------------
	if($(".modal").length>0) {
		$(".modal").each(function() {
			$(".modal").prependTo( "body" );
		});
	}
});
