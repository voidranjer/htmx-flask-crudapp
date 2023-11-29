#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Response
from .db import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts=db.get_posts())

@app.route('/post/show')
def show_post():
    post_id = request.args.get('id')
    post = db.get_post(post_id)
    return render_template('_partials/show.html', post=post)

@app.route('/post/edit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def edit_post():
    post_id = request.args.get('id') or request.form.get('id')
    post = db.get_post(post_id)

    if request.method == "GET":
        return render_template('_partials/edit.html', post=post)

    elif request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        
        post = db.add_post(title, content)
        resp = Response(render_template('_partials/show.html', post=post))
        resp.headers['HX-Trigger'] = "resetForm"

        return resp

    elif request.method == "PUT":
        title = request.form.get('title')
        content = request.form.get('content')
        post = db.set_post(post_id, title, content)
        return render_template('_partials/show.html', post=post)

    elif request.method == "DELETE":
        db.delete_post(post_id)
        return ""

@app.route('/post/validate', methods=['POST'])
def validate_post():
    title = request.form.get('title')
    error = 'Can\'t have digits in the title!' if any(char.isdigit() for char in title) else None
    return render_template('_partials/validate.html', title=title, error=error)