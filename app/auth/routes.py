from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from . import auth
from .forms import LoginForm, RegisterForm
from .. import db
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('blog.index'))
        else:
            flash('Sai tên đăng nhập hoặc mật khẩu.', 'danger')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Tên người dùng đã tồn tại.', 'warning')
        else:
            hashed_pw = generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_pw)
            db.session.add(new_user)
            db.session.commit()
            flash('Đăng ký thành công. Hãy đăng nhập.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bạn đã đăng xuất.', 'info')
    return redirect(url_for('auth.login'))
