$(document).ready(function(){

	var movementStrength = 25;
	var height = movementStrength / $(window).height();
	var width = movementStrength / $(window).width();
	$(document).mousemove(function(e){
		var pageX = e.pageX - ($(window).width() / 2);
		var pageY = e.pageY - ($(window).height() / 2);
		var newvalueX = width * pageX * -1 - 25;
		var newvalueY = height * pageY * -1 - 50;
		$('div.content').css("background-position", newvalueX+"px     "+newvalueY+"px");
});

  $("div.content_middle_item").hover(function() {
  	$(this).dequeue();
  	$(this).animate({
  		boxShadow: "0px 0px 5px 3px rgba(0, 0, 0, 0.1)"
  	}, 200); 
  }, function() {
  	$(this).dequeue();
  	$(this).animate({
  		boxShadow: "0px 0px 5px 3px rgba(0, 0, 0, 0)"
  	}); 
  });


  $("div.top_right").hover(
  	function() {
  		$("div.top_right_white").stop().animate({opacity: 0}, 300);
  	}, function() {
  		$("div.top_right_white").stop().animate({opacity: 0.75}, 300);
  	});


  $("div.header_menu_button").click(
  	function() {
  		var el = $('div.header_menu'),
  		curHeight = el.height(),
	    autoHeight = el.css('height', 'auto').height();
  		if ( curHeight == 0) { 
			el.height(curHeight).stop().animate({height: autoHeight}, 250);
		}
		else if (curHeight == autoHeight) {
			el.height(curHeight).stop().animate({height: 0}, 400);
		}
  	}
  );

  $("div.header_search input").focus(
  	function() {
  		if ($('div.header_menu').height() != 0) {
  			$('div.header_menu').stop().animate({height: 0}, 400);
  		}
  		var header_content = $('div.header_content'),
  			header_title = $('div.header_title'),
  			header_menu_button = $('div.header_menu_button'),
  			header_profile_content = $('div.header_profile_content');
  		$(this).stop().animate({width: header_content.width()-(header_title.width()+header_menu_button.width()+header_profile_content.width()+50)});
  	}
  );

  $("div.header_search input").focusout(
  	function() {
  		$(this).stop().animate({width: '150px'});
  	}
  );

  $(document).on('click', function(event) {
    if ($(event.target).closest("div.header_menu").length || $('div.header_menu').height() == 0) return;
    var el = $('div.header_menu'),
  		curHeight = el.height(),
	    autoHeight = el.css('height', 'auto').height();
	if (curHeight == autoHeight) {
		el.height(curHeight).stop().animate({height: 0}, 400);
	}
});

  $("div.header_profile_content").click(
  	function() {
  		var el = $('div.header_profile_menu'),
  		curHeight = el.height(),
	    autoHeight = el.css('height', 'auto').height();
  		if ( curHeight == 0) { 
			el.height(curHeight).stop().animate({height: autoHeight}, 250);
		}
		else if (curHeight == autoHeight) {
			el.height(curHeight).stop().animate({height: 0}, 400);
		}
  	}
  );

  $(document).on('click', function(event) {
    if ($(event.target).closest("div.header_profile_menu").length || $('div.header_profile_menu').height() == 0) return;
    var el = $('div.header_profile_menu'),
  		curHeight = el.height(),
	    autoHeight = el.css('height', 'auto').height();
	if (curHeight == autoHeight) {
		el.height(curHeight).stop().animate({height: 0}, 400);
	}
});
  $("div.files_item_content").hover(
  	function() {
  		$(this).children("div.files_item_left").stop().animate({width: "760px"});
  		$(this).children("div.files_item_right").stop().animate({width: "130px"});

  	},
  	function() {
  		$(this).children("div.files_item_left").stop().animate({width: "100%"});
  		$(this).children("div.files_item_right").stop().animate({width: "0"});
  	}
  	);
  $("div.login_button input").hover(
  	function() {
  		$("div.login_button input").stop().animate({backgroundColor: "rgb(3, 132, 0)"}, 200);
  	}, function() {
  		$("div.login_button input").stop().animate({backgroundColor: "#04B200"}, 200);
  	});
});