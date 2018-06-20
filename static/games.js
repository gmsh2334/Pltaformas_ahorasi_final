$(".project-name").click(function(){
		var url = window.location.href;
		var name = this.text().replace(" ", "").toLowerCase();
        window.location(url + "/" + name);
	});