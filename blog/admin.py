from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment
from .models import Tag
from .models import Category

class CommentInlineAdmin(admin.StackedInline):
	model = Comment
	extra = 2

class PostAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'created_at', )
	list_display_links = ('pk', 'title', )
	inlines = [CommentInlineAdmin]
	# ordering = ('-id')
	# search_fields = ('title', 'content',)
	# list_filter('title',)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('pk', 'post_id', 'created_at', 'content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Category)
