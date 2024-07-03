
from django.urls import path, include
from . import views

urlpatterns = [       
    path('payment_success/', views.payment_success, name= 'payment_success'),
    path('check_out/', views.check_out, name= 'check_out'),
    path('billing_info/', views.billing_info, name= 'billing_info'),
    path('process_order/', views.process_order, name= 'process_order'),
    path('shipping_dash/', views.shipping_dash, name= 'shipping_dash'),
    path('not_shipping_dash/', views.not_shipping_dash, name= 'not_shipping_dash'),
    path('orders/<int:order_id>/', views.order_detail, name= 'order_detail'),
    # process_order
    
]


# print('---------------------------index of cauhinhtrangchu', urlpatterns)

