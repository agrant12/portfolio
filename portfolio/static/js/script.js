
	/*$(function(){
		$(window).scroll(function(){
			var offset = $(window).scrollTop();
			$('.title_page').animate({
				'top': offset + 'px'
			});
			$('.work_content').animate({
				'top': '-' + offset + 'px'
			});
		});
	});


jQuery(document).ready(function($){

	/* Tabs for Work Page */

	/*function init_tabs(){
		if (!$('.thumbnails').length){
			return;
		}

		$('#main_wrapper').each(function(){
			$(this).find('.tabbed_content:first').hide();
		});

		$('.thumbnails').click(function(){
			if(!$(this).hasClass('current')){
				$(this).addClass('current').parent('li').siblings('li').find('a.current').removeClass('current');
				$($(this).attr('href')).fadeIn("slow").siblings('.tabbed_content').hide();
				
				/* Smooth Scroll back to Top */
	/*			$("html, body").animate({ scrollTop: 0 }, "slow");
			}
			this.blur();
			return false;
		});
	}

	jQuery(document).ready(function(){
		init_tabs();
	});
});*/

jQuery(document).ready(function($){
	if (!$('.thumbnails').length){
		return;
	}

	$('.thumbnails').click(function(e){
		e.preventDefault();
		$('.lightbox').fadeIn();
		$('body').css({
			overflow : 'hidden'
		});
	});

	$('.lightbox').click(function(){
		$(this).fadeOut();
		$('body').css({
			overflow : ''
		});
	});
});




