from unicodedata import name
from flask import Flask, request, jsonify, render_template
import json
import joblib

app = Flask(__name__)

df2 = joblib.load('df2.joblib')
model=joblib.load('save_model/model.pkl')
scaler=joblib.load('save_model/scaler.pkl')

def transfor_to_onehot(df, feat, value):
    vals = sorted(list(df[feat].unique()))
    del vals[0]
    make_onehot = []
    for val in vals:
        if val == value:
            make_onehot.append(1)
        else:
            make_onehot.append(0)
    return make_onehot




@app.route('/predict', methods=['POST'])
def predict():
      cars=[]
      cars.append(request.json['Km'])
      cars.append(request.json['Leather seats'])
      cars.append(request.json['Closing mirrors'])
      cars.append(request.json['Intelligent parking system'])
      cars.append(request.json['Sunroof'])
      cars.append(request.json['Fabric brushes'])
      cars.append(request.json['Air Conditioning'])
      cars.append(request.json['Power Steering'])
      cars.append(request.json['Remote Keyless'])
      cars.append(request.json['Electric mirrors'])
      cars.append(request.json['Front Power Windows'])
      cars.append(request.json['Back Power Windows'])
      cars.append(request.json['Tinted Glass'])
      cars.append(request.json['CD Player'])
      cars.append(request.json['DVD Player'])
      cars.append(request.json['Bluetooth'])
      cars.append(request.json['Multifunction'])
      cars.append(request.json['Cassette Radio'])
      cars.append(request.json['AUX'])
      cars.append(request.json['CD Changer'])
      cars.append(request.json['USB Port'])
      cars.append(request.json['Anti - theft System'])
      cars.append(request.json['Side Airbag'])
      cars.append(request.json['ABS'])
      cars.append(request.json['EPS'])
      cars.append(request.json['EBD'])
      cars.append(request.json['ESP'])
      cars.append(request.json['Sensors'])
      cars.append(request.json['Rear sensors'])
      cars.append(request.json['Driver Airbag'])
      cars.append(request.json['Passenger Airbag'])
      cars.append(request.json['Front sensors'])
      cars.append(request.json['Alloy wheels'])
      cars.append(request.json['Rear camera'])
      cars.append(request.json['GPS'])
      cars.append(request.json['Fog light'])
      cars.append(request.json['Rear spoiler'])
      cars.append(request.json['Cruise control'])
      cars.append(request.json['Power Seats'])
      cars.append(request.json['Central lock'])
      cars.append(request.json['Alarm'])

      cars += transfor_to_onehot(df2, 'Make', request.json['Make'])
      cars += transfor_to_onehot(df2, 'Model', request.json['Model'])
      cars += transfor_to_onehot(df2, 'Used since', request.json['Used since'])
      cars += transfor_to_onehot(df2, 'Transmission', request.json['Transmission'])
      cars += transfor_to_onehot(df2, 'City', request.json['City'])
      cars += transfor_to_onehot(df2, 'Color', request.json['Color'])
      cars += transfor_to_onehot(df2, 'Fuel', request.json['Fuel'])


      
      cars=scaler.transform([cars])
      price=int(model.predict(cars)[0])
      return jsonify({'predicted_price':price})


if __name__ == '__main__':
      app.run(debug=True)   