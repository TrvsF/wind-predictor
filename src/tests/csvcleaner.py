import csv

reader  = csv.DictReader(open('windraw.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
newlist = []
windq   = []
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

    windq.append(ws)

# print(newlist)

with open("windspeeds.csv", "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["time", "oldspeed1", "oldspeed2", "oldspeed3", "currentspeed"])
    # writer.writerow(["oldspeed1", "oldspeed2", "oldspeed3", "currentspeed"])
    for row in newlist:
        writer.writerow(row)