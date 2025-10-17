from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating',
                         choices=[('0', '✘'), ('1', '☕️'), ('2', '☕️☕️'), ('3', '☕️☕️☕️'), ('4', '☕️☕️☕️☕️'), ('5', '☕️☕️☕️☕️☕️')],
                         validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating',
                       choices=[('0','✘'), ('1', '💪'), ('2', '💪💪'), ('3', '💪💪💪'), ('4', '💪💪💪💪'), ('5', '💪💪💪💪💪')],
                       validators=[DataRequired()])
    power = SelectField('Power Socket Availability',
                        choices=[('0', '✘'), ('1', '🔌'), ('2', '🔌🔌'), ('3', '🔌🔌🔌'), ('4', '🔌🔌🔌🔌'), ('5', '🔌🔌🔌🔌🔌')],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        try:
            with open('cafe-data.csv', 'rb+') as f:
                f.seek(-1, 2)
                if f.read(1) != b'\n':
                    f.write(b'\n')
        except OSError:
            pass

        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.opening.data,
                form.closing.data,
                form.rating.data,
                form.wifi.data,
                form.power.data
            ])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
