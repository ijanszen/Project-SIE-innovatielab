## alle mogelijke states om percentages te kunnen displayen op de Nanoleaf
## usage animdata: 
state = ''
state1 = '{"write" : {"command" : "display", "animType" : "static","animData" : "7 139 1 0 255 0 0 20 234 1 255 255 255 0 20 201 1 255 255 255 0 20 117 1 255 255 255 0 20 200 1 255 255 255 0 20 104 1 255 255 255 0 20 243 1 255 255 255 0 20", "loop":"false"}}'
state2 = '{"write" : {"command" : "display", "animType" : "static","animData" : "7 139 1 0 255 0 0 20 234 1 0 255 0 0 20 201 1 255 255 255 0 20 117 1 255 255 255 0 20 200 1 255 255 255 0 20 104 1 255 255 255 0 20 243 1 255 255 255 0 20", "loop":"false"}}'
state3 = '{"write" : {"command" : "display", "animType" : "static","animData" : "7 139 1 0 255 0 0 20 234 1 0 255 0 0 20 201 1 0 255 0 0 20 117 1 255 255 255 0 20 200 1 255 255 255 0 20 104 1 255 255 255 0 20 243 1 255 255 255 0 20", "loop":"false"}}'
state4 = '{"write" : {"command" : "display", "animType" : "static","animData" : "7 139 1 0 255 0 0 20 234 1 0 255 0 0 20 201 1 0 255 0 0 20 117 1 0 255 0 0 20 200 1 255 255 255 0 20 104 1 255 255 255 0 20 243 1 255 255 255 0 20", "loop":"false"}}'
state5 = '{"write" : {"command" : "display", "animType" : "static","animData" : "7 139 1 0 255 0 0 20 234 1 0 255 0 0 20 201 1 0 255 0 0 20 117 1 0 255 0 0 20 200 1 0 255 0 0 20 104 1 255 255 255 0 20 243 1 255 255 255 0 20", "loop":"false"}}'
state6 = '{"write" : {"command" : "display", "animType" : "static","animData" : "7 139 1 0 255 0 0 20 234 1 0 255 0 0 20 201 1 0 255 0 0 20 117 1 0 255 0 0 20 200 1 0 255 0 0 20 104 1 0 255 0 0 20 243 1 255 255 255 0 20", "loop":"false"}}'
state7 = '{"write" : {"command" : "display", "animType" : "static","animData" : "7 139 1 0 255 0 0 20 234 1 0 255 0 0 20 201 1 0 255 0 0 20 117 1 0 255 0 0 20 200 1 0 255 0 0 20 104 1 0 255 0 0 20 243 1 0 255 0 0 20", "loop":"false"}}'

def calc_state(p,mini,maxi):
    r=maxi-mini
    #check which state is closest by the percentage
    l= [(r/7*1),(r/7*2),(r/7*3),(r/7*4),(r/7*5),(r/7*6),(r/7*7)]
    calcstate = min(l, key=lambda x:abs(x-p))

    if calcstate == (r/7*1):
        state = state1
        return state, p,"state1", "range:", r
        print(p,"%")
    elif calcstate == (r/7*2):
        state = state2
        return state, p,"state2", "range:", r
        print(p,"%")
    elif calcstate == (r/7*3):
        state = state3
        return state, p,"state3", "range:", r
        print(p,"%")
    elif calcstate == (r/7*4):
        state = state4
        return state, p,"state4", "range:", r
        print(p,"%")
    elif calcstate == (r/7*5):
        state = state5
        return state, p,"state5", "range:", r
        print(p,"%")
    elif calcstate == (r/7*6):
        state = state6
        return state, p,"state6", "range:", r
        print(p,"%")
    elif calcstate == (r/7*7):
        state = state7
        return state, p,"state7", "range:", r
        print(p,"%")


print(calc_state(333,200,1000))
