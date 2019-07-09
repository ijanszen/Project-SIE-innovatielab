from enum import Enum
import requests

class Panels(Enum):
  one = "data = '{"write" : {"command" : "display", "animType" : "static","animData" : \\\u201D7 139 1 0 255 0 0 20 234 1 0 255 255 255 20 2011 0 255 255 255 20 117 1 0 255 255 255 20 200 1 0 255 255 255 20 104 1 0 255 255 255 20 243 1 0 255 255 255 20", "loop":"false"}}'"
  two = "two 2"
  three = "three 3"
  four = "four 4"
  five = "five 5"
  six = "six 6"
  seven = "seven 7"

print(repr(Panels.one))


response = requests.post('http://192.168.3.192:16021/api/v1/8waBfTkcAQAFDFP1CRoaR6u2pg8ScVio/effects', data=data)
