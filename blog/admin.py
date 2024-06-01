from django.contrib import admin
from .models import Post
from .models import About
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','titleImage', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display=('full_name','about','profile_pic')

admin.site.register(About, AboutAdmin)