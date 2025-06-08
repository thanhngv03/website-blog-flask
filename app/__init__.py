from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Khởi tạo đối tượng DB và LoginManager toàn cục
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print("Cấu hình ứng dụng đã được nạp từ Config")
    # Khởi tạo db và login manager với app
    db.init_app(app)
    login_manager.init_app(app)

    # Đăng ký blueprint đăng nhập/đăng ký
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    print("đã đăng ký blueprint")
     
    # Đăng ký blueprint blog (trang chủ không có prefix)
    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)
    print("✅ đăng ký blueprint blog")

    return app
