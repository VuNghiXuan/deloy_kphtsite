from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SanPham, NhapHang
import cv2
from pyzbar import pyzbar
import base64


def san_pham_detail(request, pk):
    san_pham = SanPham.objects.get(pk=pk)

    if request.method == 'POST':
        if 'scan_barcode' in request.POST:
            # Handle barcode scanning
            try:
                # Capture frame from webcam (replace 0 with desired camera index if needed)
                cap = cv2.VideoCapture(0)
                success, frame = cap.read()

                if success:
                    # Decode barcodes from frame using pyzbar
                    barcodes = pyzbar.decode(frame)

                    # Check for a single barcode (optional: enhance for multiple)
                    if len(barcodes) == 1:
                        barcode = barcodes[0]

                        # Extract barcode data (assuming UTF-8 encoding)
                        barcode_data = barcode.data.decode('utf-8')

                        # Find matching NhapHang object by ma_san_pham
                        try:
                            nhap_hang = NhapHang.objects.get(ma_san_pham=barcode_data)
                            # Populate form fields with data from NhapHang
                            context = {'san_pham': san_pham, 'nhap_hang': nhap_hang}
                            return render(request, 'san_pham_detail.html', context)
                        except NhapHang.DoesNotExist:
                            messages.error(request, 'Mã vạch không tìm thấy!')
                    else:
                        messages.warning(request, 'Terminated: Multiple barcodes detected. (Optional: Enhance for handling multiple)')
                else:
                    messages.error(request, 'Terminated: Could not capture frame!')

                cap.release()  # Release camera

            except cv2.Error as e:
                messages.error(request, f'Camera Error: {e}')

    context = {'san_pham': san_pham}
    return render(request, 'san_pham_detail.html', context)
