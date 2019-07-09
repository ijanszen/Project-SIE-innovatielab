#!/usr/bin/python
# Import all functions
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from nanoleafmod import *

# Define variables
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

# Below all arguments that can be included in the defined URI's
# Example curl:
# curl http://192.168.37.1:5000/api/humidity -d "data=80" -d "ts=1001313" -d "ispublic=true" -X PUT
parser.add_argument('data')
parser.add_argument('ts')
parser.add_argument('ispublic')

class DisplayHumidity(Resource):
    # Display Humidity on the Nanoleaf
    def put(self):
        args = parser.parse_args()
        d = args['data']
        try:
            displaystate = NanoleafState().calc_state(int(d))
            NanoleafState().send_state(displaystate)
            return {'status': 'ok'}
        except:
            return {'status': 'failed'}

class DisplayHealth(Resource):
    # Display Healthstate on the Nanoleaf
    def put(self):
        args = parser.parse_args()
        d = args['data']
        try:
            displayhealth = NanoleafState().calc_health(int(d))
            NanoleafState().send_health(displayhealth)
            return {'status': 'ok'}
        except:
            return {'status': 'failed'}

class DisplayNoise(Resource):
    # Display Noise on the Nanoleaf
    def put(self):
        args = parser.parse_args()
        d = args['data']
        try:
            displaystate = NanoleafState().calc_state(int(d))
            NanoleafState().send_state(displaystate)
            return {'status': 'ok'}
        except:
            return {'status': 'failed'}

class DisplayWifi(Resource):
    # Display Wifi on the Nanoleaf
    def put(self):
        args = parser.parse_args()
        d = args['data']
        try:
            displaystate = NanoleafState().calc_state(int(d))
            NanoleafState().send_state(displaystate)
            return {'status': 'ok'}
        except:
            return {'status': 'failed'}

class DisplayCo2(Resource):
    # Display Co2 on the Nanoleaf
    def put(self):
        args = parser.parse_args()
        d = args['data']
        try:
            p = NanoleafState().calc_percentage(350,1500,int(d))
            displaystate = NanoleafState().calc_state(int(p))
            NanoleafState().send_state(displaystate)
            return {'status': 'ok'}
        except:
            return {'status': 'failed'}

class DisplayPressure(Resource):
    # Display Pressure on the Nanoleaf
    def put(self):
        args = parser.parse_args()
        d = args['data']
        try:
            p = NanoleafState().calc_percentage(940,1060,int(d))
            displaystate = NanoleafState().calc_state(int(p))
            NanoleafState().send_state(displaystate)
            return {'status': 'ok'}
        except:
            return {'status': 'failed'}

class DisplayTemperature(Resource):
    # Display Temperature on the Nanoleaf
    def put(self):
        args = parser.parse_args()
        d = args['data']
        print(d)
        try:
            p = NanoleafState().calc_percentage(15,30,float(d))
            displaystate = NanoleafState().calc_state(float(p))
            NanoleafState().send_state(displaystate)
            return {'status': 'ok'}
        except:
            return {'status': 'failed'}

##Define all API URI's
api.add_resource(DisplayHumidity, '/api/humidity')
api.add_resource(DisplayHealth, '/api/health')
api.add_resource(DisplayNoise, '/api/noise')
api.add_resource(DisplayWifi, '/api/wifi')
api.add_resource(DisplayCo2, '/api/co2')
api.add_resource(DisplayPressure, '/api/pressure')
api.add_resource(DisplayTemperature, '/api/temperature')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')