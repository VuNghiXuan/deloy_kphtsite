
from . import views
from django.urls import path, include


urlpatterns = [       
    path('', views.index, name= 'index'),
    path('infor_company/', views.infor_company, name='infor_company'),
    path('san-pham/<int:san_pham_id>/', views.product_detail, name='product_detail'),
    path('all-products/<int:bo_suu_tap_id>/', views.all_products_in_collection, name='all_products_in_collection'),
    path('search_products/', views.search_products, name='search_products'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # path('update_user/', views.update_user, name='update_user'),
    # path('update_password/', views.update_password, name='update_password'),
    
    # path('register/', views.register_user, name='register'),
]


# print('---------------------------index of cauhinhtrangchu', urlpatterns) register

