from django.contrib import admin
from .models import Category #import the category app 

# Register your models here.

#to prepopulate the slug fields 
class CategoryAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug': ('category_name', )}
    list_display = ('category_name', 'slug')


admin.site.register(Category, CategoryAdmin) #we register the model to the admin 

