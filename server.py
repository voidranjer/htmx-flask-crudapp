from flask import Flask, render_template, url_for

app = Flask(__name__)

db = {
  "users": [
    {
      "id": 1,
      "username": "john_doe",
      "email": "john@example.com",
      "posts": [1, 2]
    },
    {
      "id": 2,
      "username": "jane_smith",
      "email": "jane@example.com",
      "posts": [3]
    }
  ],
  "posts": [
    {
      "id": 1,
      "userId": 1,
      "title": "My first post",
      "content": "This is the content of my first post.",
      "comments": [1, 2]
    },
    {
      "id": 2,
      "userId": 1,
      "title": "Another post",
      "content": "This is another post I created.",
      "comments": [3]
    },
    {
      "id": 3,
      "userId": 2,
      "title": "Jane's post",
      "content": "Hello, I'm Jane. This is my post.",
      "comments": []
    }
  ],
  "comments": [
    {
      "id": 1,
      "userId": 2,
      "postId": 1,
      "text": "Great post, John!"
    },
    {
      "id": 2,
      "userId": 1,
      "postId": 1,
      "text": "Thanks, Jane!"
    },
    {
      "id": 3,
      "userId": 2,
      "postId": 2,
      "text": "Nice one, John."
    }
  ]
}

@app.context_processor
def utility_processor():
    def static_url(filename):
        return url_for('static', filename=filename)
    return dict(static_url=static_url, db=db)

@app.route("/")
def home():
    urls = {'favicon': url_for('static', filename='favicon.ico')}
    return render_template('index.html', urls=urls)

@app.route("/posts")
def posts():
    return render_template('posts/index.html')
