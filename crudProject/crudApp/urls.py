from django.urls import path
from .views import *
urlpatterns = [
     path('', home,name="home"),
     path('form/', form,name='form'),
     path('contact/', contact,name='contact'),
     path('about/', about,name='about'),
     path('delete/<int:id>', delete_data,name='delete'),
     path('edit/<int:id>', edit,name='edit'),
     path('search/', search,name='search'),
     path('bin/', bin,name='bin'),
     path('restore/<int:id>', restore,name='restore'),
     path('delete_bin/<int:id>', delete_bin,name='delete_bin'),
     
     
     # _________________________________________________________
     # _________________________________________________________
     # Authentication part
     
     path('log_in/',log_in,name='log_in'),
     path('register/',register,name='register')
     
     
]
