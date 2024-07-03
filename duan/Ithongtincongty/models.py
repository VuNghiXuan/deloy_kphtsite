from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

# class User(AbstractUser): #Lesson    
#     # ten_nhan_vien = models.CharField(max_length=100, verbose_name=_("Tên nhân viên"), null=True)
#     # phong_ban = models.ForeignKey('PhongBan', on_delete=models.SET_NULL, null=True, related_name='nhanvien', verbose_name=_("Thuộc phòng ban"))
#     # chi_nhanh = models.ForeignKey('ChiNhanh', on_delete=models.SET_NULL, null=True, related_name='nhanvien', verbose_name=_("Thuộc chi nhánh"))
#     anh_dai_dien = models.ImageField(upload_to='avatar/%Y/%m', verbose_name=_("Ảnh đại diện"), default=None, null= True, blank=True)
#     # nhiem_vu = models.ManyToManyField(NhiemVu, related_name='nhanvien', verbose_name=_("Nhiệm vụ"), blank=True)
#     class Meta:
#         verbose_name = _("Đăng ký tài khoản")
#         verbose_name_plural = _("6. Đăng ký tài khoản")
    
    # def __str__(self):
    #     return self.ten_nhan_vien

    


class LopCoBan(models.Model):
    # Không muốn tạo ra table Số thứ tự
    class Meta:
        abstract = True
    so_thu_tu = models.CharField(max_length = 10, verbose_name=_("STT"), editable=False, blank='')
    kich_hoat = models.BooleanField(default= True, verbose_name=_("Kích hoạt"), editable=True, blank='')
    # models.CharField(max_length = 10, verbose_name=_("Kích hoạt"), editable=False, blank='')
    def save(self, *args, **kwargs):
        if not self.id:
            last_stt = self.__class__.objects.last()
            if last_stt:
                last_stt = int(last_stt.so_thu_tu)
                self.so_thu_tu = str(last_stt + 1)
            else:
                self.so_thu_tu = '1'
        super(LopCoBan, self).save(*args, **kwargs)


class CongTy(LopCoBan):  # Category
    ten_cong_ty = models.CharField(max_length=255, verbose_name=_("Tên công ty"), unique=True)
    ten_viet_tat = models.CharField(max_length=100, verbose_name=_("Tên viết tắt"), unique=True)
    logoCongTy = models.ImageField(upload_to="congty/%Y/%m", verbose_name=_("Thêm Logo"), null=True, blank=True)
    dia_chi = models.CharField(max_length=255, verbose_name=_("Địa chỉ"))
    hotline = models.CharField(max_length=15, verbose_name=_("Hotline"))
    kick_hoat_web = models.BooleanField(default= False, verbose_name=_("Hiển thị thông tin lên Website"))

    class Meta:
        verbose_name = _("Công ty")
        verbose_name_plural = _("1. Công ty")
        

    def __str__(self):
        return self.ten_cong_ty

    def so_nhan_vien(self):
        """
        Counts the total number of employees across all branches belonging to this company.
        """
        return NhanVien.objects.filter(chi_nhanh__cong_ty=self).count()

    

class ChiNhanh(LopCoBan): #Course
    ten_chi_nhanh = models.CharField(max_length=100, verbose_name=_("Tên chi nhánh"), unique=True)
    cong_ty = models.ForeignKey(CongTy, on_delete=models.SET_NULL, null=True,related_name='chi_nhanhs', verbose_name=_("Trực thuộc công ty"), default=1)
    ten_viet_tat = models.CharField(max_length=100, verbose_name=_("Tên viết tắt"), unique=True)
    dia_chi = models.CharField(max_length=255, verbose_name=_("Địa chỉ"))
    hotline = models.CharField(max_length=15, verbose_name=_("Hotline"))
    # kich_hoat = models.BooleanField(default=True, verbose_name=_("Hiển thị thông tin lên Website")) # Luôn tất, dựa vào đăng nhập cho True sau

    class Meta:
        verbose_name = _("Chi nhánh")
        verbose_name_plural = _("2. Chi nhánh")
        

    def __str__(self):
        return self.ten_chi_nhanh


class PhongBan(LopCoBan):
    ten_phong_ban = models.CharField(max_length=100, verbose_name=_("Tên phòng ban"), unique=True)
    # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.CASCADE, related_name='phong_bans', verbose_name=_("Thuộc chi nhánh"), default=1)

    class Meta:
        verbose_name = _("Phòng ban")
        verbose_name_plural = _("3. Phòng ban")
        

    def __str__(self):
        return self.ten_phong_ban

    # def so_nhan_vien(self):
    #     """
    #     Counts the total number of employees belonging to this department.
    #     """
    #     return self.nhanviens.count()

class NhiemVu(LopCoBan): #Task
    ten_nhiem_vu = models.CharField(max_length=100, verbose_name=_("Tên nhiệm vụ"), unique=True)

    class Meta:
        verbose_name = _("Nhiệm vụ nhân viên")
        verbose_name_plural = _("4. Nhiệm vụ nhân viên")
        

    def __str__(self):
        return self.ten_nhiem_vu

class NhanVien(LopCoBan): #Lesson
    ten_nhan_vien = models.CharField(max_length=255, verbose_name=_("Tên nhân viên"), null=True)
    chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, related_name='nhanvien', verbose_name=_("Chi nhánh"), null=True, default=1)
    # anh_dai_dien = models.ImageField(upload_to='chinhanh/%Y/%m', verbose_name=_("Ảnh đại diện"), default=None)
    nhiem_vu = models.ManyToManyField(NhiemVu, related_name='nhanvien', verbose_name=_("Nhiệm vụ"), blank=True)
    # phong_ban = models.ForeignKey('PhongBan', on_delete=models.SET_NULL, null=True, related_name='nhanvien', verbose_name=_("Thuộc phòng ban"))
    
    # Trường lưu trữ tên đăng nhập
    # ten_dang_nhap = models.CharField(max_length=255, editable=False, verbose_name="Tên đăng nhập")

    # Trường lưu trữ mật khẩu đã mã hóa
    # mat_khau = models.CharField(max_length=255, editable=False, verbose_name="Mật khẩu")

    # Trường lưu trữ thời gian đăng nhập cuối cùng
    # dang_nhap_lan_cuoi = models.DateTimeField(null=True, blank=True, verbose_name="Lần đăng nhập cuối cùng")

    def __str__(self):
        return self.ten_nhan_vien
    
    class Meta:
        verbose_name = _("Danh sách nhân viên")
        verbose_name_plural = _("5. Danh sách nhân viên")
        

    

    # def save(self, *args, **kwargs):
    #     # Cập nhật trường username_hien_thi
    #     self.ten_dang_nhap = self.username

    #     # Cập nhật trường password_hien_thi (lưu mật khẩu đã mã hóa)
    #     if self.password:
    #         self.mat_khau = self.password

    #     # Cập nhật trường last_login khi lưu mới hoặc khi mật khẩu thay đổi
    #     if self.pk is None or self.password != self._old_password:
    #         self.last_login = timezone.now()

    #     super().save(*args, **kwargs)


# Update số thứ tự
@receiver(post_delete, sender=CongTy)
@receiver(post_delete, sender=ChiNhanh)
@receiver(post_delete, sender=PhongBan)
@receiver(post_delete, sender=NhiemVu)
@receiver(post_delete, sender=NhanVien)

def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 