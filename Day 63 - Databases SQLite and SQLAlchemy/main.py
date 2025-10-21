from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template("index.html", books=all_books)

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_rating(book_id):
    with app.app_context():
        book_to_update = db.get_or_404(Book, book_id)
        if request.method == "POST":
            new_rating = request.form["new_rating"]
            book_to_update.rating = float(new_rating)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("edit.html", book=book_to_update)

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    with app.app_context():
        book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return render_template("index.html")
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)

