function update_icons() {
    if ($('#sidebar').hasClass("active")) {
	    $('#sidebar-collapse-icon').addClass('fa-angle-double-right').removeClass('fa-angle-double-left')
    } else {
	    $('#sidebar-collapse-icon').addClass('fa-angle-double-left').removeClass('fa-angle-double-right')
    }
}

function update_sidebar() {
    if ($(window).width() <= 768 && !$('#sidebar').hasClass('active')) {
   	$('#sidebar').addClass('active')
	$('#content').addClass('active')
	update_icons()
    }
}

$(document).ready(function () {
    update_sidebar()

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
	$('#content').toggleClass('active');

	update_icons()
    });
});

$(window).resize(function() {
    update_sidebar()
});
