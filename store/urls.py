from django.urls import path
from . import views 
urlpatterns = [
    path('', views.store, name = 'store'),
    path('<slug:category_slug>/', views.store, name = 'products_by_category'),#how we set the path in the website 
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

] 
