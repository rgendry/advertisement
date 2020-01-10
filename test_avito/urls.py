from create.views import get_list, create, get_item
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', get_list),
    path('admin/', admin.site.urls),
    path('api/get_list/', get_list),   
    path('api/get_list/<int:id>', get_item),  
    path('api/create/', create),    
]
