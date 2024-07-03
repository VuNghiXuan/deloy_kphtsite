# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
# from django import forms

# # Chỉnh sửa password
# class ChangePassWordForm(SetPasswordForm):
# 	class Meta:
# 		model = User
# 		fields = ['new_password1', 'new_password2']
	
# 	def __init__(self, *args, **kwargs):
# 		super(ChangePassWordForm, self).__init__(*args, **kwargs)

		
# 		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
# 		self.fields['new_password1'].widget.attrs['placeholder'] = 'Nhập lại mật khẩu mới'
# 		self.fields['new_password1'].label = ''
# 		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Mật khẩu của bạn không được quá giống với thông tin cá nhân khác của bạn.</li><li>Mật khẩu của bạn phải chứa ít nhất 8 ký tự.</li><li>Mật khẩu của bạn không được là mật khẩu thông dụng.</li><li>Mật khẩu của bạn không được hoàn toàn là số.</li></ul>'

# 		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
# 		self.fields['new_password2'].widget.attrs['placeholder'] = 'Xác nhận mật khẩu'
# 		self.fields['new_password2'].label = ''
# 		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Nhập mật khẩu giống như lần đầu để xác minh.</small></span>'
		

# # Cập nhật và chỉnh sửa tài khoản
# class UpdateUserForm(UserChangeForm):
# 	# Ẩn password
# 	password = None	
	
# 	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
# 	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Họ và tên lót'}))
# 	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên'}))

# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email')

# 	def __init__(self, *args, **kwargs):
# 		super(UpdateUserForm, self).__init__(*args, **kwargs)

# 		self.fields['username'].widget.attrs['class'] = 'form-control'
# 		self.fields['username'].widget.attrs['placeholder'] = 'Tên đăng nhập'
# 		self.fields['username'].label = ''
# 		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Yêu cầu. 150 ký tự trở xuống. Chỉ các chữ cái, chữ số và @/./+/-/_.</small></span>'

		

# # Đăng ký mới
# class SignUpForm(UserCreationForm):
# 	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
# 	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Họ và tên lót'}))
# 	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên'}))

# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# 	def __init__(self, *args, **kwargs):
# 		super(SignUpForm, self).__init__(*args, **kwargs)

# 		self.fields['username'].widget.attrs['class'] = 'form-control'
# 		self.fields['username'].widget.attrs['placeholder'] = 'Tên đăng nhập'
# 		self.fields['username'].label = ''
# 		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Yêu cầu. 150 ký tự trở xuống. Chỉ các chữ cái, chữ số và @/./+/-/_.</small></span>'

# 		self.fields['password1'].widget.attrs['class'] = 'form-control'
# 		self.fields['password1'].widget.attrs['placeholder'] = 'Mật khẩu'
# 		self.fields['password1'].label = ''
# 		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Mật khẩu của bạn không được quá giống với thông tin cá nhân khác của bạn.</li><li>Mật khẩu của bạn phải chứa ít nhất 8 ký tự.</li><li>Mật khẩu của bạn không được là mật khẩu thông dụng.</li><li>Mật khẩu của bạn không được hoàn toàn là số.</li></ul>'

# 		self.fields['password2'].widget.attrs['class'] = 'form-control'
# 		self.fields['password2'].widget.attrs['placeholder'] = 'Xác nhận mật khẩu'
# 		self.fields['password2'].label = ''
# 		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Nhập mật khẩu giống như lần đầu để xác minh.</small></span>'
		
# # https://github.com/flatplanet/musker/blob/main/musker/forms.py