from django.shortcuts import render, redirect
from VIIgiohang.cart import Cart
from VIIItratien.forms import ShippingForm, ShippingAddress, PaymentForm
from VIIItratien.models import ShippingAddress, Order, ItemOrder
from django.contrib.auth.models import User
from django.contrib import messages
from IIIquanlykho.models import NhapHang



# Xử lý đơn hàng
def process_order(request):
    if request.POST:
        # Get from cart
        cart = Cart(request)
        cart_san_pham = cart.get_prods()
        so_luong = cart.get_quants()
        tong_gia_tri = cart.total()

        # Get Billing info from the last page 
        payment_form = PaymentForm(request.POST or None)
        # Get shipping Session data from def billing info
        my_shipping = request.session.get('my_shipping')
        
        # print('---------------------------my_shipping', my_shipping)
        # Gather Order Info
        full_name = my_shipping['shipping_full_name']
        # email = 

        # Create Shipping Address from session info    
        shipping_address = f"{my_shipping['shipping_address']}\n{my_shipping['shipping_phone']}\n{my_shipping['shipping_id_card']}\n"
       
        amount_paid = tong_gia_tri
        # date_order = 

        # Create a Order
        if request.user.is_authenticated:
            # logged in 
            # 1.Create a Order
            user = request.user
            create_order = Order(user = user, full_name=full_name, shipping_address=shipping_address, amount_paid= amount_paid)
            create_order.save()

            # 2.Add order item
            # Get order id
            order_id = create_order.pk

            # Get product id
            for prod in cart_san_pham:
                product_id = prod.id
                # Get product info
                price = prod.gia_ban_mon
                # if prod.ton_kho:
                #     price = prod.gia_ban_mon
                # else: 
                #     price = 0

                # Get quantity
                
                for key, val in so_luong.items():
                    if int(key) == product_id:
                        if prod.ton_kho:
                            sl = val
                        else:
                            sl = 0

                        # Create a order item
                        create_order_item = ItemOrder(order_id =  order_id, product_id = product_id, user = user, quantity = sl, price= price)
                        create_order_item.save()
           




            messages.success(request, "Đặt hàng thành công. Quý khách vui lòng để ý điện thoại trong thời gian nhận hàng ...")
            return redirect('index')
    

        else:
            # Not logged in
            # 1. Create a Order
            create_order = Order(full_name=full_name, shipping_address=shipping_address,  amount_paid= amount_paid)
            create_order.save()
            
            # 2.Add order item
            # Get order id
            order_id = create_order.pk

            # Get product id
            for prod in cart_san_pham:
                product_id = prod.id
                # Get product info
                price = prod.gia_ban_mon
                # if prod.ton_kho:
                #     price = prod.gia_ban_mon
                # else: 
                #     price = 0

                # Get quantity
                
                for key, val in so_luong.items():
                    if int(key) == product_id:
                        if prod.ton_kho:
                            sl = val
                        else:
                            sl = 0

                        # Create a order item
                        create_order_item = ItemOrder(order_id =  order_id, product_id = product_id, quantity = sl, price= price)
                        create_order_item.save()



            messages.success(request, "Đặt hàng thành công. Quý khách vui lòng để ý điện thoại trong thời gian nhận hàng ...")
            return redirect('index')
        
    
    else:
        messages.success(request, "Quyền truy cập bị từ chối")
        return redirect('index')
    
    # return render(request, 'process_order.html',{})

# Thông tin thanh toán
def billing_info(request):
    if request.POST:
        # Get from cart
        cart = Cart(request)
        cart_san_pham = cart.get_prods()
        so_luong = cart.get_quants()
        tong_gia_tri = cart.total()

        # Create a session with Shipping info to def process_order
        my_shipping = request.POST
        # print('-------------------my_shipping from request.POST', my_shipping)

        request.session['my_shipping'] = my_shipping
        # print('-------------------my_shipping in billing_info', my_shipping)


        # Check to see user is loging
        if request.user.is_authenticated:
            # Get the billing Form
            billing_form = PaymentForm()
            return render(request, 'billing_info.html', {'cart_san_pham':cart_san_pham,
                                                'so_luong':so_luong,
                                                'tong_gia_tri':tong_gia_tri, 
                                                'shipping_info':request.POST,
                                                'billing_form' :billing_form})
        else:
            # Get the billing Form
            billing_form = PaymentForm()
            return render(request, 'billing_info.html', {'cart_san_pham':cart_san_pham,
                                                'so_luong':so_luong,
                                                'tong_gia_tri':tong_gia_tri, 
                                                'shipping_info':request.POST,
                                                'billing_form' :billing_form})

        # # Get user shipping
        # shipping_form = request.POST
        # return render(request, 'billing_info.html', {'cart_san_pham':cart_san_pham,
        #                                         'so_luong':so_luong,
        #                                         'tong_gia_tri':tong_gia_tri, 
        #                                         'shipping_form':shipping_form})
    else:
        messages.success(request, "Quyền truy cập bị từ chối")
        return redirect('index')

# Create your views here.
def check_out(request):
    # Get from cart
    cart = Cart(request)
    cart_san_pham = cart.get_prods()
    so_luong = cart.get_quants()
    tong_gia_tri = cart.total()

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
        # # Check out guest
        # return render(request, 'check_out.html', {'cart_san_pham':cart_san_pham,
        #                                         'so_luong':so_luong,
        #                                         'tong_gia_tri':tong_gia_tri,
        #                                         'shipping_form':shipping_form})
        # return redirect('register')
        # return render(request, 'update_user.html')

              

        # Get user shipping
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'check_out.html', {'cart_san_pham':cart_san_pham,
                                                'so_luong':so_luong,
                                                'tong_gia_tri':tong_gia_tri,
                                                'shipping_form':shipping_form})
    
                      
def payment_success(request):
    return render(request, 'payment_success.html', {})

