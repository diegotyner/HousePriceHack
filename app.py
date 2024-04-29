from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)
app.config
app.config['SECRET_KEY'] = 'mysecret'

agenda = ["learn flask", 'setup venv', 'build an app']

class HousingPredictorForm(FlaskForm):
    longitude = StringField("Longitude")
    latitude = StringField("Latitude")
    age = StringField("Age of House")
    rooms = StringField("Total Rooms")
    bedrooms = StringField("Bedrooms")
    population = StringField("Population of Block")
    households = StringField("Households in Block")
    income = StringField("Median Income of Block")
    ocean = SelectField('Programming Language', choices=[ ('<1', '1H Ocean'), ('Inland', 'Inland'), ('Near Ocean', 'Near Ocean'), ('Near Bay', 'Near Bay'), ('Island', 'Island') ])



    submit = SubmitField("Check House")

@app.route('/', methods=["GET", "POST"])
def index():
    if 'longitude' in request.form:
        agenda.append(request.form['longitude'])
    return render_template('index.html', todos=agenda, template_form=HousingPredictorForm()) # template gets var todos, and its equal to todos




