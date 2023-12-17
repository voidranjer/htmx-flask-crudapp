from flask import Flask, render_template, request
from .db import sample_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/posts")
def posts():
    posts = sample_db.get_posts()
    return render_template('posts/index.html', posts=posts)

@app.route("/post/<string:post_id>")
def show_post(post_id):
    post = sample_db.get_post(post_id)
    return render_template('posts/_partials/show.html', post=post)

@app.route("/posts/edit/<string:post_id>", methods=['GET', 'PUT'])
def edit_post(post_id):
    if request.method == 'PUT':
        title = request.form.get('title')
        content = request.form.get('content')
        sample_db.update_post(post_id, title=title, content=content)
        return show_post(post_id)

    # Default: GET
    post = sample_db.get_post(post_id)
    return render_template('posts/_partials/edit.html', post=post)

@app.route("/post/<string:post_id>/delete", methods=['DELETE'])
def delete_post(post_id):
    sample_db.delete_post(post_id)
    return ""