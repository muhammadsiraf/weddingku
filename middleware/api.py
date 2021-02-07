import flask 
import pdfkit
from flask import Flask, jsonify, request, redirect, send_file
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
    nama = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    afiliasi = request.form['afiliasi']
    konfirmasi = request.form['konfirmasi']


    data = {
        'nama': nama,
        'email': email,
        'phone': phone,
        'afiliasi': afiliasi,
        'konfirmasi': konfirmasi,
    }

    result = firebase.post('Register', data)
    return result

@app.route('/registered/<id>/', methods=['GET'])
def get_detail(id):
    result = firebase.get('/Register/'+id+'/', '')
    nama = result['nama']
    map_link = "https://tlgur.com/d/GYwWJqm4"
    doa = "Dengan Memohon Rahmat Allah SWT Kami Bermaksud Menyelenggarakan Resepsi Pernikahan Putra-Putri Kami"
    alamat_tujuan = "Jalan Tirtohudan Raya no II, Kediri"
    tanggal_resepsi = "Minggu, 9 Desember 2021"
    pukul_resepsi = "10.00-selesai"
    tanggal_ijab = "Jumat, 7 Desember 2021"
    pukul_ijab = "08.00-10.00"
    harapan = "Kehadiran Serta Doa Restu Bapak/Ibu/Saudara/i merupakan suatu kehormatan & kebahagiaan bagi kami"

    data = {
        'nama':nama,
        'doa':doa,
        'alamat_tujuan':alamat_tujuan,
        'tanggal_resepsi':tanggal_resepsi,
        'pukul_resepsi':pukul_resepsi,
        'tanggal_ijab':tanggal_ijab,
        'pukul_ijab':pukul_ijab,
        'harapan':harapan,
        'map_link':map_link
    }

    return jsonify(data)

@app.route('/registered/<id>/invitation/', methods=['GET'])
def get_invitation(id):

    data_pdf = pdfkit.from_url(
        'https://tlgur.com/d/GWNWEab8', 'micro.pdf')
    return send_file(data_pdf)

app.run()
