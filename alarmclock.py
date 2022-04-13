import os
import datetime
from playsound import playsound
#os. system('cleart')
alarmH = int(input("what hour do you want to ring?"))
alarmM = int(input("what minute do you want to ring?"))
amPm = str(input("am or pm? "))
#os. system('cleart')
print("waiting for alarm", alarmH, alarmM, amPm)
if(amPm == "pm"):
    alarmH = alarmH + 12
    while(1 ==1):
        if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute):
            print("time to wake up")
            playsound("/Users/Ashish/Desktop/Program/audio.mp3.mp3")
            break
