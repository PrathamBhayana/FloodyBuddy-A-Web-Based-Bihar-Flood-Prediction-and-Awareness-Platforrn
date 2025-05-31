from flask import Flask, render_template, request, redirect
import pickle
import numpy as np
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure multiple databases using SQLALCHEMY_BINDS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'  # Default database
app.config['SQLALCHEMY_BINDS'] = {
    'flood': 'sqlite:///flood_data.db'  # Bind for flood data
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    reason = db.Column(db.Text, nullable=False)

# Flood data model
class FloodData(db.Model):
    __bind_key__ = 'flood'  # Specify the bind key for this model
    id = db.Column(db.Integer, primary_key=True)
    river_name = db.Column(db.String(50), nullable=False)
    water_level = db.Column(db.Float, nullable=False)
    rainfall_level = db.Column(db.Float, nullable=False)
    flood_prediction = db.Column(db.String(10), nullable=False)  # "Yes" or "No"
    affected_area = db.Column(db.String(50), nullable=True)  # Allow NULL values
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

river_name_encoding = {
    'Bagmati': 0,
    'Burhi Gandak': 1,
    'Gandak': 2,
    'Ganga': 3,
    'Kamla Balan': 4,
    'Kosi': 5,
    'Mahananda': 6,
    'Phalgu': 7,
    'Punpun': 8,
    'Sone': 9
}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    phone = request.form['phone']
    reason = request.form['reason']

    new_contact = Contact(name=name, phone=phone, reason=reason)
    db.session.add(new_contact)
    db.session.commit()

    return redirect('/contact')

@app.route('/after', methods=['POST'])
def after():
    model = pickle.load(open('flood.pkl', 'rb'))

    river_name_input = request.form['a']
    river_name = river_name_encoding.get(river_name_input, -1)

    if river_name == -1:
        return render_template('error.html', message="Invalid river name entered.")

    water_level = float(request.form['b'])
    rainfall_level = float(request.form['c'])

    input_data = np.array([[river_name, water_level, rainfall_level]])
    
    prediction = model.predict(input_data)
    flood_prediction = "Yes" if prediction[0][0] == 1 else "No"
    affected_area = prediction[0][1]

    label_mappings = {
        "Part of Bihar Affected": {
            0: "Central Bihar",
            1: "East Bihar",
            2: "North Bihar",
            3: "South Bihar",
            4: "West Bihar"
        }
    }
    # Set affected_area_decoded to None if no flood is predicted
    affected_area_decoded = (
        label_mappings["Part of Bihar Affected"].get(affected_area, "Unknown")
        if flood_prediction == "Yes"
        else None
    )

    # Save flood prediction data to the flood database
    new_flood_data = FloodData(
        river_name=river_name_input,
        water_level=water_level,
        rainfall_level=rainfall_level,
        flood_prediction=flood_prediction,
        affected_area=affected_area_decoded
    )
    db.session.add(new_flood_data)  # Use the single `db` instance
    db.session.commit()

    return render_template('after.html', data=1 if flood_prediction == "Yes" else 0, affected=affected_area_decoded)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables for both databases
    app.run(debug=True)