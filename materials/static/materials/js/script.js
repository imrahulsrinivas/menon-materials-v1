/*------------------------------------------------------------------
* Bootstrap Simple Admin Template
* Version: 2.0
* Author: Alexis Luna
* Copyright 2020 Alexis Luna
* Website: https://github.com/alexis-luna/bootstrap-simple-admin-template
-------------------------------------------------------------------*/
// Toggle sidebar on Menu button click

var document_width, document_height;

$(document).ready(function()
{
	document_width=$(document).width(); document_height=$(document).height();
    // Do something
})


if ($(window).width() <= 768) {
    $('#sidebar, #body').addClass('active');
}

$('#sidebarCollapse').on('click', function() {
    $('#sidebar').toggleClass('active');
    $('#body').toggleClass('active');
});

//Auto-hide sidebar on window resize if window size is small
$(window).on('resize', function () {
	if(document_width!=$(document).width() || document_height!=$(document).height()) {
	    if ($(window).width() <= 768) {
	        $('#sidebar, #body').addClass('active');
	    }
	}

});


//Auto-hide sidebar on window resize if window size is small
$(window).on('resize', function () {
    if(document_width!=$(document).width() || document_height!=$(document).height()) {
	    if ($(window).width() > 768) {
        	$('#sidebar, #body').removeClass('active');
    	}
    }
});