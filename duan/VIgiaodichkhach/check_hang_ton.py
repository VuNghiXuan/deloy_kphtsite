from django.core.exceptions import ValidationError
def validate_stock(quantity, nhap_hang):
    available_stock = nhap_hang.ton_kho
    # print("-------------------------------------------------quantity", quantity)
    # print("-----------------------------------------ton_kho", nhap_hang.ton_kho)
    if quantity > available_stock:
        raise ValidationError(f'Số lượng vượt quá kho hàng! Vui lòng nhập số lượng nhỏ hơn hoặc bằng {available_stock}')