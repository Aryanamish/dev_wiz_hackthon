from django.contrib import admin

from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# creating admin class
class blogadmin(SummernoteModelAdmin):
	# displaying posts with title slug and created time
	list_display = ('title', 'slug', 'date_posted')
	list_filter = ("title", )
	search_fields = ['title', 'content']
	# prepopulating slug from title
	prepopulated_fields = {'slug': ('title', )}
	summernote_fields = ('content', )

# registering admin class
admin.site.register(Post, blogadmin)



