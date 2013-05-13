jQuery(document).ready(function($){

	/* Set Varibales for Featured Works*/

	var $work = $('.work');
	var $front = $('.front');
	var $back = $('.back');
	var defaultToggleState = true;

	/* Toggle Back on Hover */

	$work.on('hover', function(){
		if (defaultToggleState){
			
			$(this).find($back).slideDown('fast');

			defaultToggleState = false;
		} else{
			
			$(this).find($back).slideUp('fast');
			
			defaultToggleState = true;
		}
	});
});




