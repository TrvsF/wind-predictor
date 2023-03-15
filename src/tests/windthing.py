from machine import Pin, ADC, Timer, RTC
import time

filename = ""
rtc     = RTC()
timer   = Timer(0)
pot     = ADC(Pin(4))
pot.atten(ADC.ATTN_11DB)

def start():
    global timer
    global filename
    date = rtc.datetime()
    filename = f"{date[4]}-{date[5]}-{date[6]}.txt"

    timer.init(period=500, mode=Timer.PERIODIC, callback=printspeed)

def stop():
    global timer

    timer.deinit()

def printspeed(args):
    global pot
    global rtc
    global filename

    # get time & assign to xtime
    localtime = rtc.datetime()
    hour = localtime[4]
    mins = localtime[5]
    secs = localtime[6]
    xtime = (hour, mins, secs)
    voltage = pot.read()

    with open(f"{filename}", "a", encoding="utf-8") as file:
        file.write(f"{voltage}:{xtime}\n")
    print(pot.read())
    print(xtime)

def settime(month, day, hour, min, second, weekday=0):
    global rtc

    # TODO : system for weekday
    rtc.datetime((2023, month, day, weekday, hour, min, second, 0))