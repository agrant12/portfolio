jQuery(document).ready(function($){

	/* Set Varibales for Featured Works*/

	var $work = $('.work');
	var $front = $('.front');
	var $back = $('.back');
	var defaultToggleState = true;

	/* Toggle Back on Hover */
	
	//$work.hide();

	/*$work.each(function(){
		$(this).show();
	});
	
	$work.on('hover', function(){
		if (defaultToggleState){
			
			$(this).find($back).slideDown('fast');

			defaultToggleState = false;
		} else{
			
			$(this).find($back).slideUp('fast');
			
			defaultToggleState = true;
		}
	});*/

	/* Tabs for Work Page */

	function init_tabs(){
		if (!$('.thumbnails').length){
			return;
		}

		$('#main_wrapper').each(function(){
			$(this).find('div.tabbed_content:first').show();
		});

		$('.thumbnails').click(function(){
			if(!$(this).hasClass('current')){
				$(this).addClass('current').parent('li').siblings('li').find('a.current').removeClass('current');
				$($(this).attr('href')).fadeIn("slow").siblings('.tabbed_content').hide();
				
				/* Smooth Scroll back to Top */
				$("html, body").animate({ scrollTop: 0 }, "slow");
			}
			this.blur();
			return false;
		});
	}

	jQuery(document).ready(function(){
		init_tabs();
	});
});




