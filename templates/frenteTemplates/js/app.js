$(document).ready(function(){
	$(".menu_option").click(function() {
		$(".menu_option").removeClass("activate");
		$(this).addClass("activate");
	});
});