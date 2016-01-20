/* Theme Name: Worthy - Free Powerful Theme by HtmlCoder
 * Author:HtmlCoder
 * Author URI:http://www.htmlcoder.me
 * Version:1.0.0
 * Created:November 2014
 * License: Creative Commons Attribution 3.0 License (https://creativecommons.org/licenses/by/3.0/)
 * File Description: Initializations of plugins
 */

(function($){
	$(document).ready(function(){

		$(".banner-image").backstretch('assets/static/images/Drahi.jpg');

		// Fixed header
		//-----------------------------------------------
		$(window).scroll(function() {
			if (($(".header.fixed").length > 0)) {
				if(($(this).scrollTop() > 0) && ($(window).width() > 767)) {
					$("body").addClass("fixed-header-on");
				} else {
					$("body").removeClass("fixed-header-on");
				}
			};
		});

		$(window).load(function() {
			if (($(".header.fixed").length > 0)) {
				if(($(this).scrollTop() > 0) && ($(window).width() > 767)) {
					$("body").addClass("fixed-header-on");
				} else {
					$("body").removeClass("fixed-header-on");
				}
			};
		});

		//Scroll Spy
		//-----------------------------------------------
		if($(".scrollspy").length>0) {
			$("body").addClass("scroll-spy");
			$('body').scrollspy({
				target: '.scrollspy',
				offset: 152
			});
		}


		//Open modal
		//-----------------------------------------------
		if(window.location.href.indexOf('#register_done') != -1) {
		  $('#register_done').modal('show');
		}

		if(window.location.href.indexOf('#update_done') != -1) {
		  $('#update_done').modal('show');
		}

		if(window.location.href.indexOf('#already_registered') != -1) {
		  $('#already_registered').modal('show');
		}

	}); // End document ready
})(this.jQuery);
