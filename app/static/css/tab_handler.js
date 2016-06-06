$(document).ready(function() {

	//Default action on page load:

	//Hide all content
	$(".tab_content").hide();
	$(".subtab_content").hide();

	//Highlight first tab button
	$(".tabs a:first").addClass("active").show();
	$(".subtabs a:first").addClass("active").show();

	//Show first tab content
	$(".tab_content:first").show();
	$(".subtab_content:first").show();

	//When a tab button is clicked:
	$(".tabs a").click(function() {

		//Remove any "active" class
		$(".tabs a").removeClass("active");

		//Add the "active" class to the clicked tab
		$(this).addClass("active");
		//Hide all tab content

		$(".tab_content").hide();
		//Find the reference to the active tab button

		var activeTab = $(this).attr("href");

		//Fade in the active content (speed in milliseconds)
		$(activeTab).fadeIn(500);
		return false;
	});
	$(".subtabs a").click(function() {

		//Remove any "active" class
		$(".subtabs a").removeClass("active");

		//Add the "active" class to the clicked tab
		$(this).addClass("active");
		//Hide all tab content

		$(".subtab_content").hide();
		//Find the reference to the active tab button

		var activeTab = $(this).attr("href");

		//Fade in the active content (speed in milliseconds)
		$(activeTab).fadeIn(500);
		return false;
	});

});
