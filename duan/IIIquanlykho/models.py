from django.db import models
import barcode 
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.utils import timezone

from Ithongtincongty.models import LopCoBan, ChiNhanh
from IVdoitac.models import NhaCungCap
from IIcauhinhtrangchu.models import BoSuuTap

from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models.signals import pre_save
# # Create your models here.
# from permissions.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


# ... (import các model khác nếu cần)

class QuayLon(LopCoBan):
    # id = models.AutoField(primary_key=True, verbose_name="ID")
    # ma_quay_lon = models.AutoField(primary_key=True, verbose_name="Mã quầy lớn")
    ten_quay_lon = models.CharField(max_length=255, verbose_name="Tên quầy lớn", unique=True)
    chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True,  verbose_name="Thuộc chi nhánh", related_name='quay_lons', default=1)#related_name='ten_quay_lons', to_field='ten_chi_nhanh',
    # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True, related_name='phong_bans', default=1)  # Relates to ChiNhanh# on_delete=models.CASCADE,
    
    # hoat_dong = models.BooleanField(verbose_name="Hoạt động", default=True)
    class Meta:
        verbose_name = "Quầy lớn"
        verbose_name_plural = "1. Quầy lớn"
    
    def __str__(self):
        return self.ten_quay_lon


class QuayNho(LopCoBan):
    # id = models.AutoField(primary_key=True, verbose_name="ID")
    # ma_quay_nho = models.AutoField(primary_key=True, verbose_name="Mã quầy nhỏ")
    ten_quay_nho = models.CharField(max_length=255, verbose_name="Tên quầy nhỏ", unique=True)
    quay_lon = models.ForeignKey(QuayLon, on_delete=models.SET_NULL, null=True,  verbose_name="Thuộc quầy lớn", related_name='quay_nhos', default=1)
    chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True,  verbose_name="Thuộc chi nhánh", related_name='quay_nhos', default=1)#related_name='ten_quay_lons', to_field='ten_chi_nhanh',
    trong_luong_khay_ly = models.PositiveIntegerField(verbose_name="Trọng lượng khay ly", default=0)
    trong_luong_khay_gram = models.PositiveIntegerField(verbose_name="Trọng lượng khay gram", default=0)


    # hoat_dong = models.BooleanField(verbose_name="Hoạt động", default=True)

    class Meta:
        verbose_name = "Quầy nhỏ"
        verbose_name_plural = "2. Quầy nhỏ"

    def __str__(self):
        return self.ten_quay_nho

class NhomVang(LopCoBan):
    # ma_nhom_vang = models.AutoField(primary_key=True, verbose_name="Mã nhóm vàng")
    ten_nhom_vang = models.CharField(max_length=100, unique=True, verbose_name="Tên nhóm vàng")
    # hoat_dong = models.BooleanField(verbose_name="Hoạt động", default=True)

    class Meta:
        verbose_name = "Nhóm vàng"
        verbose_name_plural = "3. Nhóm vàng"

    def __str__(self):
        return self.ten_nhom_vang
    

# Khai báo các biến cho Loại vàng --------------------------------------

DON_VI_TINH_CHOICES = (
        ('1', 'Ly'),
        ('2', 'Gram'),
        ('3', 'Món')
    )
DON_VI_CAN_CHOICES = (
        ('1', 'Lượng'),
        ('2', 'Chỉ'),
        ('3', 'Phân'),
        ('3', 'Ly')
    )

TIEN_TE_CHOICES = (
        ('1', 'VND'),
        ('2', 'SIN'),
        ('3', 'THAI'),
        ('4', 'UC'),
        ('5', 'USD'),
        ('6', 'USD (1-2)'),
        ('7', 'USD (5-10-2)'),
    )
LAMTRON_CHOICES = (
        ('1', 'Đơn vị ngàn đồng'),
        ('2', 'Đơn vị chục ngàn đồng'),
        ('3', 'Đơn vị trăm ngàn đồng'),
        ('4', 'Đơn vị triệu đồng'),
        ('5', 'Không làm tròn')
        
    )


class LoaiVang(LopCoBan):    
    # id = models.AutoField(primary_key=True, verbose_name="ID")
    # ma_loai_vang = models.AutoField(primary_key=True, verbose_name="Tên loại vàng")
    ten_loai_vang = models.CharField(max_length=100, unique=True, verbose_name="Tên loại vàng")
    nhom_vang = models.ForeignKey(NhomVang, on_delete=models.SET_NULL, null=True, verbose_name="Thuộc nhóm vàng", default=1)#related_name='loai_vangs', 
    # MaCongTy = models.ForeignKey(CongTy, on_delete=models.CASCADE, verbose_name="Công ty", default=1)
    # MaChiNhanh = models.ForeignKey(ChiNhanh, on_delete=models.CASCADE, verbose_name="Chi nhánh", default=1)
    # MaQuayLon = models.ForeignKey(QuayLon, on_delete=models.CASCADE, verbose_name="Quầy lớn", default=1)
    # MaQuayNho = models.ForeignKey(QuayNho, on_delete=models.CASCADE, verbose_name="Quầy nhỏ", default=1)

    # MaNhomVang = models.ForeignKey(NhomVang, on_delete=models.CASCADE, verbose_name="Nhóm vàng", default=1)
    # TenLoaiVang = models.CharField(max_length=255, verbose_name="Tên loại vàng")
    tuoi_vang = models.FloatField(verbose_name="Tuổi vàng", default=0)
    tuoi_pho = models.CharField(max_length=50, verbose_name="Tuổi phổ", default=0)
    tien_te = models.CharField(max_length=100, choices=TIEN_TE_CHOICES, verbose_name="Tiền tệ", default=1)
    doi = models.PositiveIntegerField(verbose_name="Đổi", default=0)
    don_vi_tinh = models.CharField(max_length=100, choices=DON_VI_TINH_CHOICES, verbose_name="Đơn vị tính")
    
    do_uu_tien = models.PositiveIntegerField(verbose_name="Độ ưu tiên", null=True, blank=True)
    
    don_gia_bu = models.IntegerField(verbose_name="Đơn giá bù/Tiền bù", default=0)
    phantram_giabu = models.IntegerField(verbose_name="% Giá trị bù", default=0)
    
    hien_bang_dientu = models.CharField(max_length=255, verbose_name="Tên hiển thị bảng điện tử", default=0)
    ghi_chu = models.CharField(max_length=255, verbose_name="Ghi chú", null=True, blank=True)
    
    khoang_cach_1 = models.CharField(max_length=255, verbose_name="Khoảng cách 1", null=True, blank=True)
    khoang_cach_2 = models.CharField(max_length=255, verbose_name="Khoảng cách 2", null=True, blank=True)
    khoang_cach_3 = models.CharField(max_length=255, verbose_name="Khoảng cách 3", null=True, blank=True)
    khoang_cach_4 = models.CharField(max_length=255, verbose_name="Khoảng cách 4", null=True, blank=True)

    tygia_min = models.PositiveIntegerField(verbose_name="% Tỷ giá min", default=0)
    tygia_max = models.PositiveIntegerField(verbose_name="% Tỷ giá max", default=0)
    
    giamgia_bansi = models.IntegerField(verbose_name="Giảm giá bán sỉ", null=True, blank=True)
    
    "DonVi_Can: Chọn dẻ thì tắt cân, nhóm C"
    don_vi_can = models.CharField(max_length=50, choices=DON_VI_CAN_CHOICES, verbose_name="Đơn vị cân")
    
    # QuyCach_LamTron = models.CharField(max_length=50, choices=LAMTRON_CHOICES, verbose_name="Quy cách làm tròn")
    
    lamtron_giamuaban = models.CharField(max_length=150, choices=LAMTRON_CHOICES, verbose_name="Làm tròn giá mua bán")
    hienbang_dientu = models.BooleanField(verbose_name="Hiện bảng điện tử", null=True, blank=True)
    # Ban
    # hoat_dong = models.BooleanField(verbose_name="Hoạt động", default=True)
    
    class Meta:
        verbose_name = "Loại vàng"
        verbose_name_plural = "4. Loại vàng"

    
    def __str__(self):
        return self.ten_loai_vang

class NhomHang(LopCoBan):
    ma_nhom_hang = models.CharField(max_length=10, unique=True, verbose_name="Mã nhóm")
    ten_nhom_hang = models.CharField(max_length=100, unique=True, verbose_name="Tên nhóm hàng")
    quay_nho = models.ForeignKey(QuayNho, on_delete=models.SET_NULL, null=True, related_name='nhom_hangs', verbose_name="Quầy nhỏ", default=1)

    # hoat_dong = models.BooleanField(verbose_name="Hoạt động", default=True)
    class Meta:
        verbose_name = "Nhóm hàng"
        verbose_name_plural = "5. Nhóm hàng"

    def __str__(self):
        return self.ten_nhom_hang


# NHap hang ---------------------
TEM_CHOICE = (
        ('1', 'Tem theo món'),
        ('2', 'Không tem'),
        
    )

TEN_DANG_NHAP = (
        ('1', 'Chưa code'),
        ('2', 'Code sau'),
        
    )


    
class NhapHang(LopCoBan):
    # ma_nhap_hang = models.AutoField(primary_key=True, verbose_name="Mã nhập hàng")
    ten_san_pham = models.CharField(max_length=255, verbose_name="Tên sản phẩm")
    mo_ta = models.CharField(max_length=255, verbose_name="Mô tả", blank=True)
    hinh_anh = models.ImageField(upload_to='san_pham', blank=True, null=True, verbose_name="Hình ảnh")
    ten_chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True, related_name='nhap_hangs', verbose_name="Chi nhánh", default=1)
    quay_lon = models.ForeignKey(QuayLon, on_delete=models.SET_NULL, null=True, verbose_name="Quầy lớn", default=1)
    quay_nho = models.ForeignKey(QuayNho, on_delete=models.SET_NULL, null=True, related_name='nhap_hangs', verbose_name="Quầy nhỏ", default=1)
    loai_vang = models.ForeignKey(LoaiVang, on_delete=models.SET_NULL, null=True, related_name='nhap_hangs', verbose_name="Loại vàng")
    nhom_hang = models.ForeignKey(NhomHang, on_delete=models.SET_NULL, null=True, related_name='nhap_hangs', verbose_name="Nhóm hàng")
    bo_suu_tap = models.ForeignKey(BoSuuTap, on_delete=models.SET_NULL, null=True, related_name='nhap_hangs', verbose_name="Hiển thị trong bộ sưu tập", default=1)
    
    # ten_nhan_vien = models.CharField(max_length=100, choices=TEN_DANG_NHAP, verbose_name="Nhân viên nhập hàng")
    nhan_vien = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Nhân viên nhập hàng", null=True, blank= True)
    
    so_luong = models.PositiveIntegerField(default=1, verbose_name="Số lượng")
    tl_vang_hot = models.DecimalField(default=0, decimal_places=3, max_digits=6, verbose_name="Trọng lượng vàng + hột")
    tl_hot = models.DecimalField(default=0, decimal_places=3, max_digits=6, verbose_name="Trọng hột/SP")
    tl_vang = models.DecimalField(default=0, decimal_places=3, max_digits=6, verbose_name="Trọng vàng", editable=False)
    cong_von = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="Công vốn")
    cong_ban = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="Công bán")
    tien_hot = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="Tiền hột")
    gia_ban_mon = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="Giá bán món")

    # Hỏi lại rồi mở rộng sau
    # tem_hang = models.CharField(max_length=100, choices=TEM_CHOICE, verbose_name="Tem theo hàng")
    
    nha_cung_cap = models.ForeignKey(NhaCungCap, on_delete=models.SET_NULL, null=True, blank= True, related_name='nhap_hangs', verbose_name="Nhà cung cấp", default=1)#
    so_lo = models.CharField(max_length=50, verbose_name="Số lô")

    # nha_cung_cap = models.ForeignKey(NhaCungCap, on_delete=models.CASCADE)
    # ten_chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True, related_name='san_phams', verbose_name="Chi nhánh")

    tinh_trang = models.CharField(max_length=50, choices=(
        # ("Chờ duyệt nhập", "Chờ duyệt nhập"),
        ("Còn hàng", "Còn hàng"),
        ("Hết hàng", "Hết hàng"),
    ), verbose_name="Trạng thái", default="Còn hàng")
    

    
    # ten_nhan_vien = models.CharField(max_length=100, choices=DanhSachNhanVienNhapHang().get_nhap_hang_nhanvien(), verbose_name="Nhân viên nhập hàng")
    
    # **New line:**
    
    tem = models.ImageField(upload_to='tem', blank=True, verbose_name="Tem", editable=False)
    ma_san_pham = models.CharField(max_length=13, verbose_name="Mã sản phẩm", editable=False)
    ngay_nhap = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name="Ngày nhập hàng", editable=False)
    da_ban = models.PositiveIntegerField(verbose_name='SL bán', editable=False, default=0)
    ton_kho = models.PositiveIntegerField(verbose_name='SL tồn kho', editable=False, default=0)
    luot_thich = models.PositiveIntegerField(verbose_name='Khởi tạo lượt like', editable=False, default=0)

    def save(self, *args, **kwargs):
        # Automatically set QuayLon based on selected QuayNho
        if self.quay_nho:
            self.quay_lon = self.quay_nho.quay_lon
        # Update tinh_trang based on ton_kho
        # self.tinh_trang = "het_hang" if self.ton_kho == 0 else "con_hang"

        super().save(*args, **kwargs)  # Call the original save() method
    
    


    class Meta:
        verbose_name = "Nhập hàng"
        verbose_name_plural = "6. Nhập hàng"

    def __str__(self):
        return self.ten_san_pham

    
    # Tạo mã vạch
    def save(self, *args, **kwargs):
        # Lấy mã chi nhánh
        viettat_cn = None  
        if self.ten_chi_nhanh:
            try:
                # ten_cn = ChiNhanh.objects.get(pk=self.ten_chi_nhanh.pk)
                viettat_cn = ChiNhanh.objects.get(pk=self.ten_chi_nhanh.pk).ten_viet_tat
            except ChiNhanh.DoesNotExist:
                viettat_cn = "CN0"
            # print('----------------chi nhánh', viettat_cn)            

        # Lấy mã nhóm hàng
        ma_nh = None
        # ten_cn =''
        try:
            if self.nhom_hang:                
                ma_nh = NhomHang.objects.get(pk=self.nhom_hang.pk).ma_nhom_hang#.code_generation_function()
                # print('----------------Nhóm hàng', ma_nh)
                
        except NhomHang.DoesNotExist:
            ma_nh = "NH0"
            

        
        # Số thứ tự sản phẩm
        if not self.tem:
            try:                
                last_product = NhapHang.objects.order_by('-id').first()  # Order by descending ID
                if last_product:
                    highest_id = int(last_product.id) + 1
                else:
                    highest_id = 1  # Start with 1 if no products exist
            except ValueError:  # Handle potential conversion errors (e.g., non-numeric ID)                
                highest_id = 1
            product_id = str(highest_id).zfill(12)
            
            
            EAN = barcode.get_barcode_class('ean13')
            my_ean = EAN(product_id, writer=ImageWriter())
            # print('------------------------------unique_barcode_id sau:', product_id)
            
            # from PIL import Image
            with BytesIO() as buffer:
                my_ean.write(buffer)
                buffer.seek(0)  # Đặt con trỏ về đầu buffer
                # print('------------------------my_ean', my_ean)

                # Resize ảnh từ buffer
                to_be_resized = Image.open(buffer)
                newSize = (300, 100)
                resized_image = to_be_resized.resize(newSize, resample=Image.NEAREST)

                # Lưu ảnh resized
                with BytesIO() as resized_buffer:
                    resized_image.save(resized_buffer, format='PNG')
                    resized_buffer.seek(0)  # Đặt con trỏ về đầu resized_buffer

                    # Lưu ảnh vào trường tem
                    # resized_image.save(f'media/tem/{unique_barcode_id}.png') 
                    self.tem.save(f'{product_id}.png', File(resized_buffer), save=False)        
                    self.ma_san_pham = f"{viettat_cn}-{ma_nh}-{my_ean}"
        super().save(*args, **kwargs)


# Function to calculate and set tl_vang before saving the model
@receiver(pre_save, sender=NhapHang)
def calculate_tl_vang(sender, instance, **kwargs):
    instance.tl_vang = max(0, instance.tl_vang_hot - instance.tl_hot)  # Ensure non-negative weight

def calculate_ton_kho(sender, instance, **kwargs):
    instance.ton_kho = max(0, instance.so_luong-instance.da_ban)  # Ensure non-negative weight
    

# Register the signal handler
pre_save.connect(calculate_tl_vang, sender=NhapHang)
pre_save.connect(calculate_ton_kho, sender=NhapHang)



# Update số thứ tự
@receiver(post_delete, sender=QuayLon)
@receiver(post_delete, sender=QuayNho)
@receiver(post_delete, sender=NhomVang)
@receiver(post_delete, sender=LoaiVang)
@receiver(post_delete, sender=NhomHang)
@receiver(post_delete, sender=NhapHang)
# @receiver(post_delete, sender=SanPham)


def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 






