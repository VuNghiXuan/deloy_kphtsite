
from django.urls import path, include
from .views import scan_view, stop_scan

urlpatterns = [       
    path('', scan_view, name= 'scan_view'),
    path('stop-scan/', stop_scan, name= 'stop_scan'),
     
]


# print('---------------------------index of cauhinhtrangchu', urlpatterns)

