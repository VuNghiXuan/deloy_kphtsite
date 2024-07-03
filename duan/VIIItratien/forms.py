# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import ShippingAddress

# Form thông tin giao hàng
class ShippingForm(forms.ModelForm):
	shipping_full_name = forms.CharField(label='Họ và tên người nhận', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Họ và tên người nhận'}), required=True)
	shipping_address = forms.CharField(label='Địa chỉ giao hàng', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Địa chỉ giao hàng'}), required=True)#(max_length=200, blank= True, verbose_name= 'Địa chỉ')
	shipping_phone = forms.CharField(label='Số điện thoại', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Số điện thoại'}), required=True)#(max_length=20, blank= True, verbose_name= 'Số điện thoại')
	# shipping_bank_account = forms.CharField(label='Số tài khoản', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Số tài khoản'}), required=False)#(max_length=20, blank= True, verbose_name= 'Tài khoản ngân hàng')
	
	# shipping_email = forms.CharField(label='Địa chỉ email', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Địa chỉ email'}), required=False)#(max_length=200, blank= True, verbose_name= 'Địa chỉ')
	shipping_id_card = forms.CharField(label='Số CCCD/CMND', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nhập số căn cước công dân'}), required=False)#(max_length=20, blank= True, verbose_name= 'Căn cước công dân')
	# shipping_address = forms.CharField(label='Chỗ ở hiện nay', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Địa chỉ'}), required=False)#(max_length=200, blank= True, verbose_name= 'Địa chỉ')

	# shipping_avatar = forms.ImageField(label='Ảnh đại diện', required=False)
	# city = models.CharField(max_length=200, blank= True, verbose_name= 'Thành phố')
	# province = models.CharField(max_length=200, blank= True, verbose_name= 'Tỉnh')

	class Meta:
		model = ShippingAddress
		fields = ['shipping_full_name', 'shipping_address', 'shipping_phone',  ] #'shipping_avatar'
		exclude = ['user',]

# Form thông tin thanh toán
class PaymentForm(forms.Form):
	card_name = forms.CharField(label='Tên chủ thẻ', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nhập tên chủ thẻ'}), required=False)
	bank_account = forms.CharField(label='Số tài khoản', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Số tài khoản'}), required=False)#(max_length=200, blank= False, verbose_name= 'Địa chỉ')
	bank_name = forms.CharField(label='Tên ngân hàng', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Tên ngân hàng'}), required=False)#(max_length=20, blank= True, verbose_name= 'Số điện thoại')
	contents = forms.CharField(label='Nội dung chuyển khoản', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ghi chú nội dung (kèm số tiền chuyển khoản)'}), required=False)#(max_length=20, blank= True, verbose_name= 'Số điện thoại')
	

	# class Meta:
	# 	model = ShippingAddress
	# 	fields = ['shipping_full_name', 'shipping_address', 'shipping_phone',  ] #'shipping_avatar'
	# 	exclude = ['user',]



# https://github.com/flatplanet/musker/blob/main/musker/forms.py