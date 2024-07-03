from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny  # Optional: Permission for authenticated users only
# from rest_framework import permissions 

from .models import CongTy, ChiNhanh, PhongBan, NhiemVu, NhanVien
from .serializers import (
    CongTySerializer,
    ChiNhanhSerializer,
    PhongBanSerializer,
    NhiemVuSerializer,
    NhanVienSerializer,
)


class CongTyViewSet(viewsets.ModelViewSet):
    queryset = CongTy.objects.all()
    serializer_class = CongTySerializer
    
    # Quyền hạn dựa trên hành động (phương thức) được gọi
    def get_permissions(self):
        """
        Xác định quyền dựa trên hành động (phương thức) được gọi.
        """
        if self.action == 'list':
            permission_classes = [AllowAny()]  # Cho phép tất cả người dùng xem danh sách nhiemvu
        else:
            permission_classes = [IsAuthenticated()]  # Các hành động khác yêu cầu xác thực
        return permission_classes


    

class ChiNhanhViewSet(viewsets.ModelViewSet):
    queryset = ChiNhanh.objects.all()
    serializer_class = ChiNhanhSerializer
    
    # Quyền hạn dựa trên hành động (phương thức) được gọi
    def get_permissions(self):
        """
        Xác định quyền dựa trên hành động (phương thức) được gọi.
        """
        if self.action == 'list':
            permission_classes = [AllowAny()]  # Cho phép tất cả người dùng xem danh sách nhiemvu
        else:
            permission_classes = [IsAuthenticated()]  # Các hành động khác yêu cầu xác thực
        return permission_classes



class PhongBanViewSet(viewsets.ModelViewSet):
    queryset = PhongBan.objects.all()
    serializer_class = PhongBanSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # Quyền hạn dựa trên hành động (phương thức) được gọi
    def get_permissions(self):
        """
        Xác định quyền dựa trên hành động (phương thức) được gọi.
        """
        if self.action == 'list':
            permission_classes = [AllowAny()]  # Cho phép tất cả người dùng xem danh sách nhiemvu
        else:
            permission_classes = [IsAuthenticated()]  # Các hành động khác yêu cầu xác thực
        return permission_classes



class NhiemVuViewSet(viewsets.ModelViewSet):

    queryset = NhiemVu.objects.all()  # Lấy tất cả các đối tượng NhiemVu
    serializer_class = NhiemVuSerializer  # Lớp serializer để chuyển đổi dữ liệu giữa JSON và object

    # Quyền hạn dựa trên hành động (phương thức) được gọi
    def get_permissions(self):
        """
        Xác định quyền dựa trên hành động (phương thức) được gọi.
        """
        if self.action == 'list':
            permission_classes = [AllowAny()]  # Cho phép tất cả người dùng xem danh sách nhiemvu
        else:
            permission_classes = [IsAuthenticated()]  # Các hành động khác yêu cầu xác thực
        return permission_classes


class NhanVienViewSet(viewsets.ModelViewSet):
    queryset = NhanVien.objects.all()
    serializer_class = NhanVienSerializer

    # Quyền hạn dựa trên hành động (phương thức) được gọi
    def get_permissions(self):
        """
        Xác định quyền dựa trên hành động (phương thức) được gọi.
        """
        if self.action == 'list':
            permission_classes = [AllowAny()]  # Cho phép tất cả người dùng xem danh sách nhiemvu
        else:
            permission_classes = [IsAuthenticated()]  # Các hành động khác yêu cầu xác thực
        return permission_classes

    
    
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # Optional filtering based on user permissions or other criteria
    #     return queryset
