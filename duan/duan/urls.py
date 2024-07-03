"""
URL configuration for duan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings 
from django.conf.urls.static import static
from IIcauhinhtrangchu import views

urlpatterns = [
    path('', include('IIcauhinhtrangchu.urls')),

    path('barcode/', include('barcodeScaner.urls')),
    # Vào trang: "api"
    path('api/', include('Ithongtincongty.urls')),
    path('cart/', include('VIIgiohang.urls')),
    path('sys/', include('hethong.urls')),
    path('payment/', include('VIIItratien.urls')),
    
    # Chứng thực và vào trang: "o/applications"
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

"Tạm thời comment lại"
# # Nếu sử dụng static files trong môi trường phát triển (xóa nếu không cần)
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     # print('---------------------------True of kphtsite', urlpatterns)
# else:
#     urlpatterns += staticfiles_urlpatterns()
#     # print('---------------------------False of kphtsite', urlpatterns)

# Config title admin
admin.site.site_title = 'ĐĂNG NHẬP HỆ THỐNG'
admin.site.site_header = 'TRANG HỆ THỐNG QUẢN TRỊ'
admin.site.index_title = 'DANH MỤC CHỨC NĂNG HỆ THỐNG'