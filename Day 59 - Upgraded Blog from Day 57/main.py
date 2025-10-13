import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    response_blog = requests.get("https://api.npoint.io/8a2a9787f98be1677ea5")
    response_blog.raise_for_status()
    blog_data = response_blog.json()
    return render_template("index.html", posts=blog_data)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def post_page(post_id):
    response_blog = requests.get("https://api.npoint.io/8a2a9787f98be1677ea5")
    response_blog.raise_for_status()
    blog_data = response_blog.json()
    post = next((item for item in blog_data if item['id'] == post_id), None)
    if post:
        return render_template("post.html", posts=post)
    else:
        return "Post not found"

if __name__ == "__main__":
    app.run(debug=True)