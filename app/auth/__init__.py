# Blueprint: Xử lý đăng nhập / đăng ký

from flask import Blueprint

# Khởi tạo Blueprint cho module auth
auth = Blueprint('auth', __name__, url_prefix='/auth')

# Import các routes để đăng ký vào blueprint (bắt buộc phải ở sau khi tạo Blueprint)
from . import routes
