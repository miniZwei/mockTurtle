from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
class BookmarkView(admin.ModelAdmin):
    list_display = ('id', 'username', 'quiz_no')

admin.site.register(Bookmark, BookmarkView)
