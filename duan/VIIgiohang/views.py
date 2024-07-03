from django.shortcuts import render, get_object_or_404, HttpResponse
from .cart import Cart
from IIIquanlykho.models import NhapHang
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def cart_sumary(request):
    # Get from cart
    cart = Cart(request)
    cart_san_pham = cart.get_prods()
    so_luong = cart.get_quants()
    tong_gia_tri = cart.total()
    return render(request, 'cart_sumary.html', {'cart_san_pham':cart_san_pham,
                                                'so_luong':so_luong,
                                                'tong_gia_tri':tong_gia_tri})

def cart_add(request):
    # Get cart
    cart= Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get infor products
        san_pham_id = int(request.POST.get("san_pham_id"))
        so_luong = int(request.POST.get("so_luong"))
        
        # Lookup product in dataBase
        san_pham = get_object_or_404(NhapHang, id=san_pham_id)
        
        # Save to session
        cart.add(san_pham = san_pham, so_luong = so_luong)#

        # Get quatity món hàng trong giỏ
        cart_quantity = cart.__len__()
        # print("--------------------VIIgiohang\views.py, cart", cart)
        # print("--------------------VIIgiohang\views.py, cart_quantity", cart_quantity)
        # Return resonse

        # Thông báo thêm sản phẩm thành công
        messages.success(request, (f'Đã thêm "{san_pham}" vào giỏ hàng thành công!!!'))

        response = JsonResponse({"ten_san_pham": san_pham.ten_san_pham, 
                                 "so_luong": so_luong,
                                 "so_luong_gio": cart_quantity})
        
        # Tạo phản hồi
        # message = f"Sản phẩm {san_pham.ten_san_pham} đã được thêm vào giỏ hàng (Số lượng: {cart_quantity})"
        # return  HttpResponse(message)

        return response


def cart_delete(request):
    cart= Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get infor products
        san_pham_id = int(request.POST.get("san_pham_id"))
        # Call delete function in Cart
        messages.success(request, (f'Đã xóa sản phẩm ra khỏi giỏ hàng!!!'))
        cart.delete(san_pham = san_pham_id)
        response = JsonResponse({"ten_san_pham": san_pham_id})
        return response

    # return render(request, 'cart_delete.html', {})

def cart_update(request):
    # Get cart
    cart= Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get infor products
        san_pham_id = int(request.POST.get("san_pham_id"))
        
        so_luong = int(request.POST.get("so_luong"))
        
        cart.update(san_pham = san_pham_id, so_luong = so_luong)

        messages.success(request, (f'Đã cập nhật số lượng vào giỏ hàng!!!'))
        response = JsonResponse({"so_luong": so_luong})
        
        # return redirect('cart_sumary')
        return response

