var Grant = Grant || {};
	Grant.utils = {};

var $window = $(window).width();

Grant.utils.userAgent = function()
{
	var results = {
		"is_mobile" : false,
		"device" : "",
		"url" : ""
	}
};

if (/(iPhone|iPad|iPod|Android)/i.test(navigator.userAgent)) {

	result["is_mobile"] = true;

	if (/(iPad|iPhone)/i.test(navigator.userAgent)) {
		result["url"] = 'http://itunes.apple.com/us/app/radio-com/id364176316?mt=8';
		result["device"] = 'ipad';
	}
	else if (/(Android)/i.test(navigator.userAgent)) {
		result["url"] = 'https://market.android.com/details?id=com.radiocom';
		result["device"] = 'android';
	}
	else {
		result["url"] = "";
		result["device"] = "";
	}
}

Grant.utils.screenSize = function()
{
	var script = {
		"script" : true,
		"src" : "random script"
	}
};

if ( $window <= 480 ){

	script["script"] = true;
	script["src"] = 'random1';

}
