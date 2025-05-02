from django.contrib import admin
from .models import News,Category
@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    list_display=('title','author','published_date','category')
    last_filter=('category')
admin.site.register(Category)


# Register your models here.
