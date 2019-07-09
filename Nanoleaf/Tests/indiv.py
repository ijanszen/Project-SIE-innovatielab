from nanoleaf import Aurora

my_aurora = Aurora("192.168.3.192", "8waBfTkcAQAFDFP1CRoaR6u2pg8ScVio")
effect_data = {
"command" : "display",
"animType": "static",
"animData": '2 139 1 255 255 255 1 20 200 1 255 255 255 1 20',
"loop": "false"}

my_aurora.effect_set_raw(effect_data)