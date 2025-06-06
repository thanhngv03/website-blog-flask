  # Blueprint: Xử lý bài viết
  
from flask import Blueprint

blog = Blueprint('blog', __name__, url_prefix='/')

from . import routes