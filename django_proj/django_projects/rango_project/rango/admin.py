from django.contrib import admin
from .models import Category, Page

# Register your models here.
admin.site.register(Page)

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    # Update the registration to include this customised interface

admin.site.register(Category, CategoryAdmin)