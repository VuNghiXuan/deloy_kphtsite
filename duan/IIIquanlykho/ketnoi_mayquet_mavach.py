# import cv2 as cv
# from pyzbar import pyzbar

# # Capture webcam
# cap = cv.VideoCapture(0)

# found_barcode = False

# while not found_barcode:
#     success, frame = cap.read()
#     barcodes = pyzbar.decode(frame)
    
#     if not barcodes:
#         print("Không phát hiện được mã barcode")
#     else:
#         for barcode in barcodes:            
#             (x, y, m, h) = barcode.rect
#             cv.rectangle(frame, (x, y), (x + m, y + h), (0, 255, 255), 2)
#             barcodeData = barcode.data.decode('utf-8')
#             barcodeType = barcode.type
#             text = "{} - {}".format(barcodeData, barcodeType)
#             print(text)
#             cv.putText(frame, text, (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            
#             found_barcode = True  # Đánh dấu đã tìm thấy mã vạch
#             break  # Thoát khỏi vòng lặp khi tìm thấy mã vạch
    
#     cv.imshow('Đọc mã vạch - mã QR', frame)
    
#     key = cv.waitKey(1)
#     if key == ord('q'):
#         break

# # Giải phóng camera
# cap.release()
# cv.destroyAllWindows()



