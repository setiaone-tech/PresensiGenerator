import json
from flask import Flask, render_template, jsonify, request
import datetime

app = Flask(__name__)
app.secret_key = "generate-presensi"

@app.route('/', methods=['GET'])
def index():
    with open('matkul.json') as f:
        data = list(json.load(f))
    
    waktu_saat_ini = datetime.datetime.now()

    #Untuk menyesuaikan waktu Indonesia Barat
    waktu_indonesia_barat = waktu_saat_ini - datetime.timedelta(hours=7)

    #Untuk menampilkan hasil
    waktu = waktu_indonesia_barat.date()
        
    return render_template("index.html",data=data, waktu=waktu)
    

if '__name__' == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
