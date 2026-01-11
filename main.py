import psutil, time, winsound

i=0
while True:
    batinf = psutil.sensors_battery()
    
    if batinf is None:
        continue
    if batinf.percent>=80 and batinf.power_plugged:
        winsound.Beep(700, 500)
        time.sleep(3)
    elif batinf.percent<=30 and not batinf.power_plugged:
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    i+=1
    time.sleep(1)
