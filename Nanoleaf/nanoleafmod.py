import requests
import json
# Parsing the effects.json file to variable data
with open('effects.json') as json_file:
            data = json.load(json_file)
# Define variables
health = ''
state = ''

class NanoleafState():
    def calc_percentage(self,mini,maxi,d):
        """Calculate percentage for data between range
        Usage: calc_percentage(min,max,data)
        """
        p = ((d - mini)*100)/(maxi - mini)
        return p
    
    def calc_health(self,health_id):
        """Check which healthstate from healthid and returning healthstate
        Usage: calc_health(health_id)
        """
        h = ''
        if health_id == 0:
            h = str(data['health'][0])
            health = '{"write" : {"command" : "display", "animType" : "static","animData" : "'+h+'", "loop":"false"}}'
            return health
        elif health_id == 1:
            h = str(data['health'][1])
            health = '{"write" : {"command" : "display", "animType" : "static","animData" : "'+h+'", "loop":"false"}}'
            return health
        elif health_id == 2:
            h = str(data['health'][2])
            health = '{"write" : {"command" : "display", "animType" : "static","animData" : "'+h+'", "loop":"false"}}'
            return health
        elif health_id == 3:
            h = str(data['health'][3])
            health = '{"write" : {"command" : "display", "animType" : "static","animData" : "'+h+'", "loop":"false"}}'
            return health
        elif health_id == 4:
            h = str(data['health'][4])
            health = '{"write" : {"command" : "display", "animType" : "static","animData" : "'+h+'", "loop":"false"}}'
            return health

    def calc_state(self,p):
        """Check which state is closest by the percentage and returning statedata
        Usage: calc_state(percentage)
        """
        l= [(100/7*1),(100/7*2),(100/7*3),(100/7*4),(100/7*5),(100/7*6),(100/7*7)]
        calcstate = min(l, key=lambda x:abs(x-p))
        s = ''
        if calcstate == l[0]:
            s = str(data['state'][0])
            state = '{"write":{"animData":"'+s+'","animType":"custom","command":"display","loop":false}}'
            return state
        elif calcstate == l[1]:
            s = str(data['state'][1])
            state = '{"write":{"animData":"'+s+'","animType":"custom","command":"display","loop":false}}'
            return state
        elif calcstate == l[2]:
            s = str(data['state'][2])
            state = '{"write":{"animData":"'+s+'","animType":"custom","command":"display","loop":false}}'
            return state
        elif calcstate == l[3]:
            s = str(data['state'][3])
            state = '{"write":{"animData":"'+s+'","animType":"custom","command":"display","loop":false}}'
            return state
        elif calcstate == l[4]:
            s = str(data['state'][4])
            state = '{"write":{"animData":"'+s+'","animType":"custom","command":"display","loop":false}}'
            return state
        elif calcstate == l[5]:
            s = str(data['state'][5])
            state = '{"write":{"animData":"'+s+'","animType":"custom","command":"display","loop":false}}'
            return state
        elif calcstate == l[6]:
            s = str(data['state'][6])
            state = '{"write":{"animData":"'+s+'","animType":"custom","command":"display","loop":false}}'
            return state

    def send_health(self,health):
        ## RUN OFFICIAL NANOLEAF RESTAPI HEALTH
        requests.put('http://192.168.3.192:16021/api/v1/8waBfTkcAQAFDFP1CRoaR6u2pg8ScVio/effects',data=health)

    def send_state(self,state):
        ## RUN RESTAPI PERCENTAGE
        requests.put('http://192.168.3.192:16021/api/v1/8waBfTkcAQAFDFP1CRoaR6u2pg8ScVio/effects',data=state)