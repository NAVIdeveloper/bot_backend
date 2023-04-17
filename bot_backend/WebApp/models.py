from django.db import models

# Create your models here.

class Style(models.Model):
	css = models.FileField()
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Lexer(models.Model):
	name = models.CharField(max_length=255)
	lang = models.CharField(max_length=255)
	def __str__(self):
		return self.name


class CodeFile(models.Model):
	user = models.IntegerField()
	file_name = models.CharField(max_length=255)
	code = models.TextField()
	lang = models.ForeignKey(Lexer,on_delete=models.SET_NULL,null=True)
	style = models.ForeignKey(Style,on_delete=models.SET_NULL,null=True)
	str_style = models.CharField(max_length=255,null=True,blank=True)
	is_public = models.BooleanField(default=True)
	
	def __str__(self):
		return self.file_name

