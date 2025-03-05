from django.contrib import admin
from .models import Post,Category,Content

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','content')
    list_filter=('created_at','category')
    search_fields=('title','content')





admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Content)