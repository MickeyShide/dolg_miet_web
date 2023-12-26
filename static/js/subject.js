$(document).ready(function(){
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
  		$(this).children("div.files_item_left").stop().animate({width: "760px"}, 200);
  		$(this).children("div.files_item_right").stop().animate({width: "130px"}, 200);

  	},
  	function() {
  		$(this).children("div.files_item_left").stop().animate({width: "100%"}, 200);
  		$(this).children("div.files_item_right").stop().animate({width: "0"}, 200);
  	}
  	);
});