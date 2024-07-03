from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DonHang, DonHangChiTiet, SanPham, KhachHang, ChiNhanh, NhanVien
from django.contrib.auth.decorators import login_required

# View for creating a new sales order
@login_required
def create_donhang(request):
    if request.method == 'POST':
        # Get form data
        loai_giao_dich = request.POST['loai_giao_dich']
        ngay_tao = request.POST['ngay_tao']
        # ... Get other relevant data from the form

        # Create a new DonHang instance
        donhang = DonHang.objects.create(
            loai_giao_dich=loai_giao_dich,
            ngay_tao=ngay_tao,
            # ... Set other fields using the form data
        )

        # Add order details (DonHangChiTiet)
        # ... Get order item data from the form
        # ... Create DonHangChiTiet instances and associate them with the DonHang object

        # Save the DonHang object
        donhang.save()

        # Display a success message and redirect to the list
