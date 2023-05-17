import csv

def write_csv(data, filename="windspeeds"):
    with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["time", "oldspeed1", "oldspeed2", "oldspeed3", "currentspeed"])
        for row in data:
            writer.writerow(row)

def get_data():
    # setup lists
    priorspeeds = []
    data = []

    for item in reader:
        # get datetime in format 'hhmm' and wind speed in m/s
        dt = item["#Date and Time"].split(" ")[1].replace(":", "")
        ws = item["Wind Spd 12m m/s"]
        # ensure time str is consistant
        if len(dt) == 3:
            dt = "0" + dt
        # if wind speed is invald continue
        if ws == None or ws == "" or float(ws) > 10.0 or float(ws) < 0.01:
            continue 
        # save windspeed to list and pop front, then add 4 inputs to data
        if len(priorspeeds) > 3:
            priorspeeds.pop(0)
            data.append((dt, priorspeeds[0], priorspeeds[1], priorspeeds[2], ws))
        priorspeeds.append(float(ws))
    
    return data

if __name__ == "__main__":
    reader = csv.DictReader(open('windraw.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
    data = get_data()
    write_csv(data)