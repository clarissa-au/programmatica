import math
import itertools
data = """HIDDEN"""

data = data.splitlines()
data = [list(i) for i in data]
mapping = {}
bounds = len(data[0])
for i in range(len(data)):
    for j in range(len(data[0])):
        mapping[(i, j)] = data[i][j]

if len(data[0]) != len(data):
    print("Area Not a Square! Tread with caution!")

antennaInfo = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        if mapping[(i, j)] != ".":
            if mapping[(i, j)] not in antennaInfo:
                antennaInfo[mapping[(i, j)]] = [(i, j)]
            else:
                antennaInfo[mapping[(i, j)]].append((i, j))

locations = []
for key in antennaInfo:
    for pair in itertools.product(antennaInfo[key], repeat=2):
        if pair[0] != pair[1]:
            dX = pair[1][0] - pair[0][0]
            dY = pair[1][1] - pair[0][1]
            antinode0 = (pair[0][0]-dX, pair[0][1]-dY)
            if antinode0[0] >= 0 and antinode0[0] < bounds and antinode0[1] >= 0 and antinode0[1] < bounds:
                if antinode0 not in locations:
                    locations.append(antinode0)
            antinode1 = (pair[1][0]+dX, pair[1][1]+dY)
            if antinode1[0] >= 0 and antinode1[0] < bounds and antinode1[1] >= 0 and antinode1[1] < bounds:
                if antinode1 not in locations:
                    locations.append(antinode1)
print(f"Part 1 answer: {len(locations)}")

locations = []
for key in antennaInfo:
    for pair in itertools.product(antennaInfo[key], repeat=2):
        if pair[0] != pair[1]:
            dX = pair[1][0] - pair[0][0]
            dY = pair[1][1] - pair[0][1]
            if pair[0] not in locations:
                locations.append(pair[0])
            if pair[1] not in locations:
                locations.append(pair[1])
            if dX == 0:
                for i in range(len(bounds)):
                    if (i, pair[0][0]) not in locations:
                        locations.append((i, pair[0][0]))
            if dY == 0:
                for i in range(len(bounds)):
                    if (i, pair[0][1]) not in locations:
                        locations.append((i, pair[0][1]))
            if math.gcd(dX, dY) != 0:
                gcd = math.gcd(dX, dY)
                dX = dX / gcd
                dY = dY / gcd
            antinode0 = (pair[0][0]-dX, pair[0][1]-dY)
            while antinode0[0] >= 0 and antinode0[0] < bounds and antinode0[1] >= 0 and antinode0[1] < bounds:
                if antinode0 not in locations:
                    locations.append(antinode0)
                antinode0 = (antinode0[0]-dX, antinode0[1]-dY)
            antinode1 = (pair[0][0]+dX, pair[0][1]+dY)
            while antinode1[0] >= 0 and antinode1[0] < bounds and antinode1[1] >= 0 and antinode1[1] < bounds:
                if antinode1 not in locations:
                    locations.append(antinode1)
                antinode1 = (antinode1[0]+dX, antinode1[1]+dY)

print(f"Part 2 answer: {len(locations)}")
