from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from django.apps import apps 
from .class_user_info import UserInfo

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from .forms import SignUpForm, UpdateUserForm, ChangePassWordForm

# from django.contrib import messages

from Ithongtincongty.models import CongTy
from IIIquanlykho.models import BoSuuTap, ChiNhanh, NhapHang
from .models import BoSuuTap
from hethong.models import UserProfile
from django.db.models import Q


def get_all_company_data():
    """
    Lấy tất cả thông tin công ty trong một truy vấn cơ sở dữ liệu duy nhất.
    Xử lý trường hợp không có công ty nào đang hoạt động.
    """
    context = {}
    active_companies = CongTy.objects.filter(kich_hoat=True)
    # kich_hoat
    if not active_companies.exists():
        return None  # Xử lý trường hợp không có công ty nào đang hoạt động

    context = {
        "congty": active_companies.first(),
        "chinhanh": ChiNhanh.objects.filter(kich_hoat=True),
        "bo_suu_tap": BoSuuTap.objects.filter(kich_hoat=True),
    }
    return context


def get_filtered_products(bo_suu_tap):
    return NhapHang.objects.filter(bo_suu_tap__in=bo_suu_tap)#, bo_suu_tap__kick_hoat=True

# Lấy sp trong 1 sưu tập
def get_products_in_collection(bo_suu_tap):
    """
    Retrieves all products belonging to a specific collection.

    Args:
        bo_suu_tap (BoSuuTap object): The collection object.

    Returns:
        QuerySet: A queryset containing the filtered products.
    """
    return NhapHang.objects.filter(bo_suu_tap=bo_suu_tap)


def get_app_verbose_names():
    app_verbose_names = {}
    for app in apps.get_app_configs():
        # Kiểm tra xem ứng dụng có thuộc tính `verbose_name` hay không
        if hasattr(app, 'verbose_name'):
            app_verbose_names[app.label] = app.verbose_name
    return app_verbose_names

def get_user_apps(user_permissions):
    user_app = {}
    app_verbose_names = get_app_verbose_names()

    for permission in user_permissions:
        app_label, permission_name = permission.split('.')

        if app_label not in user_app:
            user_app[app_label] = app_verbose_names.get(app_label, app_label)  # Sử dụng .get() để tránh lỗi khi không tìm thấy app_label

    return user_app


# Get my_context_processor for all pages
def my_context_processor(request): #, san_pham_id   
    # context = {}
        
    # san_pham = get_object_or_404(NhapHang, pk=san_pham_id)
    context = get_all_company_data()
    if context:
        san_pham = get_filtered_products(context['bo_suu_tap'])
        context.update({'san_pham': san_pham}) #'company_info':company_info
    # print(context)

    # Lấy avatar
    if request.user.is_authenticated:
        current_user = UserProfile.objects.get(user=request.user)
        context.update ({'current_user': current_user})
        
        # Lấy user_groups, permissions
        user_groups = request.user.groups.all()
        user_group = []
        for gr in user_groups:
            user_group.append(gr.name)
        # print ('-------------------------------------------- user_group', user_group)
        
        # Lấy user_permissions
        user_permissions = request.user.get_all_permissions()
        
        context.update ({'user_permissions': user_permissions,
                        'user_group': user_group})
        
        # Get get_user_apps
        user_apps = get_user_apps(user_permissions)    
        

        # get_permission_verbose_names
        user_info = UserInfo(user_permissions, user_apps)
        user_apps = user_info.get_app()
        # print ('-------------------------------------------- user_apps', user_apps)
        context.update(user_apps)
        # context.update ({'user_apps': user_apps})
        
        # user_permissions = ['app_label.permission_name']
        # print ('-------------------------------------------- user_permissions', user_permissions)
        # app_verbose_name = {'app_label': 'app_verbose_name'}
        user_permissions_verbose_names = user_info.get_user_permissions_verbose_names()
        context.update(user_permissions_verbose_names)
        # print ('-------------------------------------------- context', context)
        # print ('-------------------------------------------- user_permissions_verbose_names', user_permissions_verbose_names)
        
    return context

# Trang chủ
def index(request): 
    return render(request, 'index.html', {})
   

# Trang show tất cả sản phẩm trong 1 bộ sưu tập
def all_products_in_collection(request, bo_suu_tap_id):
    bo_suu_tap = get_object_or_404(BoSuuTap, pk=bo_suu_tap_id)
    san_pham = get_products_in_collection(bo_suu_tap)
    context = {'bo_suu_tap_duoc_chon': bo_suu_tap, 'san_pham_trong_bo': san_pham}
    return render(request, 'all_products_in_collection.html', context)

# Trang xem chi tiết 1 sản phẩm
def product_detail(request, san_pham_id):
    san_pham = get_object_or_404(NhapHang, pk=san_pham_id)
    context = {'san_pham': san_pham}
    return render(request, 'product_detail.html', context)

# Trang thông tin về Công ty
def infor_company(request):
    return render(request, 'infor_company.html')

def search_products(request):
    if request.method == "POST":
        key_word = request.POST['searched'].lower()  # Get keyword from searched field in navbar.html
        searched = NhapHang.objects.filter(
            Q(ten_san_pham__icontains=key_word) | Q(mo_ta__icontains=key_word) | Q(ma_san_pham__icontains=key_word)
        )
        # Q cho phép kết hợp nhiều biểu thức bộ lọc 

        return render(request, 'search_products.html', {"key_word": key_word, "searched": searched})
    else:
        return render(request, 'search_products.html', {})


# # Đăng nhập Khách
# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         checked = request.POST.get('exampleCheck1', False)  # Get checkbox value (defaults to False)

#         user = authenticate(request, username=username, password=password)
#         # print('---------- checked:', checked)
#         if user is not None and checked:  # Successful authentication and checkbox checked
#             login(request, user)
#             messages.success(request, (f'Đăng nhập thành công. Rất vui được phục vụ Quý khách!!!'))
#             return redirect('index')
#         else:
#             if not username or not password:  # Missing username or password
#                 messages.error(request, 'Tên đăng nhập hoặc mật khẩu không hợp lệ.')
#             elif not user:  # Incorrect username or password (authentication failed)
#                 messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại.')
#             else:  # Checkbox not checked but authentication succeeded (unlikely scenario)
#                 messages.error(request, 'Vui lòng chọn "Tôi không phải là Robot" để tiếp tục.')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')



# # Thoát đăng nhập Khách
# def logout_user(request):
#     logout(request)
#     messages.success(request, ('Đã đăng xuất thành công. Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi. Trân trọng !!!'))
#     return redirect('index')

# # Trang đăng ký
# def register_user(request):
#     form = SignUpForm()
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']

#             # login user
#             user = authenticate(username = username, password = password)
#             login (request, user)
#             messages.success(request, "Đăng ký thành công!")
#             return redirect('index')
#         else:
#             # messages.success(request, "Có lỗi đăng ký. Vui lòng nhập lại thông tin")
#             # return redirect('register')
            
#             # Display specific error messages for each form field
#             for field, errors in form.errors.items():
#                 for err in errors:
#                     messages.error(request, f"Lỗi ở trường '{field}': {err}")  # Customize message format if needed
#             return render(request, 'register.html', {'form': form})
#     else:
#         return render(request, 'register.html', {'form':form})
    

# # Trang update_user
# def update_user(request):
#     if request.user.is_authenticated:
#         current_user = User.objects.get(id = request.user.id)
#         user_form = UpdateUserForm(request.POST or None, instance = current_user)

#         if user_form.is_valid():
#             user_form.save()
#             login(request, current_user)
#             messages.success(request, "Cập nhật thay đổi thành công ...")
#             return redirect('index')
#         return render(request, 'update_user.html', {'user_form':user_form})
#     else:
#         messages.success(request, "Có lỗi đăng ký. Vui lòng nhập lại thông tin")
#             # return redirect('register')
            
#         # Display specific error messages for each form field
#         for field, errors in user_form.errors.items():
#             for err in errors:
#                 messages.error(request, f"Lỗi ở trường '{field}': {err}")  # Customize message format if needed
#         return render(request, 'update_user.html', {'user_form': user_form})

# # Trang update_password
# def update_password(request):
#     if request.user.is_authenticated:
#         current_user = request.user
#         if request.method == 'POST':
#             password_form = ChangePassWordForm(current_user, request.POST)
#             if password_form.is_valid():
#                 password_form.save()
#                 messages.success(request, "Thay đổi mật khẩu thành công !!!")
#                 login(request, current_user)
#                 return redirect('index')
#                 # return redirect('update_user')
#             else:
#                 # Display specific error messages for each form field
#                 for field, errors in password_form.errors.items():
#                     for err in errors:
#                         messages.error(request, f"Lỗi ở trường '{field}': {err}")  # Customize message format if needed
#                 return render(request, 'update_password.html', {'password_form': password_form})
#         else:
            
        
#             password_form = ChangePassWordForm(current_user)
#             return render(request, 'update_password.html', {'password_form': password_form})
#     else:
#         messages.success(request, "Bạn cần phải thực hiện đăng nhập")
#         return redirect('index')