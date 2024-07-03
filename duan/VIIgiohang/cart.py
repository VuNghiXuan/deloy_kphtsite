from IIIquanlykho.models import NhapHang
from hethong.models import UserProfile
class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        self.request = request

        # Lấy session key hiện tại nếu nó tồn tại
        cart = self.session.get('session_key')

        # Nếu mới chưa có thì tạo mới, tạo số lượng là 1
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Tạo ra cart is available trên tất cả các trang
        self.cart = cart
    
    # Add cart from database
    def db_add(self, san_pham, so_luong):
        san_pham_id = str(san_pham)
        so_luong = str(so_luong)

        # Logic
        if san_pham_id in self.cart:
            pass
        else:
            # self.cart[san_pham_id]= {'gia_ban':str(san_pham.gia_ban_mon)}
            self.cart[san_pham_id]= int(so_luong)
            self.session.modified = True
        
        # Deal with logout user
        if self.request.user.is_authenticated:
            # Get the current_user profile
            current_user = UserProfile.objects.filter(user__id=self.request.user.id)
            # {'3':2, '5': 3}
            carty = str(self.cart)
            # print("------------------------carty trc", carty)

            carty = carty.replace("\'", "\"")
            # print("------------------------carty sau", carty)

            # SAve cart vào UserProfile
            current_user.update(old_cart=str(carty))


    def add(self, san_pham, so_luong): #
        san_pham_id = str(san_pham.id)
        so_luong = str(so_luong)

        # Logic
        if san_pham_id in self.cart:
            pass
        else:
            # self.cart[san_pham_id]= {'gia_ban':str(san_pham.gia_ban_mon)}
            self.cart[san_pham_id]= int(so_luong)
            self.session.modified = True
        
        # Deal with logout user
        if self.request.user.is_authenticated:
            # Get the current_user profile
            current_user = UserProfile.objects.filter(user__id=self.request.user.id)
            # {'3':2, '5': 3}
            carty = str(self.cart)
            # print("------------------------carty trc", carty)

            carty = carty.replace("\'", "\"")
            # print("------------------------carty sau", carty)

            # SAve cart vào UserProfile
            current_user.update(old_cart=str(carty))

    def __len__(self):
        return len(self.cart)

    # Lấy tên sản phẩm
    def get_prods(self):
        # Get ids from cart
        san_pham_ids = self.cart.keys()
        # Use ids lookup prods in database model
        san_pham = NhapHang.objects.filter(id__in = san_pham_ids)
        return san_pham
    
    # Lấy số lượng cần mua từ người dùng
    def get_quants(self):
        so_luong = self.cart
        # print("-------------------get_quants", so_luong)
        return so_luong
    
    # Update số lượng thay đổi theo danh mục giỏ hàng
    def update(self, san_pham, so_luong): #
        san_pham_id = str(san_pham) #str(san_pham.id)
        so_luong = str(so_luong)

        # cart : {'4':3, "2":5}
        outcart = self.cart
        # Update dictionary/cart
        outcart[san_pham_id] = so_luong
        self.session.modified = True

        # Deal with logout user
        if self.request.user.is_authenticated:
            # Get the current_user profile
            current_user = UserProfile.objects.filter(user__id=self.request.user.id)
            # {'3':2, '5': 3}
            carty = str(self.cart)
            # print("------------------------carty trc", carty)

            carty = carty.replace("\'", "\"")
            # print("------------------------carty sau", carty)

            # SAve cart vào UserProfile
            current_user.update(old_cart=str(carty))
            
        things = self.cart

        return things

    # Xóa sản phẩm ra khỏi giỏ hàng
    def delete(self, san_pham):
        # cart : {'4':3, "2":5}
        san_pham_id = str(san_pham) 
        # delte
        if san_pham_id in self.cart:
            del self.cart[san_pham_id]
        self.session.modified = True

        # Deal with logout user
        if self.request.user.is_authenticated:
            # Get the current_user profile
            current_user = UserProfile.objects.filter(user__id=self.request.user.id)
            # {'3':2, '5': 3}
            carty = str(self.cart)
            # print("------------------------carty trc", carty)

            carty = carty.replace("\'", "\"")
            # print("------------------------carty sau", carty)

            # SAve cart vào UserProfile
            current_user.update(old_cart=str(carty))

    
    # Tính tổng giá trị giỏ hàng
    def total(self):
        san_pham_ids = self.cart.keys()
        san_pham = NhapHang.objects.filter(id__in = san_pham_ids)

        tong_gia_tri = 0

        # Tìm số lượng
        # {'40': 1, '42': 1, '45': 3}
        dic_gio_hang = self.cart
        
        # print('--------------------- san_pham_ids', san_pham_ids)
        # print('--------------------- san_pham', san_pham)
        # print('--------------------- dic_gio_hang', dic_gio_hang)
        for key, val in dic_gio_hang.items():
            key = int(key)
            for sp in san_pham:
                # print('--------------------- sp.id', sp.id)
                if key == sp.id:
                    so_luong = int(val)
                    tong_gia_tri += sp.gia_ban_mon * so_luong
            
        #             print(f'---------------------sp.gia_ban_mon', sp.gia_ban_mon)
        #             print(f'---------------------so_luong', so_luong)
        # print(f'---------------------tong_gia_tri', tong_gia_tri)

        return tong_gia_tri