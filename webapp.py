import picoweb
import utils as u
import utime
import machine
import ucollections as uc
from collections import OrderedDict 
app = picoweb.WebApp(None)

pin1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
pin2 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
pin3 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
pin4 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

# Car = {'t1'=[lap1_time,lap2_time,lap3_time,...],'t2'=[lap1_time,lap2_time,lap3_time,...]}
car1 = OrderedDict()
car2 = OrderedDict()
car3 = OrderedDict()
car4 = OrderedDict()

car1_name=""
car2_name=""
car3_name=""
car4_name=""

car1_timelap = 0
car2_timelap = 0
car3_timelap = 0
car4_timelap = 0

car1_laps = 0
car2_laps = 0
car3_laps = 0
car4_laps = 0


laps = 1
tracks = 4
gp_ready = False

def resetTimeLaps():
    global car1_timelap
    global car2_timelap
    global car3_timelap
    global car4_timelap
    
    global car1_laps
    global car2_laps
    global car3_laps
    global car4_laps
    
    car1_timelap = 0
    car2_timelap = 0
    car3_timelap = 0
    car4_timelap = 0

    car1_laps = 0
    car2_laps = 0
    car3_laps = 0
    car4_laps = 0
    
runningTrack = list()
last_value_change_ms1 = 0
def calcTrack():
    global car1
    global car2
    global car3
    global car4
    global runningTrack
    ret = list()
    if not runningTrack:
        for i in range(tracks):
            ret.append(i+1)
    else:
        for i in range(1,tracks):
            ret.append(runningTrack[i])
        ret.append(runningTrack[0])
    
    car1["Pista" + str(ret[0])] = list()
    car2["Pista" + str(ret[1])] = list()
    car3["Pista" + str(ret[2])] = list()
    car4["Pista" + str(ret[3])] = list() 
    
    runningTrack = ret
    resetTimeLaps()
def car1Timer(p):
    global last_value_change_ms1
    global car1
    global car1_timelap
    global car1_laps
    
    if not gp_ready:
        return
    
    cur_time = utime.ticks_ms()
    diff = cur_time - last_value_change_ms1
    
    if diff > 1000:
        if (car1_laps<laps): #Only if laps done < totla laps to be!
            last_value_change_ms1 = cur_time
        
            if not car1_timelap:
                car1_timelap = cur_time
                print('Set car1 timer to current time: ',car1_timelap)
                return
            
            print('Appending Car1 Time Track: ', cur_time - car1_timelap)
            car1["Pista" + str(runningTrack[0])].append(cur_time - car1_timelap)
            car1_timelap = cur_time
            car1_laps = car1_laps + 1
    #else:  
    #    print("Debouncing...", diff)
last_value_change_ms2 = 0
def car2Timer(p):
    global car2
    global last_value_change_ms2
    global car2_timelap
    global car2_laps
    
    if not gp_ready:
        return
    
    cur_time = utime.ticks_ms()
    diff = cur_time - last_value_change_ms2
    
    if diff > 1000:
        if (car2_laps<laps): #Only if laps done < totla laps to be!
            last_value_change_ms2 = cur_time
        
            if not car2_timelap:
                car2_timelap = cur_time
                print('Set car2 timer to current time: ',car2_timelap)
                return
            
            print('Appending Car2 Time Track: ', cur_time - car2_timelap)
            car2["Pista" + str(runningTrack[1])].append(cur_time - car2_timelap)
            car2_timelap = cur_time
            car2_laps = car2_laps + 1

last_value_change_ms3 = 0
def car3Timer(p):
    global car3
    global last_value_change_ms3
    global car3_timelap
    global car3_laps
    
    if not gp_ready:
        return
    
    cur_time = utime.ticks_ms()
    diff = cur_time - last_value_change_ms3
    
    if diff > 1000:
        if (car3_laps<laps): #Only if laps done < totla laps to be!
            last_value_change_ms3 = cur_time
        
            if not car3_timelap:
                car3_timelap = cur_time
                print('Set car3 timer to current time: ',car3_timelap)
                return
            
            print('Appending Car3 Time Track: ', cur_time - car3_timelap)
            car3["Pista" + str(runningTrack[2])].append(cur_time - car3_timelap)
            car3_timelap = cur_time
            car3_laps = car3_laps + 1

last_value_change_ms4 = 0    
def car4Timer(p):
    global car4
    global last_value_change_ms4
    global car4_timelap
    global car4_laps
    
    if not gp_ready:
        return
    
    cur_time = utime.ticks_ms()
    diff = cur_time - last_value_change_ms4
    
    if diff > 1000:
        if (car4_laps<laps): #Only if laps done < totla laps to be!
            last_value_change_ms4 = cur_time
        
            if not car4_timelap:
                car4_timelap = cur_time
                print('Set car4 timer to current time: ',car4_timelap)
                return
            
            print('Appending Car4 Time Track: ', cur_time - car4_timelap)
            car4["Pista" + str(runningTrack[3])].append(cur_time - car4_timelap)
            car4_timelap = cur_time
            car4_laps = car4_laps + 1

pin1.irq(trigger=machine.Pin.IRQ_FALLING, handler=car1Timer)
pin2.irq(trigger=machine.Pin.IRQ_FALLING, handler=car2Timer)
pin3.irq(trigger=machine.Pin.IRQ_FALLING, handler=car3Timer)
pin4.irq(trigger=machine.Pin.IRQ_FALLING, handler=car4Timer)

#### Parsing function
def qs_parse(qs):
 
  parameters = {}
  ampersandSplit = qs.split("&")
 
  for element in ampersandSplit:
    equalSplit = element.split("=")
    parameters[equalSplit[0]] = equalSplit[1]
 
  return parameters
 
@app.route("/")
def index(req, resp):
    global car1
    global car2
    global car3
    global car4
    #car times
    car1_t = ''
    print('Car1 = ', car1)
    timeSum = 0
    for track in car1:
        car1_t = car1_t + '<h3>{}</h3>'.format(track)
        trackCounter = 0
        for t in car1[track]:
            dtime = utime.localtime(int(t/1000))
            timeSum = timeSum + t
            mills = t%1000
            car1_t = car1_t + '<p>{}:{}.{}</p>'.format(dtime[4],dtime[5],mills)
            trackCounter = t + trackCounter 
        dtimeTrackC1 = utime.localtime(int(trackCounter/1000))
        millsTrackC1 = trackCounter%1000
        car1_t = car1_t + '<p style="background-color:#004d00;">.</p>'
        car1_t = car1_t + '<p>Total: {}:{}.{}</p>'.format(dtimeTrackC1[4],dtimeTrackC1[5],millsTrackC1)    
    dtimeC1 = utime.localtime(int(timeSum/1000))
    millsC1 = timeSum%1000
    car1_t = car1_t + '<p style="background-color:#000;">.</p>'
    car1_t = car1_t + '<h3>Totais: {}:{}.{}</h3>'.format(dtimeC1[4],dtimeC1[5],millsC1)
    
    car2_t = ''
    timeSum = 0
    for track in car2:
        car2_t = car2_t + '<h3>{}</h3>'.format(track)
        trackCounter = 0
        for t in car2[track]:
            dtime = utime.localtime(int(t/1000))
            timeSum = timeSum + t
            mills = t%1000
            car2_t = car2_t + '<p>{}:{}.{}</p>'.format(dtime[4],dtime[5],mills)
            trackCounter = t + trackCounter 
        dtimeTrackC2 = utime.localtime(int(trackCounter/1000))
        millsTrackC2 = trackCounter%1000
        car2_t = car2_t + '<p style="background-color:#006600;">.</p>'
        car2_t = car2_t + '<p>Total: {}:{}.{}</p>'.format(dtimeTrackC2[4],dtimeTrackC2[5],millsTrackC2)    
    dtimeC2 = utime.localtime(int(timeSum/1000))
    millsC2 = timeSum%1000
    car2_t = car2_t + '<p style="background-color:#000;">.</p>'
    car2_t = car2_t + '<h3>Totais: {}:{}.{}</h3>'.format(dtimeC2[4],dtimeC2[5],millsC2)
    
    car3_t = ''
    timeSum = 0
    for track in car3:
        car3_t = car3_t + '<h3>{}</h3>'.format(track)
        trackCounter = 0
        for t in car3[track]:
            dtime = utime.localtime(int(t/1000))
            timeSum = timeSum + t
            mills = t%1000
            car3_t = car3_t + '<p>{}:{}.{}</p>'.format(dtime[4],dtime[5],mills)
            trackCounter = t + trackCounter 
        dtimeTrackC3 = utime.localtime(int(trackCounter/1000))
        millsTrackC3 = trackCounter%1000
        car3_t = car3_t + '<div style="background-color:#008000;">.</div>'
        car3_t = car3_t + '<p>Total: {}:{}.{}</p>'.format(dtimeTrackC3[4],dtimeTrackC3[5],millsTrackC3)    
    dtimeC3 = utime.localtime(int(timeSum/1000))
    millsC3 = timeSum%1000
    car3_t = car3_t + '<div style="background-color:#000;">.</div>'
    car3_t = car3_t + '<h3>Totais: {}:{}.{}</h3>'.format(dtimeC3[4],dtimeC3[5],millsC3)
    
    car4_t = ''
    timeSum = 0
    for track in car4:
        car4_t = car4_t + '<h3>{}</h3>'.format(track)
        trackCounter = 0
        for t in car4[track]:
            dtime = utime.localtime(int(t/1000))
            timeSum = timeSum + t
            mills = t%1000
            car4_t = car4_t + '<p>{}:{}.{}</p>'.format(dtime[4],dtime[5],mills)
            trackCounter = t + trackCounter 
        dtimeTrackC4 = utime.localtime(int(trackCounter/1000))
        millsTrackC4 = trackCounter%1000
        car4_t = car4_t + '<div style="background-color:#009900;">.</div>'
        car4_t = car4_t + '<p>Total: {}:{}.{}</p>'.format(dtimeTrackC4[4],dtimeTrackC4[5],millsTrackC4)    
    dtimeC4 = utime.localtime(int(timeSum/1000))
    millsC4 = timeSum%1000
    car4_t = car4_t + '<div style="background-color:#000;">.</div>'
    car4_t = car4_t + '<h3>Totais: {}:{}.{}</h3>'.format(dtimeC4[4],dtimeC4[5],millsC4)
    
    if gp_ready:
        rdy = "SIM"
    else:
        rdy = "NAO"
    yield from picoweb.start_response(resp)
    yield from resp.awrite(u.timetrack.format(laps=laps,car1_name=car1_name,car2_name=car2_name,car3_name=car3_name,car4_name=car4_name,car1_times=car1_t,car2_times=car2_t,car3_times=car3_t,car4_times=car4_t,ready=rdy))

@app.route("/data")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(u.datainput)

@app.route("/start")
def index(req, resp):
    global gp_ready
    gp_ready = True
    calcTrack()
    headers = {"Location": "/"}
    yield from picoweb.start_response(resp, status="303", headers=headers)
    
@app.route("/datain")
def index(req, resp):
    global car1_name
    global car2_name
    global car3_name
    global car4_name
    global laps
    
    queryString = req.qs
    parameters = qs_parse(queryString)
    print('Parameters: ',parameters)
    car1_name=parameters['car1']
    car2_name=parameters['car2']
    car3_name=parameters['car3']
    car4_name=parameters['car4']
    laps = int(parameters['laps'])
    
    headers = {"Location": "/"}
    yield from picoweb.start_response(resp, status="303", headers=headers)
    
@app.route("/reset")
def reset(req, resp):
    global car1
    global car2
    global car3
    global car4
    
    global gp_ready
    global runningTrack
    runningTrack = list()
    
    car1 = {}
    car2 = {}
    car3 = {}
    car4 = {}
    resetTimeLaps()
    gp_ready = False
    
    headers = {"Location": "/"}
    yield from picoweb.start_response(resp, status="303", headers=headers)

def countTrack():
    t = utime.ticks_ms()

app.run(debug=True, host = "0.0.0.0")


