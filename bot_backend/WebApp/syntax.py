from pygments import highlight
from pygments.lexers import PythonLexer,get_lexer_by_name
from pygments.formatters import HtmlFormatter
from .models import *


def Html(code):
	c = highlight(code.code,get_lexer_by_name(code.lang.name),HtmlFormatter())
	css=code.style.css.read()
	css=css.decode()
	
	c+=f"""<style>\n{css}\n<style/>"""
	return c
