from django.db import models
from django.urls import reverse 
# Create your models here.
class Category(models.Model): 
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    cat_image = models.ImageField(upload_to = 'photos/categories/', blank = True ) #category image with blank = true is optional 

    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'categories' 

    def get_url(self): 
        return reverse('products_by_category', args = [self.slug])#args: taking the category slug 
        #when cliked on the drop-down list of all category, it will links the url of that items 

    def __str__(self): 
        return self.category_name
