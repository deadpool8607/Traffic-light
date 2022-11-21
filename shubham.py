import signal 
import time
i=1
while(True):
    print('siganl')
    print('green')
    print('ready to go')
    print('____________________')
    time.sleep(60)
    print('signal')
    print ('red')
    print('stop the car')
    print('_____________________')
    time.sleep(60)
    print('signal')
    print('yellow')
    print('ready to go and stop')
    print('_____________________')
    time.sleep(60)
    i=i+1
    if(i>3):
        break
    print('select the right signal')
    print('_______________________')