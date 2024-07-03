from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import UserProfile

# Thêm thông tin cá nhân người dùng
class UserInfoForm(forms.ModelForm):
	
	phone = forms.CharField(label='Số điện thoại', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nhập số điện thoại'}), required=False)#(max_length=20, blank= True, verbose_name= 'Số điện thoại')
	bank_account = forms.CharField(label='Số tài khoản', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nhập số tài khoản'}), required=False)#(max_length=20, blank= True, verbose_name= 'Tài khoản ngân hàng')
	id_card = forms.CharField(label='Số CCCD/CMND', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nhập số căn cước công dân'}), required=False)#(max_length=20, blank= True, verbose_name= 'Căn cước công dân')
	# avatar = forms.ImageField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ảnh đại diện'}), required=False)#(upload_to="users/%Y/%m", verbose_name="Ảnh đại diện", null=True, blank=True)
	address = forms.CharField(label='Chỗ ở hiện nay', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nhập địa chỉ'}), required=False)#(max_length=200, blank= True, verbose_name= 'Địa chỉ')
	avatar = forms.ImageField(label='Ảnh đại diện', required=False)
	# city = models.CharField(max_length=200, blank= True, verbose_name= 'Thành phố')
	# province = models.CharField(max_length=200, blank= True, verbose_name= 'Tỉnh')

	class Meta:
		model = UserProfile
		fields = ['address','phone', 'id_card', 'bank_account', 'avatar']
        

    

# Chỉnh sửa password
class ChangePassWordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1', 'new_password2']
	
	def __init__(self, *args, **kwargs):
		super(ChangePassWordForm, self).__init__(*args, **kwargs)

		
		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Nhập lại mật khẩu mới'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Mật khẩu của bạn không được quá giống với thông tin cá nhân khác của bạn.</li><li>Mật khẩu của bạn phải chứa ít nhất 8 ký tự.</li><li>Mật khẩu của bạn không được là mật khẩu thông dụng.</li><li>Mật khẩu của bạn không được hoàn toàn là số.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Xác nhận mật khẩu'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Nhập mật khẩu giống như lần đầu để xác minh.</small></span>'
		

# Cập nhật và chỉnh sửa tài khoản
class UpdateUserForm(UserChangeForm):
	# Ẩn password
	password = None	
	
	email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nhập email'}), required=False)
	last_name = forms.CharField(label="Họ và tên lót", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Họ và tên lót'}), required=False)
	first_name = forms.CharField(label="Tên thường dùng", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên'}), required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Tên đăng nhập'
		self.fields['username'].label = 'Tên đăng nhập'
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Yêu cầu. 150 ký tự trở xuống. Chỉ các chữ cái, chữ số và @/./+/-/_.</small></span>'

		

# Đăng ký mới
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Họ và tên lót'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Tên đăng nhập'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Yêu cầu. 150 ký tự trở xuống. Chỉ các chữ cái, chữ số và @/./+/-/_.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Mật khẩu'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Mật khẩu của bạn không được quá giống với thông tin cá nhân khác của bạn.</li><li>Mật khẩu của bạn phải chứa ít nhất 8 ký tự.</li><li>Mật khẩu của bạn không được là mật khẩu thông dụng.</li><li>Mật khẩu của bạn không được hoàn toàn là số.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Xác nhận mật khẩu'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Nhập mật khẩu giống như lần đầu để xác minh.</small></span>'
		
# https://github.com/flatplanet/musker/blob/main/musker/forms.py