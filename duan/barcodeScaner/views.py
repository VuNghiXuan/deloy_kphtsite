# from django.shortcuts import render
# from django.http import HttpResponse
# import cv as cv
# from pyzbar import pyzbar 
# from pyzbar.pyzbar import decode
# from .models import Barcode
# from django.utils import timezone
# import threading
# import time
# import pygame
# import os

# # Create your views here.

# # initialize pygame mixer
# pygame.mixer.init()

# sound_file_path = os.path.join(os.path.dirname(__file__), 'beep.wav')
# def play_sound():
#     pygame.mixer.music.load(sound_file_path)
#     pygame.mixer.music.play()

# scanning_active = True

# def barcode_scanner():
#     global scanning_active
#     # Capture webcam

#     cap = cv.VideoCapture(0)
#     scanned_barcodes = set()

#     found_barcode = True

#     while cap.isOpened() and found_barcode and scanning_active:
#         success, frame = cap.read()
#         frame = cv.flip(frame, 1)
#         frame = cv.resize(frame, (640, 480))

#         if cap.get(1)%5 == 0:
#             barcodes = decode(frame)
#             for barcode in barcodes: 
#                 if barcode.data !="" and   barcode.data not in scanned_barcodes:        
#                     (x, y, m, h) = barcode.rect
#                     cv.rectangle(frame, (x, y), (x + m, y + h), (0, 255, 255), 2)
#                     # barcodeData = barcode.data.decode('utf-8')
#                     # barcodeType = barcode.type
#                     # text = "{} - {}".format(barcodeData, barcodeType)
#                     # cv.putText(frame, text, (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
#                     text = str(barcode.data)
#                     cv.putText(frame, text, (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
#                     print('barcode.data', barcode.data)
#                     print('scanned_barcodes', scanned_barcodes)
                    
#                     print(text)
                    
#                     Barcode.objects.create(du_lieu = str(barcode.data), ngay_tao = timezone.now())
#                     # scanned_barcodes.add(barcode.data)
#                     play_sound()
#                     scanning_active = False
#                     # found_barcode = True  # Đánh dấu đã tìm thấy mã vạch
#                     break  # Thoát khỏi vòng lặp khi tìm thấy mã vạch
    
        
#             else: 
            
#                 print("Không phát hiện được mã barcode")
#         # else:
#         #     for barcode in barcodes:            
#         #         (x, y, m, h) = barcode.rect
#         #         cv.rectangle(frame, (x, y), (x + m, y + h), (0, 255, 255), 2)
#         #         barcodeData = barcode.data.decode('utf-8')
#         #         barcodeType = barcode.type
#         #         text = "{} - {}".format(barcodeData, barcodeType)
#         #         print(text)
#         #         cv.putText(frame, text, (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
                
#         #         found_barcode = True  # Đánh dấu đã tìm thấy mã vạch
#         #         break  # Thoát khỏi vòng lặp khi tìm thấy mã vạch
        
#         cv.imshow('Đọc mã vạch - mã QR', frame)
        
#         key = cv.waitKey(1)
#         if key == ord('q'):
#             break
#         time.sleep(0.1)

#     # Giải phóng camera
#     cap.release()
#     cv.destroyAllWindows()
# def scan_view(request):
#     global scanning_active
#     scanning_thread = threading.Thread(target=barcode_scanner)
#     scanning_thread.start()
#     return HttpResponse('Bắt đầu đọc barcode. Nhấn "q" để thoát')

# def stop_scan(request):
#     global scanning_active
#     scanning_active = False
#     return HttpResponse('Đã ngừng đọc barcode.')



from django.shortcuts import render
from django.http import HttpResponse
import cv2 as cv
from pyzbar import pyzbar 
from pyzbar.pyzbar import decode
from .models import Barcode
from django.utils import timezone
import threading
import time
import pygame
import os

# Create your views here.

# initialize pygame mixer
pygame.mixer.init()

sound_file_path = os.path.join(os.path.dirname(__file__), 'beep.wav')
def play_sound():
    pygame.mixer.music.load(sound_file_path)
    pygame.mixer.music.play()

scanning_active = True


def process_barcode(frame, barcode, request):
    (x, y, m, h) = barcode.rect
    cv.rectangle(frame, (x, y), (x + m, y + h), (0, 255, 255), 2)
    text = str(barcode.data)
    cv.putText(frame, text, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
    print(f'Barcode data: {text}')

    # Set temporary message
    from django.contrib.messages import success
    success(request, 'Đã đọc được mã vạch!')
    

    # Filter based on your needs (e.g., minimum length)
    if len(text) >= 5:  # Example filter for minimum length
        Barcode.objects.create(du_lieu=text, ngay_tao=timezone.now())
        play_sound()

def barcode_scanner(request):
    global scanning_active
    # Capture webcam
    cap = cv.VideoCapture(0)
    scanned_barcodes = set()  # Uncomment to keep track of scanned codes (optional)

    while cap.isOpened() and scanning_active:
        success, frame = cap.read()
        if not success:
            print("Không tìm thấy kết nối Camare.")
            break

        frame = cv.flip(frame, 1)
        frame = cv.resize(frame, (640, 480))

        if cap.get(1) % 5 == 0:
            barcodes = decode(frame)           
            for barcode in barcodes:
                if barcode.data not in scanned_barcodes:  # Uncomment for duplicate handling
                    process_barcode(frame, barcode, request)
                    # process_barcode(frame, barcode)  # Pass frame as argument
                    scanned_barcodes.add(barcode.data)  # Uncomment for duplicate handling 
                    break  # Stop processing barcodes after finding one (optional)            

        cv.imshow('Scanner Barcode ', frame)

        key = cv.waitKey(1)
        if key == ord('q'):
            break
        time.sleep(0.1)

    # Release resources
    cap.release()
    cv.destroyAllWindows()

def scan_view(request):
    global scanning_active
    scanning_thread = threading.Thread(target=lambda: barcode_scanner(request))
    scanning_thread.start()
    return render(request, 'scan.html')  # Render scan.html with messages

def stop_scan(request):
    global scanning_active
    scanning_active = False
    return HttpResponse('Đã ngừng đọc barcode.')
