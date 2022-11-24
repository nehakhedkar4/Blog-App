from django.contrib import admin
from .models import Post,UndoPost

# Register your models here.
# admin.site.register(Post)

@admin.register(UndoPost)
class UndoPostAdmin(admin.ModelAdmin):
    list_display = ('undo_id','username','title','content')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','blog_user','title')
