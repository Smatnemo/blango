from django.contrib import admin

from blog.models import Tag, Post

# Register your models here.
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  # slug field is dependent on title field.
  # Slug field changes when the title field is updated
  prepopulated_fields = {"slug": ("title",)}
  list_display = ['slug', 'published_at']

admin.site.register(Post, PostAdmin)