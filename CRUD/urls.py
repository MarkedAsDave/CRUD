from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('', views.home, name="home"),
    #add item
    path('add_item', views.add_item, name="add_item"),
    #view item individually
    path('item/<str:item_id>', views.item, name="item"),
    #edit item
    path('edit_item', views.edit_item, name="edit_item"),
    #delete item
    path('delete_item/<str:item_id>', views.delete_item, name="delete_item"),
]
