from django.shortcuts import render
from .syntax import Html
from .models import *
# Create your views here.


def Code_View(request,pk):
	try:
		code = CodeFile.objects.get(id=pk)
		user = request.GET['user']
		if (code.is_public) or (code.user == user):
			html_code = Html(code)
			
			DATA = {
				"html_code":html_code,
				"code":code,
				}
			return render(request,"code.html",DATA)
		else:
			return render(request,"404.html")
	except Exception as e:
		print(e)
		return render(request,"404.html")
