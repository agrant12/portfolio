jQuery(document).ready(function($){

	/* Set Varibales for Featured Works*/

	var $work = $('#work');
	var $front = $('.front');
	var $back = $('.back');
	var defaultToggleState = true;

	/* Toggle Back on Hover & Set Opacity of Front Div */
	
	$work.on('hover', function(){
		if (defaultToggleState){
			$back.slideDown('fast');

			defaultToggleState = false;
		} else{
			$back.slideUp('fast');

			defaultToggleState = true;
		}
	});

	

	/*$work.hover(function(){
		$back.toggle('fast');
		$
	});*/
});




