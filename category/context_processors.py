from .models import Category 

def menu_links(request): 
    links = Category.objects.all()
    return dict(links=links) #store all the category into the links variable 
