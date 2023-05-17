from machine import Pin, ADC, Timer, RTC

# output filename
filename = ""
# store current time
rtc     = RTC()
# timer to run method 
timer   = Timer(0)
# pins
pot     = ADC(Pin(4))
pot.atten(ADC.ATTN_11DB)

# ------------
# util methods
# ------------
def get_timevar(hour, min):
    return hour * 100 + min

def get_speed(val):
    voltage_val = val / 65535 * 3.3
    return voltage_val

def set_time(month, day, hour, min, second, weekday=0):
    global rtc
    rtc.datetime((2023, month, day, weekday, hour, min, second, 0))

# ------------
# main methods
# ------------
def start():
    global timer
    global filename

    date = rtc.datetime()
    # hour-min-second.txt
    filename = f"{date[3]}-{date[4]}-{date[5]}.txt"

    timer.init(period=30000, mode=Timer.PERIODIC, callback=print_speed)

def stop():
    global timer
    timer.deinit()

def print_speed(args):
    global pot
    global rtc
    global filename

    # time
    localtime = rtc.datetime()
    hour = localtime[4]
    min = localtime[5]
    vartime = get_timevar(hour, min)

    # wind speed
    voltage = pot.read()
    windspeed = get_speed(voltage)

    # write to file
    with open(f"{filename}", "a", encoding="utf-8") as file:
        file.write(f"{windspeed}:{vartime}\n")
        
    # print to console
    print(f"speed: {windspeed} time: {vartime}")