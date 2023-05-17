import matplotlib.pyplot as plt
import csv
import statistics

def show_avgdayspeed():
    datavis  = []
    windlist = []
    days     = 0

    for item in reader:
        speed = item["currentspeed"]
        time  = item["time"]

        windlist.append(float(speed))

        if time == "0000":
            datavis.append((days, statistics.mean(windlist)))
            days += 1
            windlist.clear()

    plt.plot(*zip(*datavis[:365]))
    plt.xlabel("day")
    plt.ylabel("avg windspeed (m/s)")
    plt.show()

def show_avghourspeed():
    timespeeddict = {}

    for item in reader:
        speed = item["currentspeed"]
        time  = item["time"]

        if time not in timespeeddict:
            timespeeddict[time] = []

        timespeeddict[time].append(float(speed))

    timespeedlist = []
    for time, speed in timespeeddict.items():
        avgspeed = statistics.mean(speed)
        timespeedlist.append((time, avgspeed))

    plt.plot(*zip(*timespeedlist))
    plt.xlabel("time")
    plt.ylabel("avg windspeed (m/s)")
    plt.show()

if __name__ == "__main__":
    reader = csv.DictReader(open("windspeeds.csv", "r", encoding="utf-8"), delimiter=",", quoting=csv.QUOTE_NONE)
    # show_avgdayspeed()
    show_avghourspeed()