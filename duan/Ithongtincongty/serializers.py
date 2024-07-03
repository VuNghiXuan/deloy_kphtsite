from rest_framework import serializers
from .models import CongTy, ChiNhanh, PhongBan, NhiemVu, NhanVien

class CongTySerializer(serializers.ModelSerializer):
    so_nhan_vien = serializers.SerializerMethodField()

    class Meta:
        model = CongTy
        fields = '__all__'  # Include all fields by default

    def get_so_nhan_vien(self, obj):
        """
        Calculates the total number of employees across all branches belonging to this company.
        """
        return NhanVien.objects.filter(chi_nhanh__cong_ty=obj).count()

class ChiNhanhSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiNhanh
        fields = '__all__'  # Include all fields by default

class PhongBanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhongBan
        fields = '__all__'  # Include all fields by default

class NhiemVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NhiemVu
        fields = '__all__'  # Include all fields by default

class NhanVienSerializer(serializers.ModelSerializer):
    # nhiem_vu = NhiemVuSerializer(many = True)
    class Meta:
        model = NhanVien
        fields = '__all__'  # Include all fields by default, or customize as needed

        
