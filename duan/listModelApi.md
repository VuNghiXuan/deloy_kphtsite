# Api và Model    
    API và Model cho trang web bán vàng trang sức và cầm đồ
    Model:

    Sản phẩm:

    id: Khóa chính tự động tăng.
    loại_sản_phẩm: Loại sản phẩm (vàng, trang sức, cầm đồ).
    ten_sản_phẩm: Tên sản phẩm.
    mô_tả: Mô tả chi tiết sản phẩm.
    giá_bán: Giá bán sản phẩm.
    giá_gốc: Giá gốc sản phẩm (tùy chọn).
    trọng_lượng: Trọng lượng sản phẩm (tùy chọn).
    độ_tinh_khiết: Độ tinh khiết của vàng (tùy chọn).
    kiểu_chế_tác: Kiểu chế tác sản pahẩm (tùy chọn).
    hình_ảnh: Hình ảnh sản phẩm.
    tình_trạng: Tình trạng sản phẩm (còn hàng, hết hàng).
    Khách hàng:

    id: Khóa chính tự động tăng.
    họ_tên: Họ và tên khách hàng.
    số_điện_thoại: Số điện thoại khách hàng.
    địa_chỉ: Địa chỉ khách hàng.
    email: Email khách hàng (tùy chọn).
    Hóa đơn:

    id: Khóa chính tự động tăng.
    ngày_lập: Ngày lập hóa đơn.
    loại_hóa_đơn: Loại hóa đơn (bán hàng, cầm đồ).
    nhân_viên: Nhân viên lập hóa đơn.
    khách_hang: Khách hàng liên quan đến hóa đơn.
    chi_tiết_hóa_đơn: Chi tiết các sản phẩm trong hóa đơn (sản phẩm, số lượng, giá bán).
    tổng_thanh_toán: Tổng số tiền thanh toán.
    phương_thức_thanh_toán: Phương thức thanh toán (tiền mặt, thẻ ngân hàng).
    Phiếu cầm đồ:

    id: Khóa chính tự động tăng.
    ngày_cầm: Ngày cầm đồ.
    khách_hang: Khách hàng cầm đồ.
    sản_phẩm_cầm: Sản phẩm cầm đồ.
    số_tiền_cầm: Số tiền cầm đồ.
    lãi_suất: Lãi suất cầm đồ.
    hạn_thanh_toán: Hạn thanh toán cầm đồ.
    tình_trạng: Tình trạng phiếu cầm đồ (chưa thanh toán, đã thanh toán, quá hạn).
    Nhà cung cấp:

    id: Khóa chính tự động tăng.
    tên_nhà_cung_cấp: Tên nhà cung cấp.
    số_điện_thoại: Số điện thoại nhà cung cấp.
    địa_chỉ: Địa chỉ nhà cung cấp.
    email: Email nhà cung cấp (tùy chọn).
    Phiếu nhập hàng:

    id: Khóa chính tự động tăng.
    ngày_nhập: Ngày nhập hàng.
    nhà_cung_cấp: Nhà cung cấp sản phẩm.
    chi_tiết_phiếu_nhập: Chi tiết các sản phẩm nhập hàng (sản phẩm, số lượng, giá nhập).
    tổng_thanh_toán: Tổng số tiền thanh toán cho nhà cung cấp.
    API:

    API quản lý sản phẩm:

    Lấy danh sách sản phẩm.
    Lấy thông tin chi tiết sản phẩm.
    Thêm sản phẩm mới.
    Cập nhật thông tin sản phẩm.
    Xóa sản phẩm.
    API quản lý khách hàng:

    Lấy danh sách khách hàng.
    Lấy thông tin chi tiết khách hàng.
    Thêm khách hàng mới.
    Cập nhật thông tin khách hàng.
    Xóa khách hàng.
    API quản lý hóa đơn:

    Lấy danh sách hóa đơn.
    Lấy thông tin chi tiết hóa đơn.
    Thêm hóa đơn mới.
    Cập nhật thông tin hóa đơn.
    Xóa hóa đơn.

    ----oOo---------------
    1. Đơn hàng:

    id: Khóa chính tự động tăng.
    khách_hàng: Khách hàng liên quan đến đơn hàng.
    nhân_viên: Nhân viên tạo đơn hàng.
    ngày_đặt_hàng: Ngày đặt hàng.
    ngày_giao_hàng: Ngày dự kiến giao hàng (tùy chọn).
    trạng_thai: Trạng thái đơn hàng (chờ xác nhận, đã xác nhận, đang xử lý, đã giao hàng, đã hủy).
    phương_thức_thanh_toán: Phương thức thanh toán (tiền mặt, thẻ ngân hàng, thanh toán trực tuyến).
    tổng_thanh_toán: Tổng số tiền thanh toán.
    chi_tiết_đơn_hàng: Chi tiết các sản phẩm trong đơn hàng (sản phẩm, số lượng, giá bán).
    ghi_chú: Ghi chú về đơn hàng (tùy chọn).
    2. Chi tiết đơn hàng:

    id: Khóa chính tự động tăng.
    đơn_hàng: Đơn hàng liên quan đến chi tiết.
    sản_phẩm: Sản phẩm trong đơn hàng.
    số_lượng: Số lượng sản phẩm.
    giá_bán: Giá bán sản phẩm trong đơn hàng.
    API:

    1. API quản lý đơn hàng:

    Lấy danh sách đơn hàng.
    Lấy thông tin chi tiết đơn hàng.
    Thêm đơn hàng mới.
    Cập nhật thông tin đơn hàng.
    Xóa đơn hàng.
    2. API quản lý chi tiết đơn hàng:

    Lấy danh sách chi tiết đơn hàng theo đơn hàng.
    Thêm chi tiết đơn hàng mới.
    Cập nhật thông tin chi tiết đơn hàng.
    Xóa chi tiết đơn hàng.
    Ví dụ code (sử dụng Django REST Framework):

    models.py:
    from django.db import models

    class Product(models.Model):
        # ... (các trường như trước)

    class Customer(models.Model):
        # ... (các trường như trước)

        

    serializers.py:

    class Order(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
        staff = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        order_date = models.DateTimeField(auto_now_add=True)
        expected_delivery_date = models.DateTimeField(null=True, blank=True)
        status = models.CharField(max_length=255)
        payment_method = models.CharField(max_length=255)
        total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.IntegerField()
        unit_price = models.DecimalField(max_digits=10, decimal_places=2)


    from rest_framework import serializers
    from .models import Order, OrderItem

    class OrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = '__all__'

    class OrderItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = '__all__'

    views.py:
    from rest_framework import viewsets
    from .models import Order, OrderItem
    from .serializers import OrderSerializer, OrderItemSerializer

    class OrderViewSet(viewsets.ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerializer

    class OrderItemViewSet(viewsets.ModelViewSet):
        queryset = OrderItem.objects.all()
        serializer_class = OrderItemSerializer


# Quản lý kho và mã vạch
    # models.py
from django.db import models

class Customer(models.Model):
    # ... (các field của model Khách hàng)

class Staff(models.Model):
    # ... (các field của model Nhân viên)

class Product(models.Model):
    # ... (các field của model Sản phẩm)
    barcode = models.CharField(max_length=50, unique=True)  # Thêm trường mã vạch

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20, choices=(('sell', 'Sell'), ('pawn', 'Pawn')))
    created_date = models.DateTimeField(auto_now_add=True)
    # ... (các field khác của model Đơn hàng)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=50)  # Lưu trữ lại mã vạch trong chi tiết
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

# serializers.py
from rest_framework import serializers
from .models import Order, OrderDetail, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'barcode')  # Hiển thị thêm mã vạch

class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Serialization lồng nhau

    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'product', 'barcode', 'quantity', 'unit_price', 'total_price')

class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'staff', 'order_type', 'created_date', 'order_details', 'total_amount', 'payment_method', 'status', 'note')

# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order, OrderDetail, Product
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        # Logic quét mã vạch và thêm sản phẩm vào chi tiết đơn hàng
        barcode = request.data['barcode']
        quantity = request.data['quantity']

        try:
            product = Product.objects.get(barcode=barcode)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found with barcode ' + barcode}, status=400)

        order = self.get_object()
        order_detail = OrderDetail.objects.create(order=order, product=product, barcode=barcode, quantity=quantity)
        order_detail.total_price = order_detail.quantity * order_detail.product.price
        order_detail.save()

        serializer = OrderDetailSerializer(order_detail)
        return Response(serializer.data)

# Lưu ý: Code chưa hoàn thiện các chức năng khác như cập nhật, xóa đơn hàng, thanh toán, 
# quản lý phiếu nhập hàng và tồn kho. Bạn cần xây dựng thêm các API và model cần thiết.
