  # Blueprint: Xử lý bài viết
  
from flask import Blueprint

blog = Blueprint('blog', __name__, url_prefix='/blog')

from . import routes  # Nếu bạn có file routes.py trong thư mục blog