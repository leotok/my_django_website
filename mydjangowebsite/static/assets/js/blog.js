var i = 0;

$(function() {

	// Ace - https://ace.c9.io/#nav=howto

	$(".editor").each(function() {

		ace.require("ace/ext/language_tools");

		var editor = ace.edit("editor"+i);
	    editor.setTheme("ace/theme/monokai");
	    editor.getSession().setMode("ace/mode/python");
	    editor.setOptions({
	        enableBasicAutocompletion: true,
	        enableSnippets: true,
	        maxLines: Infinity
	  	});
	  
	  	editor.setShowPrintMargin(false);
	  	editor.setHighlightActiveLine(false);

		i++;
	});	

});
