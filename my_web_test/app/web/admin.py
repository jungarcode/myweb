
from django.contrib import admin
from .models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','author','published',"post_categories")
    ordering = ('published',)
    search_fields = ('title','content','categories_name')
    list_filter = ('categories__name',)

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description= "category"

admin.site.register(Category)
admin.site.register(Post,PostAdmin)

# Register your models here.
