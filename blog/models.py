from __future__ import unicode_literals
from django.db import models

import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class Post(models.Model):

	data_criacao		= models.DateTimeField(auto_now_add=True)
	ultima_modificacao 	= models.DateTimeField(auto_now=True)
	autor 				= models.CharField(max_length=64, null=True, blank=True)
	texto 				= models.TextField(null=True, blank=True)
	titulo				= models.TextField(unique=True)
	codigo				= models.TextField(null=True, blank=True)
	texto_html			= models.TextField(blank=True, null=True, editable=False)

	def save(self, *args, **kwargs):
		hl_renderer = HighlightRenderer()
		md = mistune.Markdown(renderer=hl_renderer)
		self.texto_html = md(self.texto)
		super(Post, self).save(*args, **kwargs)



class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

