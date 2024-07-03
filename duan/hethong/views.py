from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, ChangePassWordForm, UserInfoForm
from django.core.files.storage import default_storage # Lấy avatar

from .models import UserProfile

from django.contrib import messages
import json
from VIIgiohang.cart import Cart

# Kết nối trả tiền mua hàng
from VIIItratien.forms import ShippingForm
from VIIItratien.models import ShippingAddress
# from .get_user_permissions import get_permissions


# Create your views here.

# Đăng nhập Khách
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        checked = request.POST.get('exampleCheck1', False)  # Get checkbox value (defaults to False)

        user = authenticate(request, username=username, password=password)
        # print('---------- checked:', checked)
        if user is not None and checked:  # Successful authentication and checkbox checked
            login(request, user)

            # Do some cart stuff
            current_user = UserProfile.objects.get(user__id=request.user.id)
            # get their cart from database
            save_cart = current_user.old_cart
            # Covert database string to python dictionary
            if save_cart:
                # Cover to dictionary using Json
                # {'4':2}
                coverted_cart = json.loads(save_cart)
                # Add the loaded cart dictionary to out session
                # Get the cart
                cart = Cart(request)
                # Loop thru the cart and add the items from database
                for key, val in coverted_cart.items():
                    cart.db_add(san_pham=key, so_luong=val)

            messages.success(request, (f'Đăng nhập thành công. Rất vui được phục vụ Quý khách!!!'))
            
            return redirect('index')
        else:
            if not username or not password:  # Missing username or password
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không hợp lệ.')
            elif not user:  # Incorrect username or password (authentication failed)
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại.')
            else:  # Checkbox not checked but authentication succeeded (unlikely scenario)
                messages.error(request, 'Vui lòng chọn "Tôi không phải là Robot" để tiếp tục.')
            return redirect('login')
    else:
        return render(request, 'login.html')



# Thoát đăng nhập Khách
def logout_user(request):
    logout(request)
    messages.success(request, ('Đã đăng xuất thành công. Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi. Trân trọng !!!'))
    return redirect('index')

# Trang đăng ký
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # login user
            user = authenticate(username = username, password = password)
            login (request, user)
            messages.success(request, "Đăng ký thành công!")
            return redirect('index')
        else:
            # messages.success(request, "Có lỗi đăng ký. Vui lòng nhập lại thông tin")
            # return redirect('register')
            
            # Display specific error messages for each form field
            for field, errors in form.errors.items():
                for err in errors:
                    messages.error(request, f"Lỗi ở trường '{field}': {err}")  # Customize message format if needed
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {'form':form})
    

# Trang update_user
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance = current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Cập nhật thay đổi thành công ...")
            return redirect('index')
        return render(request, 'update_user.html', {'user_form':user_form})
    else:
        messages.success(request, "Có lỗi đăng ký. Vui lòng nhập lại thông tin")
            # return redirect('register')
            
        # Display specific error messages for each form field
        for field, errors in user_form.errors.items():
            for err in errors:
                messages.error(request, f"Lỗi ở trường '{field}': {err}")  # Customize message format if needed
        return render(request, 'register.html', {'user_form': user_form})

# Trang update_password
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            password_form = ChangePassWordForm(current_user, request.POST)
            if password_form.is_valid():
                password_form.save()
                messages.success(request, "Thay đổi mật khẩu thành công !!!")
                login(request, current_user)
                return redirect('index')
                # return redirect('update_user')
            else:
                # Display specific error messages for each form field
                for field, errors in password_form.errors.items():
                    for err in errors:
                        messages.error(request, f"Lỗi ở trường '{field}': {err}")  # Customize message format if needed
                return render(request, 'update_password.html', {'password_form': password_form})
        else:
            
        
            password_form = ChangePassWordForm(current_user)
            return render(request, 'update_password.html', {'password_form': password_form})
    else:
        messages.success(request, "Bạn cần phải thực hiện đăng nhập")
        return redirect('index')



# Update infor for User
def update_info(request):
    if request.user.is_authenticated:
        # Get current user
        current_user = UserProfile.objects.get(user__id = request.user.id)
        # Get current shipping_user
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        # Get original User Form 
        info_form = UserInfoForm(request.POST or None, instance = current_user)#

        # Get user shipping
        shipping_form = ShippingForm(request.POST or None, instance = shipping_user)


        if info_form.is_valid() or shipping_form.is_valid():
            avatar = request.FILES.get('avatar')
            # print('---------------------------- avatar', avatar)
            if avatar:
                from datetime import datetime

                current_year = datetime.now().year
                current_month = datetime.now().month
                # Format the month as a two-digit string using f-strings
                current_month = f"{current_month:02d}"

                upload_path = f"users/{current_year}/{current_month}"
                avatar_path = default_storage.save(f"{upload_path}/{avatar.name}", avatar)

                current_user.avatar = avatar_path

            # Save original form
            info_form.save()
            # Save shipping form
            shipping_form.save()

            # login(request, current_user)
            messages.success(request, "Cập nhật thông tin cá nhân thành công ...")


            # print('------------------info_form.current_user',  current_user.avatar)
            # print('------------------info_form.current_user',  current_user.phone)


            return redirect('index')
        return render(request, 'update_info.html', {'info_form':info_form, 'shipping_form': shipping_form})
    else:
        messages.success(request, "Có lỗi xảy ra. Vui lòng nhập lại thông tin")
            # return redirect('register')
            
        # Display specific error messages for each form field
        for field, errors in info_form.errors.items():
            for err in errors:
                messages.error(request, f"Lỗi ở trường '{field}': {err}")  # Customize message format if needed
        return render(request, 'update_info.html', {'info_form': info_form})
    
def get_user_permissions(request):
    user = User.objects.get(pk=request.user.id)
    user_permissions = user.get_all_permissions()  # This includes both app-level and object-level permissions
    # print ('hethong\get_user_permissions.py', user_permissions)
    return user_permissions

def user_permissions(request):
    # user_permissions = get_user_permissions(request)
    
    # print ('hethong\get_user_permissions.py', user_permissions)
    return render(request, 'user_permissions.html', {})
    