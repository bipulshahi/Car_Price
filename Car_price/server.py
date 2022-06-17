from flask import Flask,request,jsonify
import util

app = Flask(__name__)

@app.route('/get_column_names')
def get_column_names():
    response = {'Features' : util.get_feature_names()}
    return response


@app.route('/predict_price',methods=['POST'])
def predict_price():
    age = float(request.form['age'])
    kms = float(request.form['kms'])
    mlg = float(request.form['mileage'])
    eng = float(request.form['engine'])
    pwr = float(request.form['power'])
    sts = float(request.form['seats'])
    loc = request.form['location']
    fu_type = request.form['fuel_type']
    trans = request.form['transmission']
    owner = request.form['owner']
    cname = request.form['car_name']


    price = util.predict_car_prices(age,kms,mlg,eng,pwr,sts,loc,
                                    fu_type,trans,owner,cname)  
    
    response = jsonify({'Estimated_Price':price})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run()
