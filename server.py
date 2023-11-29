#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, abort, Response
from random import randint

app = Flask(__name__)

db = {
  "posts": [
    {
      "id": 1,
      "userId": 1,
      "title": "HTMX is awesome!",
      "content": "I just learned about HTMX and it's awesome!",
      "comments": [1, 2]
    },
    {
      "id": 2,
      "userId": 1,
      "title": "This post is generated by ChatGPT",
      "content": "I'm a robot. I'm writing this post using ChatGPT.",
      "comments": [3]
    },
    {
      "id": 3,
      "userId": 2,
      "title": "I'm tired...",
      "content": "It's 3am and I want to sleep.",
      "comments": []
    }
  ]
}


def post_exists(raw_id):
  if (not raw_id):
    return False
  post_id = int(raw_id)
  for post in db['posts']:
    if post['id'] == post_id:
      return True
  return False

def get_post(raw_id):
  post_id = int(raw_id)
  for post in db['posts']:
    if post['id'] == post_id:
      return post

def delete_post(raw_id):
  post_id = int(raw_id)
  db['posts'] = [ post for post in db['posts'] if post['id'] != post_id ]

@app.context_processor
def utility_processor():

  def static_url(filename):
    return url_for('static', filename=filename)

  def nav_active(endpoint):
    return ('active' if request.endpoint == endpoint else '')

  return dict(static_url=static_url, db=db, nav_active=nav_active)


@app.route('/')
def home():
  return render_template('home/index.html')


@app.route('/posts', methods=['GET'])
def posts():
  raw_id = request.args.get('id')

  if (not raw_id):
    return render_template('posts/index.html')

@app.route('/posts/show', methods=['GET'])
def show_post():
  raw_id = request.args.get('id')
  if not post_exists(raw_id):
    abort(404)
  return render_template('posts/_show.html', post=get_post(raw_id))

@app.route('/posts/edit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def edit_post():
  raw_id = request.args.get('id') or request.form.get('id')

  # Should only run for non-POST requests
  if request.method != "POST":
    if not post_exists(raw_id):
      abort(404)

  if request.method == "GET":
    post = get_post(raw_id)
    return render_template('posts/_edit.html', post=post)

  elif request.method == "POST":
    title = request.form.get('title')
    content = request.form.get('content')
    post_id = randint(1000, 9999)
    post = {
      'id': post_id,
      'userId': 1,
      'title': title,
      'content': content,
      'comments': [],
    }
    db['posts'].insert(0, post)
    
    resp = Response(render_template('posts/_show.html', post=post))
    resp.headers['HX-Trigger'] = "resetForm"

    return resp

  elif request.method == "PUT":
    title = request.form.get('title')
    content = request.form.get('content')
    
    post = get_post(raw_id)
    post['title'] = title
    post['content'] = content

    return render_template('posts/_show.html', post=post)

  elif request.method == "DELETE":
    delete_post(raw_id)
    return ""
    # return "<p class='text-danger'>Post deleted successfully</p>"

@app.route('/posts/new/validate', methods=['POST'])
def validate_post_title():  
  title = request.form.get('title')
  error = 'Can\'t have digits in the title!' if any(char.isdigit() for char in title) else None
  return render_template('posts/_validateTitle.html', title=title, error=error)

@app.route('/posts/new')
def new_post():
  return render_template('home/index.html')

# Custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return '404 Not Found', 404