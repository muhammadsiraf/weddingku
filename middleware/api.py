import flask
from flask import Flask, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://wedding-invitation-52b05-default-rtdb.firebaseio.com/', None)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    nama = StringField('Nama', validators=[DataRequired()])
    relation = StringField('Relasi', validators=[DataRequired()])
    handphone = StringField('No Handphone', validators=[DataRequired()])
    submit = SubmitField('Daftar')

@app.route('/', methods=['GET'])
def home():
    return "<h1>Good Luck BB</h1>"

@app.route('/registered/', methods=['GET'])
def registered():
    result = firebase.get('/Register/', '')
    return result


@app.route('/registered/', methods=['POST'])
def registered_create():
    fnama = request.form['fname']
    lnama = request.form['lname']

    result = firebase.post('Register', request_data)
    return result

app.run()
