from flask import render_template, request, Blueprint
import markdown

from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3) 
    contents = {}
    for post in posts.items:
        contents[post.id] = markdown.markdown(post.content)
    return render_template('home.html', posts=posts, contents=contents)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
