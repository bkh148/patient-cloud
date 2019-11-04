$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');

	if ($('#sidebar').hasClass("active")) {
		$('#sidebar-collapse-icon').addClass('fa-angle-double-right').removeClass('fa-angle-double-left')
	} else {
		$('#sidebar-collapse-icon').addClass('fa-angle-double-left').removeClass('fa-angle-double-right')
	}
    });
});
