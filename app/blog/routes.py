from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .. import db
from ..models import Post
from .forms import PostForm
from . import blog  # sử dụng blueprint đã tạo từ __init__.py
import os
from werkzeug.utils import secure_filename

@blog.route('/')
def index():
    print(" Đang xử lý route /")
    query = request.args.get('q')
    if query:
        posts = Post.query.filter(
            (Post.title.ilike(f"%{query}%")) |  # Dùng toán tử | để tìm trong tiêu đề hoặc nội dung
            (Post.content.ilike(f"%{query}%"))
            ).all() #ilike() giúp tìm kiếm không phân biệt hoa/thường
    else:
        posts = Post.query.all()
        
    return render_template('blog/index.html', posts=posts, query=query)

@blog.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    upload_dir = os.path.join('app', 'static', 'uploads')
    os.makedirs(upload_dir, exist_ok=True)
    if form.validate_on_submit():
        image_filename = None
        
        if form.image.data: 
            filename =secure_filename(form.image.data.filename)
            image_path = os.path.join(upload_dir, filename)
            form.image.data.save(image_path)
            image_filename = filename
            
        post = Post(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id,
            image=image_filename  # Lưu tên file hình ảnh vào cơ sở dữ liệu
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    return render_template('blog/create.html', form=form)

@blog.route('/post/<int:post_id>')
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/detail.html', post=post)

@blog.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id:
        flash("Bạn không có quyền chỉnh sửa bài viết này.", "danger")
        return redirect(url_for('blog.detail', post_id=post.id))

    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Bài viết đã được cập nhật.", "success")
        return redirect(url_for('blog.detail', post_id=post.id))

    return render_template('blog/edit.html', form=form, post=post)


@blog.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id:
        flash("Bạn không có quyền xoá bài viết này.", "danger")
        return redirect(url_for('blog.detail', post_id=post.id))

    db.session.delete(post)
    db.session.commit()
    flash("Bài viết đã được xoá.", "info")
    return redirect(url_for('blog.index'))