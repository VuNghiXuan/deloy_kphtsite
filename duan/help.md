
# Package
    Python 3.11.9
    asgiref              3.8.1
    certifi              2024.2.2
    cffi                 1.16.0
    charset-normalizer   3.3.2
    cryptography         42.0.5
    Django               5.0.4
    django-oauth-toolkit 2.3.0
    djangorestframework  3.15.1
    idna                 3.7
    jwcrypto             1.5.6
    oauthlib             3.2.2
    pillow               10.3.0
    pip                  24.0
    pycparser            2.22
    requests             2.31.0
    sqlparse             0.5.0
    typing_extensions    4.11.0
    tzdata               2024.1
    urllib3              2.2.1

    - Tạo file requirements.txt: pip freeze > requirements.txt
    - Cài file requirements.txt: pip install -r requirements.txt

# Khởi tạo môi trường cài đặt (môi trường ảo)
    1.1 Cài đặt môi trường:
        
        D:\ThanhVu\GIthub_VuNghiXuan\backend>py -m venv env
        hoặc sử dụng VSC>View>Command Palette>Python Select Intepreter>Create Environ
        
        Kích hoạt: D:\ThanhVu\GIthub_VuNghiXuan\backend>env\Scripts\activate.bat
        --> ghi chú dấu "\" ngược

        --> cài đặt requirements.txt


    1.2 ---------*** Kinh nghiệm tạo dự án và User trước trình tự theo link sau: ***--------------- 
        - Tài liệu: https://django-oauth-toolkit.readthedocs.io/en/latest/getting_started.html
        - Giải thích mục đích tạo ra django-oauth-toolkit: https://gemini.google.com/app/1f0b9b2cf2469c53
        - clip tham khảo: https://www.youtube.com/watch?v=5CiOH7AmuxQ&list=PLbiEmmDApLby83031AFtpTw2WUS9tvlEB&index=19
        code:
                models.py:
                    from django.contrib.auth.models import AbstractUser

                    class User(AbstractUser):
                        avatar = models.ImageField(upload_to='up_loads/%Y/%m')
                
                settings.py:
                    AUTH_USER_MODEL = 'thongtincongty.User'
    
    1.3 Cài đặt django: project, app
    1.4 Cài đặt rest framework
    1.5 Chạy makemigrations và migrate
    1.6 http://127.0.0.1:8000/o/applications/
        1.6.1 -->click here: Đăng ký
        1.6.2 Register a new application
            Tất cả giữ nguyên, ngoại trừ 3 mục sau:
                name: kphtapp (tự đặt)
                Client type: chọn-->Confidential
                Authorization grant type: Chọn --> Resource Owner passwork base (nghĩa là giữ pw ban đầu để lấy token ra)

                Trong đó: Client id, Client secret để gởi requests xin đăng nhập và ủy quyền 

        1.6.3 Đăng nhập trang o/applications, o/token
            Copy domain vào PostMan: http://127.0.0.1:8000/o/token/
            Chọn POST -> Chuyển qua body-->Chọn Form-data
            key: 
                username: abc
                password: 123456
                client_id: h436SJs07Mpb8mMmOnHabQVS4EAYStsJOfXo1XYs
                client_secret: pbkdf2_sha256$720000$fFZp6pueX3l29pvg8SJnBw$XcY66yD2eicW2XwkSrEuDucEQ33603PSJUGYXuuVT40=
                grant_type: password
            --> runserver lại --> nhấn Send



# hỏi về việc tạo ra sản phẩm: https://groups.google.com/g/django-users/c/PRJssr6_J5U

# Note:
    
    1. User and password
    user: admin
    pw: 123456

    2. Thay đổi tiếng việt
    settings.py: 
        Comment dòng: # LANGUAGE_CODE = 'en-us'
        Thêm dòng: LANGUAGE_CODE = 'vi'
    
    3. Thay title Form đăng nhập
        Cách 1: Customize Django Admin Titles - Django Wednesdays #20
            # Config title admin trong urls.py của app main
            admin.site.site_title = 'Đăng nhập hệ thống'
            admin.site.site_header = 'Trang quản trị hệ thống'
            admin.site.index_title = 'DANH MỤC CHỨC NĂNG HỆ THỐNG'

        cách 2:
            Vào file settings.py ("INSTALLED_APPS/'django.contrib.admin'")-->ctrl+chuột đi vào admin.py
            --> file sites.py
            --> from django.contrib.admin.decorators import action, display, register
            --> action
            -->from django.contrib.admin.sites import AdminSite
            Trong class AdminSite:
                site_title = gettext_lazy("Django site admin")
                site_header = gettext_lazy("Django administration") 
                index_title = gettext_lazy("Site administration")

# Fix
    1. Apche cho xampp
        Khắc phục lỗi "Apache shutdown unexpectedly" trên XAMPP, Apache: 
        https://www.tinhocsoctrang.com/2018/01/khac-phuc-loi-apache-shutdown-unexpectedly-tren-xampp-apache.html

        OK: Khai báo lại push config trên xampp cổng 8090, 4443
    2 "Not Found: /admin
        [15/Apr/2024 05:52:57] "GET /admin HTTP/1.1" 404 2688"
        Mô tả: Lỗi trên và trang HTml không tìm thấy "media admin"
        Sửa lỗi: tạo dự án django ở chỗ khác, rồi tạo tạo khoản mới, sau khi thành công --> Quay lại mở dự án bị lỗi

# Website tham khảo:
    1. Thiết kế giao diện bootrap 5, Học lập trình tại: https://www.youtube.com/watch?v=N-x7aw-4phQ
    2. Tải bootrap 5.3.3: https://getbootstrap.com/docs/5.3/getting-started/download/
    3. Lấy icon: https://fontawesome.com/icons/facebook?f=brands&s=solid
    4. Lấy sliderold: https://owlcarousel2.github.io/OwlCarousel2/demos/responsive.html


# Thay đổi title, header trên trang admin
    1. Clip hướng dẫn: https://www.youtube.com/watch?v=CABh_KlGnrw

# Khai báo file templates
    sittings.py
        1. Thêm folder templates vào thư mục website gốc, cùng cấp với các app
        TEMPLATES = [
            { 
                'DIRS': [os.path.join(BASE_DIR, 'templates')],
            },]

# Khai báo static:
    sittings.py
        1. Thêm folder static (chép các folder css, js, img) vào thư mục website gốc, cùng cấp với các app
            STATIC_URL = '/static/'

            "STATICFILES_DIRS: Thư mục chứa file static."
            STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')]

            # Cấu hình cho Django Admin
                STATICFILES_DIRS += [
                    os.path.join(BASE_DIR, 'static_collected/admin'),
                ] #,Thay thế "static/admin" thành 'static_collected/admin' sau khi chạy lệnh static_collected

            Lưu ý: Nếu đã tạo và sử dụng admin thì thực hiện cấu hình thêm # Cấu hình cho Django Admin
        
        2. Khai báo file STATIC_ROOT: là đường dẫn tuyệt đối đến thư mục chứa tất cả file static được collect (gom lại)
           
            STATIC_ROOT = os.path.join(BASE_DIR, "static_collected")  # Thay đổi "static_collected" thành tên thư mục bạn muốn.
            
        3. --> Chạy python manage.py collectstatic, để gom các file static về STATIC_ROOT    

# Các mục chưa làm được:

    1. Lệnh xóa bộ nhớ cache (Chưa làm được bị lỗi)
        Cài đặt : pip install django-admin-commands
        python manage.py clear_cache

    2. Sắp xếp thứ tự trong trang admin (Chưa làm được)
        Tham khảo: https://djangosnippets.org/snippets/1939/#comments
    
    3. Dịch thuật và mutiplies language
        3.1 Hướng dẫn youtube: 
            Chuyển 2 ngôn ngữ: https://www.youtube.com/watch?v=z_p8WxFGV5A
            Cài đặt Django Rosetta Package, quản lý ngôn ngữ: https://www.youtube.com/watch?v=HU0rq917P58
        
        3.2 Phần cài đặt
            Cài đặt: gettext on Windows (https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#how-django-discovers-language-preference)

            Cài đặt gettext: https://mlocati.github.io/articles/gettext-iconv-windows.html
            
            https://docs.djangoproject.com/en/2.0/topics/i18n/translation/
        
        3.3 Phần tham khảo:
            https://github.com/PhungXuanAnh/django-multi-language-sample/blob/master/polls/models.py

            Hay mà chưa nguyên cứu: https://www.youtube.com/watch?v=WBKfNoxSzOg
            
            Chút xem: https://www.youtube.com/watch?v=PiTo1GbHt_I

# Cách đăng ký folder media chứa hình ảnh:
    1. settings.py
        # Tự tạo folder media và load hình ảnh khi lưu model 
        MADIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")  
    2. urls.py:
        2.1 Cách này đã khắc phục sửa lỗi:
            urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('cauhinhtrangchu.urls')),
            path('media/', serve, {'document_root': settings.MEDIA_ROOT}),]
        
        2.2 Cách này bị lỗi: "Not Found: /admin ; [25/Apr/2024 08:18:20] "GET /admin HTTP/1.1" 404 2584

            # Đăng ký đường dẫn cho media
            from django.conf import settings
            from django.conf.urls.static import static

            urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
    3. base.html
        Các biến chứa hình ảnh sau khi model thì khai báo file html là: {{congty.TenCongTy.url}}

    4. Chưa thử đoạn code này:
        urls.py
        
        from django.contrib import admin
        from django.urls import path, include
        from django.conf import settings
        from django.conf.urls.static import static
        from django.contrib.staticfiles.urls import staticfiles_urlpatterns

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('django_app.urls')),
        ]
        # Serving the media files in development mode
        <!-- if settings.DEBUG:
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        else:
            urlpatterns += staticfiles_urlpatterns() -->

# Code tự định nghĩa Form
    from django.contrib import admin
    from django import forms

    class NhanVienForm(forms.ModelForm):
        class Meta:
            model = NhanVien
            fields = '__all__'  # Hoặc liệt kê các trường cần hiển thị

        def __init__(self, *args, **kwargs):
            super(NhanVienForm, self).__init__(*args, **kwargs)
            # Lọc danh sách hiển thị theo logic (nếu cần)
            self.fields['MaCongTy'].queryset = CongTy.objects.all()
            self.fields['MaChiNhanh'].queryset = ChiNhanh.objects.filter(MaCongTy=self.initial['MaCongTy'])  # Lọc theo Công ty

        class NhanVienAdmin(admin.ModelAdmin):
            form = NhanVienForm

            # ... các thuộc tính khác ...

# Hiển thị bảng Quyền của người dùng với nút "Thêm" và "Xóa"
    
    1. Cài đặt package django-admin-ext:

        Package django-admin-ext cung cấp nhiều tính năng hữu ích cho trang quản trị Django, bao gồm khả năng hiển thị bảng quyền người dùng với các nút "Thêm" và "Xóa".

        Bash
        pip install django-admin-ext
    
    2. Thêm django-admin-ext vào INSTALLED_APPS:

        Mở file settings.py và thêm 'django_admin_ext' vào danh sách INSTALLED_APPS:

        Python
        INSTALLED_APPS = [
            # ... other apps ...
            'django_admin_ext',
            # ... other apps ...
        ]

        *** Lỗi: 
            ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
        *** Xử lý:
            Xác minh cài đặt Django: >>> pip freeze | grep django
# PostMan version: 10.24.16 (file):
    1. PostMan version: 10.24.16 (file)
        username: vunghixuan
        pw: @Vu05291922@
        email: dangdiepquan@gmail.com
        [GitHub](D:\ThanhVu\GIthub_VuNghiXuan\sofe)

# API Rest Framework đang sử dụng:    
    1. Tham khảo tìm hiểu PostMan của DuongHuuThanh: https://www.youtube.com/watch?v=7GycQ2V7VMM
    2. Api token auth User của SonNguyen: https://www.youtube.com/watch?v=yoOsUCeItMI&t=365s
    3. Nhà thuốc: https://www.youtube.com/watch?v=83NOTkDh9yg&list=PLb-NlfexLTk_lsm7qMjMamK51bTAbQ3mH&index=2

    4. Truy xuất data từ Serializes, Rest Framework
    app: I_thongtincongty

    PS D:\ThanhVu\GIthub_VuNghiXuan\kphtWebSite\kphtsite> python manage.py shell    
    Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from I_thongtincongty.serializers import *
    >>> from I_thongtincongty.models import *      
    >>> nv=NhanVien.objects.all()
    >>> NhanVienSerializer(nv, many=True).data #many=True: tập nhiều đối tượng
    [{'id': 1, 'ten_nhan_vien': 'abc', 'chi_nhanh': 1, 'nhiem_vu': [1]}, {'id': 2, 'ten_nhan_vien': 'xyz', 'chi_nhanh': 1, 'nhiem_vu': [1, 2]}]
    >>>

    Tham khảo hide 1 khóa học thay cho hide 1 sản phẩm tại bài 18: 
        https://www.youtube.com/watch?v=XzYFoMFOA3c&list=PLbiEmmDApLby83031AFtpTw2WUS9tvlEB&index=18

# django-oauth-toolkit với 'oauth2_provider', Phần này đang lỗi 
    Mai xem: 
        https://www.youtube.com/watch?v=rjiHHDvs8mE
        https://www.youtube.com/watch?v=5_hLC1QC_Vc
    
    1. Cài đặt: https://django-oauth-toolkit.readthedocs.io/en/latest/install.html
        pip install django-oauth-toolkit
    2. Chứng thực:
        https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html
            REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'oauth2_provider.contrib.rest_framework.OAuth2Authentication',)}

        Lỗi: "ModuleNotFoundError: No module named 'oauth2_provider'"
            https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
    3. Khai báo url:
        urlpatterns = [
            path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
            #re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
            ]
    4. python manage.py migrate oauth2_provider



# Tạo mutiplies menu, đệ quy
    https://www.youtube.com/watch?v=OL4nLE0GXfc&list=PLd9OKDFjBa8di0ViQ_bWWYVDBTrrZUZTn&index=15


# Thay đổi và hạn chế phân vùng cho nhân viên:
    Tham khảo phân quyền post bài 1 khu vực: 
    1. https://stackoverflow.com/questions/6103672/django-admin-form-how-to-change-select-options-dynamically
    
    2. https://www.youtube.com/watch?v=Zzd4sL7drKQ

    3. Quản lý bán hàng: 
        https://www.youtube.com/watch?v=PmuKoJ0hpUQ&list=PLInvlTu9nmo8ttdXgiD4S7sHiHL2iRVY5&index=4
        https://www.youtube.com/watch?v=W6Q4WFvcdOQ&list=PLInvlTu9nmo8ttdXgiD4S7sHiHL2iRVY5&index=21



# Mã tem hàng hóa:
    Tham khảo clip: https://www.youtube.com/watch?v=VDIJ4GgKxR8

    Code máy quét mã vạch: https://zzzcode.ai/answer-question?id=52fc517e-9e40-4acb-94a4-d246309e18f6


# Python anywhere: (https://vunghixuan.pythonanywhere.com/#)
    1. Chép và Khai báo thêm dự án django: https://www.youtube.com/watch?v=9BEKT0mEAso
        chép file: 
            Bash gaiỉ nén: unrar x duan.rar (hoặc unzip duan.zip)
    2. Tạo môi trường ảo: Bash>> mkvirtualenv venv
    3. Chuyển vào thư mục dự án: cd duan
    4. Liệt kê thư mục trong duan: ls
    5. Cài đặt thư viện: pip install -r requirements.txt
    3. Cấu hình url static cho PythonAnywhere:
        Trước khi deploy, hãy đảm bảo bạn đã chạy lệnh collectstatic trong môi trường Python của dự án Django trên PythonAnywhere. Lệnh này sẽ thu thập tất cả các tệp static từ các thư mục được chỉ định trong cài đặt STATICFILES_DIRS và đặt chúng vào thư mục static_collected.

        Sau khi deploy, truy cập trang web PythonAnywhere của bạn và điều hướng đến tab "Web".
        Trong phần "Static files", đảm bảo "Collect static files" được chọn và đường dẫn đến thư mục static_collected của bạn được đặt chính xác.

        >>Url:/static/   | Directory: 	/home/vunghixuan/duan/static_collected

    2. Hướng dẫn tạo cặp keys xác thực  cấu hình SSH với Key Pair RSA: https://www.youtube.com/watch?v=d4xhfzE01E4:
        >>ssh-keygen
        >>Enter passphrase (empty for no passphrase): kpht
        >>Enter same passphrase again: kpht
        xem và liệt kê: >>ls: Liệt kê các tệp và thư mục trong thư mục /home/vunghixuan/.ssh

        Đổi tên file vì server chỉ đọc file "authorized_keys": mv /home/vunghixuan/.ssh/id_rsa.pub /home/vunghixuan/.ssh/authorized_keys
        Your identification has been saved in /home/vunghixuan/.ssh/id_rsa
        Your public key has been saved in /home/vunghixuan/.ssh/id_rsa.pub

        Đọc và xem file: >>cat
        >>cat /home/vunghixuan/.ssh/id_rsa --> chép lưu file notepad private_key
        >>cat /home/vunghixuan/.ssh/authorized_keys --> chép lưu file notepad pup_key

        <!-- Cấu hình : không phải pass -->
        >>nano /etc/ssh/sshd_config  -> Tìm đến dòng #PubkeyAuthentication yes
        Khi sửa dòng này báo lỗi: [ Error writing /etc/ssh/sshd_config: Permission denied ]
        -->Tiếp tục sử dụng quyền root của SuperUser: sudo nano /etc/ssh/sshd_config

    https://www.youtube.com/watch?v=2zFbhj7Fykc

# Deloy web
    https://www.youtube.com/watch?v=5aEUOam1GTE

# Clip đang học
    1.Thanh Duong Huu: https://www.youtube.com/watch?v=DC0QEggBPF4&list=PLbiEmmDApLby83031AFtpTw2WUS9tvlEB&index=4
        1.1 Sử dụng lớp đối tượng chung "Class Meta" tham khảo, phút 11:  https://www.youtube.com/watch?v=zMiftBvejvs&list=PLbiEmmDApLby83031AFtpTw2WUS9tvlEB&index=5

        1.2 Truy vấn dữ liệu models trong django: https://www.youtube.com/watch?v=BWijXgFp_0Q&list=PLbiEmmDApLby83031AFtpTw2WUS9tvlEB&index=7
    
    
    Hay: https://www.youtube.com/watch?v=OTmQOjsl0eg
    
    # Note:
        Add img, 1giờ 40phút

# Các Api cần viết:
        Các API cần thiết cho trang web bán vàng trang sức
    Để xây dựng một trang web bán vàng trang sức hoàn chỉnh, bạn cần triển khai một số API quan trọng để quản lý các khía cạnh khác nhau của trang web. Dưới đây là danh sách các API chính:

    1. Quản lý sản phẩm:

    API lấy danh sách sản phẩm: Cho phép lấy danh sách tất cả các sản phẩm có sẵn, bao gồm thông tin chi tiết về sản phẩm như tên, giá cả, mô tả, hình ảnh, v.v.
    API lấy chi tiết sản phẩm: Cho phép lấy thông tin chi tiết về một sản phẩm cụ thể, bao gồm tất cả các thông tin được liệt kê ở trên và các thông tin bổ sung như chất liệu, trọng lượng, kích thước, v.v.
    API thêm sản phẩm mới: Cho phép thêm sản phẩm mới vào danh sách sản phẩm, bao gồm tất cả thông tin chi tiết cần thiết.
    API sửa đổi sản phẩm: Cho phép sửa đổi thông tin chi tiết của sản phẩm hiện có.
    API xóa sản phẩm: Cho phép xóa sản phẩm khỏi danh sách sản phẩm.
    2. Quản lý danh mục:

    API lấy danh sách danh mục: Cho phép lấy danh sách tất cả các danh mục sản phẩm, bao gồm tên danh mục và các sản phẩm thuộc danh mục đó.
    API thêm danh mục mới: Cho phép thêm danh mục sản phẩm mới, bao gồm tên danh mục và mô tả.
    API sửa đổi danh mục: Cho phép sửa đổi thông tin chi tiết của danh mục sản phẩm hiện có.
    API xóa danh mục: Cho phép xóa danh mục sản phẩm khỏi danh sách danh mục.
    3. Quản lý giỏ hàng:

    API thêm sản phẩm vào giỏ hàng: Cho phép thêm sản phẩm vào giỏ hàng của người dùng, bao gồm số lượng sản phẩm và các tùy chọn tùy chỉnh (nếu có).
    API lấy danh sách sản phẩm trong giỏ hàng: Cho phép lấy danh sách tất cả các sản phẩm trong giỏ hàng của người dùng, bao gồm số lượng, giá cả và tổng số tiền.
    API cập nhật số lượng sản phẩm trong giỏ hàng: Cho phép cập nhật số lượng sản phẩm trong giỏ hàng của người dùng.
    API xóa sản phẩm khỏi giỏ hàng: Cho phép xóa sản phẩm khỏi giỏ hàng của người dùng.
    4. Quản lý đơn hàng:

    API tạo đơn hàng mới: Cho phép tạo đơn hàng mới từ giỏ hàng của người dùng, bao gồm thông tin khách hàng, địa chỉ giao hàng, phương thức thanh toán, v.v.
    API lấy danh sách đơn hàng: Cho phép lấy danh sách tất cả các đơn hàng của người dùng, bao gồm trạng thái đơn hàng, chi tiết thanh toán, thông tin giao hàng, v.v.
    API lấy chi tiết đơn hàng: Cho phép lấy thông tin chi tiết về một đơn hàng cụ thể, bao gồm tất cả thông tin được liệt kê ở trên.
    API cập nhật trạng thái đơn hàng: Cho phép cập nhật trạng thái của đơn hàng (ví dụ: đang xử lý, đã giao hàng, đã hoàn thành, v.v.).
    5. Quản lý người dùng:

    API đăng ký người dùng mới: Cho phép người dùng mới đăng ký tài khoản trên trang web.
    API đăng nhập người dùng: Cho phép người dùng đăng nhập vào tài khoản hiện có.
    API lấy thông tin người dùng: Cho phép lấy thông tin chi tiết về tài khoản người dùng hiện tại.
    API cập nhật thông tin người dùng: Cho phép cập nhật thông tin chi tiết của tài khoản người dùng hiện tại.
    6. Quản lý thanh toán:

    API xử lý thanh toán: Cho phép xử lý thanh toán cho đơn hàng bằng cách tích hợp với các cổng thanh toán trực tuyến (ví dụ: PayPal, Stripe, v.v.).
    7. API quản trị:

    API quản lý người dùng: Cho phép quản trị viên quản lý tài khoản người dùng, bao gồm thêm, sửa đổi, xóa và đặt quyền.
    API quản lý sản phẩm: Cho phép quản trị viên quản lý sản phẩm, bao gồm thêm, sửa đổi, xóa và phân loại sản phẩm.
    API quản lý đơn hàng: Cho phép quản trị viên quản lý đơn hàng, bao gồm xem chi tiết đơn hàng, cập nhật trạng thái đơn hàng và xử lý khiếu nại.

# QRcode :
    https://www.youtube.com/watch?v=xk8K3MNu81I
    (trong đó có phần lấy html mẫu django)

    qrcode_django: https://www.youtube.com/watch?v=aYCmPFGi-Jo
    -->ảnh code: [D:\barcode_django]
# Nguyên cứu cách đặt camare lên website
    https://www.youtube.com/watch?v=xz9MvyKGYio

# Nguyên cứu Docker:
    https://www.youtube.com/watch?v=Gh1Sgknc6Fg&list=RDCMUC66_4puPl1OFS3YAeZ7tRdw&index=3

# Cloud data Railway add PostgreSQL
    Tên tài khoản: vunghixuan.info@gmail.com
    pw: giống mail

    Cài đặt:
    pip install psycopg2: Trình điều khiển PostgreSQL, Python 2.6-3.10 và Python 3.3+.
    pip freeze > requirments.txt : Đóng gói các thư viện trong môi trường tạo ra file requirments.txt
    https://railway ->chọn new project-> cài PostgreSQL
    Vào PostgreSQL: chọn Variables. Lấy các name, host, post, pw cho vào file sittings.py 
    https://railway.app/project/96757859-9ada-418c-9753-9b6cc5dade70/service/98f0b728-6183-4c5b-ba6b-2b8625f2d4ac/data?state=table&table=auth_user


    pip install python-dotenv: tách các biến môi trường khỏi mã nguồn của ứng dụng, giúp dễ dàng quản lý và bảo mật hơn
    file sittings.py thêm: from dotenv import load_dotenv
    Tạo ra 2 file: .env và .gitignore lấy pw, host, name database

    Chạy lại migrate và tạo : python manage.py createsuperuser

# Push App to Web Hosting
    pip install whitenoise: Whitenoise phục vụ các tập tin tĩnh (static files) một cách hiệu quả
    pip install gunicorn : Xử lý nhiều yêu cầu đồng thời một cách hiệu quả, sử dụng ít tài nguyên CPU và bộ nhớ

    Khai báo sittings.py:
        MIDDLEWARE = [
            # ... các middleware khác ...
            'whitenoise.middleware.WhiteNoiseMiddleware',]
    INSTALLED_APPS = [
                # ... các apps khác ...
                'whitenoise.runserver_nostatic',    ]
    
    - Tạo file procfile với :"web: gunicorn PROJECTNAME.wsgi": khởi tạo các tiến trình các app chạy riêng biệt, giúp tối ưu hóa (https://gemini.google.com/app/1f0b9b2cf2469c53)

    -Tạo file: runtime.txt 
    Chạy python -V : lấy version python 3.11.9

    Tạo ra folder .ssh với git: trong "ADMIN@DesktopHome_MrVu MINGW64 ~/.ssh"
    ssh-keygen.exe 
        - Lưu nó đúng chỗ tạo ra nên Enter: "Enter file in which to save the key (/c/Users/ADMIN/.ssh/id_rsa):"
    
    -Tạo thư mục để "test_ssh" và khởi tạo : .git
        + git config --global user.name "vunghixuan" : Giải thích: https://gemini.google.com/app/1f0b9b2cf2469c53

        + git config --global user.email "vunghixuan.info.gmail.com"

        + git config --global push.default matching

        + git config --global alias.co checkout : Dự án luôn có lệnh để nhấp chuột khi dán

        +  git init

        + git add .
        + git commit -am 'initial web'

        --> Vào github tạo ra dự án cùng tên với "test_ssh"
        --> lấy 2 câu lệnh :
            + git remote add origin https://github.com/VuNghiXuan/test_ssh.git
            + git branch -M main : Chuyển nhánh
            + git push -u origin main



