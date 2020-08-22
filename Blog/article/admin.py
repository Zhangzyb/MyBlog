from django.contrib import admin
from article.models import Article, Tag, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']
    fields = ['title', 'text', 'abstract', 'category', 'tag']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)


