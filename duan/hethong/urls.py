
from . import views
from django.urls import path, include


urlpatterns = [       
    
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),
    path('user_permissions/', views.user_permissions, name='user_permissions'),
    
    # path('register/', views.register_user, name='register'),
]


# print('---------------------------index of cauhinhtrangchu', urlpatterns) register

