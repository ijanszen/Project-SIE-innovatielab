from nanoleaf import Aurora



my_aurora = Aurora("192.168.3.192", "8waBfTkcAQAFDFP1CRoaR6u2pg8ScVio")
my_aurora.effect = "test"
#my_aurora.on = True
my_aurora.brightness = 100
#my_aurora.rgb = 255

location = my_aurora.panel_positions
print(location)
print("---------------")
print(my_aurora.effects_list)
my_aurora.on = True