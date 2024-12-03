DATA = """HIDDEN"""

cleanedData = DATA.split("\n")
RED = 12
GREEN = 13
BLUE = 14
tot = 0
for i in cleanedData:
    string = i.split(" ")
    curID = int(string[1].replace(":", ""))
    good = True
    string = string[2:]
    state = "number"
    val = 0
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    redSeen = 0
    blueSeen = 0
    greenSeen = 0
    for j in string:
        if state == "number":
            val = int(j)
            state = "text"
        else:
            if j.startswith("red"):
                redSeen += val
            if j.startswith("green"):
                greenSeen += val
            if j.startswith("blue"):
                blueSeen += val
            if j.endswith(";"):
                if redSeen > maxRed:
                    maxRed = redSeen
                if greenSeen > maxGreen:
                    maxGreen = greenSeen
                if blueSeen > maxBlue:
                    maxBlue = blueSeen
                redSeen = 0
                greenSeen = 0
                blueSeen = 0
            state = "number"
    if redSeen > maxRed:
        maxRed = redSeen
    if greenSeen > maxGreen:
        maxGreen = greenSeen
    if blueSeen > maxBlue:
        maxBlue = blueSeen
    print((maxRed, maxGreen, maxBlue))
    # if good:
    #    tot += curID
    pwr = maxBlue * maxGreen * maxRed
    tot += pwr
print(tot)
