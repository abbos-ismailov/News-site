from django.contrib import admin
from .models import Contact, Category, Tags, Social, News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'user', 'category', 'create_at', 'view_count']
    readonly_fields = ['view_count']
    prepopulated_fields = {"slug": ("title",),}

admin.site.register(News, NewsAdmin)
admin.site.register(Tags)
admin.site.register(Social)
admin.site.register(Category)
admin.site.register(Contact)