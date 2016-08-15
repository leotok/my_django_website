var i = 0;

$(function() {
	$(".editor").each(function() {

		ace.require("ace/ext/language_tools");

		var editor = ace.edit("editor"+i);
	    editor.setTheme("ace/theme/monokai");
	    editor.getSession().setMode("ace/mode/python");
	    editor.setOptions({
	        enableBasicAutocompletion: true,
	        enableSnippets: true
	  	});
	  
	  	editor.setShowPrintMargin(false);
	  	editor.setHighlightActiveLine(false);

		i++;
	});	

});
