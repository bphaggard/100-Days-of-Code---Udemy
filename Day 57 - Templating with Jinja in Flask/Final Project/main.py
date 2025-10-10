import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    response_blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response_blog.raise_for_status()
    blog_data = response_blog.json()
    return render_template("index.html", posts=blog_data)

@app.route("/post/<int:post_id>")
def post_page(post_id):
    response_blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response_blog.raise_for_status()
    blog_data = response_blog.json()
    post = next((item for item in blog_data if item['id'] == post_id), None)
    if post:
        return render_template("post.html", posts=post)
    else:
        return "Post not found"

if __name__ == "__main__":
    app.run(debug=True)
