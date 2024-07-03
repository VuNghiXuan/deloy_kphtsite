from django.shortcuts import render, redirect, get_object_or_404
from VIIgiohang.cart import Cart
from VIIItratien.forms import ShippingForm, PaymentForm
from VIIItratien.models import ShippingAddress, Order, ItemOrder
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
from hethong.models import UserProfile
# from IIIquanlykho.models import NhapHang

# OrderItem
def order_detail(request, order_id):
    if request.user.is_authenticated:
        # order = get_object_or_404(Order, pk=order_id)  # Retrieve the order object by ID
        order = Order.objects.get(id = order_id)
        items = ItemOrder.objects.filter(order = order_id)

        # Change status shipping
        if request.POST:            
            status = request.POST['shipping_status']

            # Check if true or false
            if status == "true": # Xác nhận đã vận chuyển hàng
                # print('-----------------------------status == "true"')
                # Update the status
                now = datetime.datetime.now()
                order.shipped = True
                order.date_shipped = now
                order.save()
                messages.success(request, "Trạng thái vận chyển đã được cập nhật...")
                return redirect('index')
        
            else:
                if request.user.is_superuser: # Chỉ có quyền admin mới dc sửa
                
                    # Update the status: Xác định lại do nhầm lẫn 
                    order.shipped = False
                    order.save()
                    messages.success(request, "Trạng thái vận chyển đã được cập nhật...")
                    return redirect('index')
                else: 
                    messages.success(request, "Bạn không có quyền 'Admin' để thay đổi nội dung này ...")
                    # return redirect('order_detail')
            

        # print ('----------------------------------items', items)
        return render(request, 'order_detail.html', {'order': order, 'items':items})  # Render the detail template
    

# Phần xử lý dash
def not_shipping_dash(request): #and request.is_supperuser
    if request.user.is_authenticated:    
        orders = Order.objects.filter(shipped=False)
        # Change status shipping
        if request.POST:            
            # status = request.POST['shipping_status']
            # num = request.POST['num']
            status = request.POST.get('shipping_status')
            num = request.POST.get('num')
                      
            order = orders.get(id=num)
            # print('--------------------------------order', order)
            now = datetime.datetime.now()
            order.shipped = True
            order.date_shipped = now
            order.save()
            messages.success(request, "Trạng thái vận chyển đã được cập nhật...")
            return redirect('index')
        
           
                
        return render(request, 'not_shipping_dash.html',{'orders':orders})
    # else:
    #     messages.success(request, "Quyền truy cập bị từ chối")
    #     return redirect('index')
    

def shipping_dash(request):#and request.user.has_perm('app.change_order')
    if request.user.is_authenticated:    
        orders = Order.objects.filter(shipped=True)

        if request.POST:            
            # status = request.POST['shipping_status']
            # num = request.POST['num']
            status = request.POST.get('shipping_status')
            num = request.POST.get('num')
            # print('--------------------------------status num', status, num)
            if request.user.is_superuser: # Chỉ có quyền admin mới dc sửa
                order = orders.get(id=num)
                # print('--------------------------------order', order)
            
                # Update the status: Xác định lại do nhầm lẫn 
                order.shipped = False
                order.save()
                messages.success(request, "Trạng thái vận chyển đã được cập nhật...")
                return redirect('index')
            else: 
                messages.success(request, "Bạn không có quyền 'Admin' để thay đổi nội dung này ...")
                # pass
                # return redirect('order_detail')
        


        return render(request, 'shipping_dash.html',{'orders':orders})
    # else:
    #     messages.success(request, "Quyền truy cập bị từ chối")
    #     return redirect('index')
    
# Phần xử lý giỏ hàng
def get_cart_details(request):
    cart = Cart(request)
    cart_san_pham = cart.get_prods()
    so_luong = cart.get_quants()
    tong_gia_tri = cart.total()
    return cart_san_pham, so_luong, tong_gia_tri


def create_order_and_items(request, full_name, shipping_address, amount_paid, user=None):
    order = Order.objects.create(
        full_name=full_name,
        shipping_address=shipping_address,
        amount_paid=amount_paid,
        user=user,
    )
    order_id = order.pk

    # print('----------------------------get_cart_details(request)', get_cart_details(request))
    for prod in get_cart_details(request)[0]:
        product_id = prod.id
        price = prod.gia_ban_mon
        for key, val in get_cart_details(request)[1].items():
            if int(key) == product_id:
                if prod.ton_kho:
                    sl = val
                else:
                    sl = 0

        # sl = so_luong.get(str(product_id), 0)  # Handle missing keys in so_luong
        ItemOrder.objects.create(
            order_id=order_id,
            product_id=product_id,
            user=user,
            quantity=sl,
            price=price,
        )

def delete_products_in_cart(request):
    list_sessions = list(request.session.keys())
    # print("---------------------------list_sessions",list_sessions)
    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
            # print("---------------------------list_sessions",list_sessions)
            break

# del cart from database
def delete_cart_from_database(request):
    current_user = UserProfile.objects.filter(user__id=request.user.id)
    # Delete old_cart     
    current_user.update(old_cart = '')
    
    # print('---------------------------current_user.old_cart', current_user.old_cart)

# Get infor shipped of customer
def get_shipping_address_from_order(request, payment_form, my_shipping):
    shipping_address = []
    # Địa chỉ nhận hàng
    addr = my_shipping['shipping_address']
    if addr:
        addr = f'Địa chỉ nhận hàng: {addr}'
        shipping_address.append(addr)
    
    # Điện thoại
    phone = my_shipping['shipping_phone']
    if phone:
        phone = f'Điện thoại: {phone}'
        shipping_address.append(phone)
    
    # Căn cước
    id_card = my_shipping['shipping_id_card']
    if id_card:
        id_card = f'Số CCCD: {id_card}'
        shipping_address.append(id_card)
    
    
    # Tên chủ tài khoản
    card_name = request.POST.get('card_name')
    if card_name:
        card_name = f'Tên chủ tài khoản: {card_name}'
        shipping_address.append('-------** Thông tin dành cho khách hàng chuyển khoản **-------')
        shipping_address.append(card_name)
    
    # Số tài khoản
    bank_account = request.POST.get('bank_account')
    if bank_account:
        bank_account = f'Số tài khoản: {bank_account}'
        shipping_address.append(bank_account)

    # Tên ngân hàng
    bank_name = request.POST.get('bank_name')
    if bank_name:
        bank_name = f'Tên ngân hàng: {bank_name}'
        shipping_address.append(bank_name)
    
    # Tên ngân hàng
    contents = request.POST.get('contents')
    if contents:
        contents = f'Nội dung: {contents}'
        shipping_address.append(contents)


    
    shipping_address = '\n'.join(shipping_address)

    # print('----------------------------------shipping_address', shipping_address)

    # print('----------------------------------payment_form', payment_form['card_name'], 
    #                                                             payment_form['bank_account'],
    #                                                             payment_form['bank_name'] )
    # shipping_address = f"{my_shipping['shipping_address']}\n{my_shipping['shipping_phone']}\n{my_shipping['shipping_id_card']}\n"
    return shipping_address

def process_order(request):
    if request.POST:
        # Get from cart
        cart_san_pham, so_luong, tong_gia_tri = get_cart_details(request)

        # Get billing info from the last page
        payment_form = PaymentForm(request.POST or None)
        

        # Get shipping Session data from def billing info
        my_shipping = request.session.get('my_shipping')
        
        

        # Gather Order Info
        full_name = my_shipping['shipping_full_name']
        # shipping_address = f"{my_shipping['shipping_address']}\n{my_shipping['shipping_phone']}\n{my_shipping['shipping_id_card']}\n"
        shipping_address = get_shipping_address_from_order(request, payment_form, my_shipping)
        amount_paid = tong_gia_tri

        # Create Order
        create_order_and_items(request, full_name, shipping_address, amount_paid, request.user if request.user.is_authenticated else None)

       
        # Delete cart
        delete_products_in_cart(request)
        # Delete cart from database
        delete_cart_from_database(request)

        messages.success(request, "Đặt hàng thành công. Quý khách vui lòng để ý điện thoại trong thời gian nhận hàng ...")
        return redirect('index')

    else:
        messages.success(request, "Quyền truy cập bị từ chối")
        return redirect('index')


def billing_info(request):
    if request.POST:
        # Get from cart
        cart_san_pham, so_luong, tong_gia_tri = get_cart_details(request)

        # Create a session with Shipping info to def process_order
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping

        # Check to see user is loging
        if request.user.is_authenticated:
            billing_form = PaymentForm()
            return render(request, 'billing_info.html', {
                'cart_san_pham': cart_san_pham,
                'so_luong': so_luong,
                'tong_gia_tri': tong_gia_tri,
                'shipping_info': request.POST,
                'billing_form': billing_form,
            })
        else:
            billing_form = PaymentForm()
            return render(request, 'billing_info.html', {
                'cart_san_pham': cart_san_pham,
                'so_luong': so_luong,
                'tong_gia_tri': tong_gia_tri,
                'shipping_info': request.POST,
                'billing_form': billing_form,
            })

    else:
        messages.success(request, "Quyền truy cập bị từ chối")
        return redirect('index')


def check_out(request):
    # Get from cart
    cart_san_pham, so_luong, tong_gia_tri = get_cart_details(request)
    # Check shipping
    if request.user.is_authenticated:
        # Checkout login
        
        # Get current shipping_user
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)        

        # Get user shipping
        shipping_form = ShippingForm(request.POST or None, instance = shipping_user)
        
        return render(request, 'check_out.html', {'cart_san_pham':cart_san_pham,
                                                'so_luong':so_luong,
                                                'tong_gia_tri':tong_gia_tri, 
                                                'shipping_form':shipping_form})
    else:       

        # Get user shipping
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'check_out.html', {'cart_san_pham':cart_san_pham,
                                                'so_luong':so_luong,
                                                'tong_gia_tri':tong_gia_tri,
                                                'shipping_form':shipping_form})
    


    #

def payment_success(request):
    return render(request, 'payment_success.html', {})
