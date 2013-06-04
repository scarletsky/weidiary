from django.contrib import admin
from diary.models import *

class DiaryAdmin(admin.ModelAdmin):
	list_display = ['user', 'date', 'content']

class CoverAdmin(admin.ModelAdmin):
	list_display = ['user', 'year', 'month', 'imgurl']

class FeedAdmin(admin.ModelAdmin):
	list_display = ['user', 'title', 'content']

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Cover, CoverAdmin)
admin.site.register(Feed, FeedAdmin)
