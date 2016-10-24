I've been searching for different ways of presenting code snippets on my ongoing blog and for now I've found 3 that were most satisfying.

1. Gist (from Github)
2. CodeHilite (with Pygments with Markdown)
3. Ace Code Editor

I'll introduce them and talk about the things that I liked and disliked about them

---

## Gist

#### - Example

<script src="https://gist.github.com/leotok/0ba6b81fd43e846d56a20e479312bbdf.js"></script>

By far, this is the easiest way of adding a code snippet. Gist stores all of the code you want to present on your Github account and it gives you a script so it can be added and rendered on your blog. It keeps all of your code together and organized online. The downside is that you don't have direct access to that piece of code when you're editing your post.

#### - How to 

Add your code file to [gist.github](https://gist.github.com) and then add their script to your post and it will be rendered automagicly.


```html
<script src="https://gist.github.com/leotok/0ba6b81fd43e846d56a20e479312bbdf.js"></script>
```

---

## pygments

#### - Example

```python
def hello(someone="World"):
	print "Hello " + someone

hello("everyone")
```

#### - How to

On your ```models.py``` add the following:

```python
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class Post(models.Model):

	# other attributes...
	text 		= models.TextField(null=True, blank=True)
	text_html	= models.TextField(blank=True, null=True, editable=False)

	def save(self, *args, **kwargs):
		hl_renderer = HighlightRenderer()
		md = mistune.Markdown(renderer=hl_renderer)
		self.text_html = md(self.texto)
		super(Post, self).save(*args, **kwargs)


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)
```
 
It will convert all your code inside Markdown/Mistune text to a highlighted code and save it in HTML format.

You'll also need to provide the CSS with de correct colors for each of the keyword classes. You can many find these stylesheet with different themes online.
Ex:
```css
.highlight pre { background-color: #272822; border-color: transparent;}
.highlight .hll { background-color: #272822; }
.highlight .c { color: #75715e } /* Comment */
.highlight .k { color: #66d9ef } /* Keyword */
.highlight .l { color: #ae81ff } /* Literal */
.highlight .n { color: #f8f8f2 } /* Name */
.highlight .o { color: #f92672 } /* Operator */
/* many other classes... */

```
---

## Ace Code Editor

#### - Example

<div class="jumbotron editor" id="ace-example">
def hello(someone="World"):
	print "Hello " + someone

hello("everyone")
</div>

#### - How to

Add the the script below to your HTML together with the Ace lib. You can either download and serve it from your static files or load from a CDN. You can change the options according to your needs.

```javascript
var i = 0;
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
```

This script will transform all your ```<div>``` elements with class ```editor``` into a highlighted code snippet and it also lets you create a full-featured online code editor just like Sublime Text with themes.

---

### Reference:

- [gist.github](https://gist.github.com)
- [Pygments](http://pygments.org)
- [Mistune](https://github.com/lepture/mistune)
- [CodeHilite](https://pythonhosted.org/Markdown/extensions/code_hilite.html)
- [Ace Code Editor](https://ace.c9.io/#nav=about)