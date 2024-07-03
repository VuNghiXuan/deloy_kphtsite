from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NhapHang, LoaiVang, NhomHang, NhaCungCap, ChiNhanh, QuayLon, QuayNho
from django.contrib.auth.decorators import login_required

# View for creating a new product import record
@login_required
def create_nhaphang(request):
    if request.method == 'POST':
        # Get form data
        ten_san_pham = request.POST['ten_san_pham']
        # ... Get other relevant data from the form

        # Create a new NhapHang instance
        nhaphang = NhapHang.objects.create(
            ten_san_pham=ten_san_pham,
            # ... Set other fields using the form data
        )

        # Save the NhapHang object
        nhaphang.save()

        # Display a success message and redirect to the list view
        messages.success(request, "Nhập hàng thành công!")
        return redirect('nhaphang_list')

    # Render the form template
    context = {
        # ... Add any additional context variables needed for the form
    }
    return render(request, 'nhaphang/create_nhaphang.html', context)

# View for listing all product import records
@login_required
def nhaphang_list(request):
    # Get all NhapHang objects
    nhaphangs = NhapHang.objects.all()

    # Render the list template
    context = {
        'nhaphangs': nhaphangs,
    }
    return render(request, 'nhaphang/nhaphang_list.html', context)

# View for editing an existing product import record
@login_required
def edit_nhaphang(request, pk):
    # Get the NhapHang object to be edited
    nhaphang = NhapHang.objects.get(pk=pk)

    if request.method == 'POST':
        # ... Update NhapHang fields using the form data
        nhaphang.save()

        # Display a success message and redirect to the list view
        messages.success(request, "Cập nhật nhập hàng thành công!")
        return redirect('nhaphang_list')

    # Pre-populate the form with existing data
    context = {
        'nhaphang': nhaphang,
        # ... Add any additional context variables needed for the form
    }
    return render(request, 'nhaphang/edit_nhaphang.html', context)

# View for deleting a product import record
@login_required
def delete_nhaphang(request, pk):
    # Get the NhapHang object to be deleted
    nhaphang = NhapHang.objects.get(pk=pk)

    # Delete the NhapHang object
    nhaphang.delete()

    # Display a success message and redirect to the list view
    messages.success(request, "Xóa nhập hàng thành công!")
    return redirect('nhaphang_list')
