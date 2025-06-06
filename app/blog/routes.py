from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .. import db
from ..models import Post
from .forms import PostForm

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
    query = request.args.get('q')
    if query:
        posts = Post.query.filter(Post.title.ilike(f"%{query}%")).all()
    else:
        posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)

@blog.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    return render_template('blog/create.html', form=form)

@blog.route('/post/<int:post_id>')
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/detail.html', post=post)
