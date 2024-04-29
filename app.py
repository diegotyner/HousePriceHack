from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import pickle

app = Flask(__name__)
app.config
app.config['SECRET_KEY'] = 'mysecret'

# agenda = ["learn flask", 'setup venv', 'build an app']
holder = "Please enter a value:"
filename = "Pickled_Model"

class HousingPredictorForm(FlaskForm):
    longitude = StringField("Longitude")
    latitude = StringField("Latitude")
    age = StringField("Age of House")
    rooms = StringField("Total Rooms")
    bedrooms = StringField("Bedrooms")
    population = StringField("Population of Block")
    households = StringField("Households in Block")
    income = StringField("Median Income of Block")
    ocean = SelectField('Programming Language', choices=[ ('<1', '<1H Ocean'), ('Inland', 'Inland'), ('Near Ocean', 'Near Ocean'), ('Near Bay', 'Near Bay'), ('Island', 'Island') ])


    submit = SubmitField("Check House")



@app.route('/', methods=["GET", "POST"])
def index():
    # if request.form:
    #     loaded_model = pickle.load(open(filename), 'rb')
    #     loaded_model.predict([
    #         request.form.longitude,
    #         request.form.latitude,
    #         request.form.age,
    #         request.form.rooms,
    #         request.form.bedrooms,
    #         request.form.population,
    #         request.form.households,
    #         request.form.income,
    #         request.form.ocean
    #         ])
        # agenda.append(request.form['longitude'])
    return render_template('index.html', estimate=holder, template_form=HousingPredictorForm()) # template gets var todos, and its equal to todos




