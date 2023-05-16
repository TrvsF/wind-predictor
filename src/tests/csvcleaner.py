import csv
import matplotlib.pyplot as plt
import statistics

reader  = csv.DictReader(open('windraw.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
newlist = []
windq   = []
datavis = []
days    = 0
counter = 0
for item in reader:
    counter += 1

    dt = item["#Date and Time"].split(" ")[1].replace(":", "")
    ws = item["Wind Spd 12m m/s"]
    
    if ws == None or ws == "" or float(ws) > 10.0 or float(ws) < 0.01:
        continue 

    if len(windq) > 3:
        windq.pop(0)
        newlist.append((dt, windq[0], windq[1], windq[2], ws))
        # newlist.append((windq[0], windq[1], windq[2], ws))

    windq.append(float(ws))

    if dt == "0000":
        datavis.append((days, statistics.mean(windq)))
        days += 1
        windq.clear()

print(f"days counted : {len(datavis)}")

with open("windspeeds.csv", "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["time", "oldspeed1", "oldspeed2", "oldspeed3", "currentspeed"])
    # writer.writerow(["oldspeed1", "oldspeed2", "oldspeed3", "currentspeed"])
    for row in newlist:
        writer.writerow(row)

plt.plot(*zip(*datavis[:365]))
plt.xlabel("day")
plt.ylabel("windspeed (m/s)")
plt.show()