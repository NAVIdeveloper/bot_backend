from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Style)
admin.site.register(CodeFile)
admin.site.register(Lexer)
