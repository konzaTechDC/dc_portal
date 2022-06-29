from django.urls import path  
from .views import all_services,webhosting,flavours,category

app_name = 'services'

urlpatterns = [
    path('all_services/<int:servicetype>/', all_services, name='all_services'),
    path('flavours/<int:index>/',  flavours, name='flavours'),
    path('category/<int:index>/',  category, name='category'),
    path('webhosting/', webhosting, name='webhosting'),
    
    
]
