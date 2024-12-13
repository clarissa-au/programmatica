from functools import partial
from multiprocessing.dummy import Pool as ThreadPool
import itertools
import copy
data = """HIDDEN"""

data = [list(i) for i in data.split("\n")]
mapping = {}
boundary = len(data[0])-1
for i in range(len(data)):
    for j in range(len(data[0])):
        mapping[(i, j)] = data[i][j]


class Guard():
    def __init__(self, i, j, direction="n"):
        self.i = i
        self.j = j
        self.direction = direction

    def currentPos(self):
        return (self.i, self.j)

    def currentState(self):
        return (self.i, self.j, self.direction)

    def north(self):
        return (self.i-1, self.j)

    def south(self):
        return (self.i+1, self.j)

    def east(self):
        return (self.i, self.j+1)

    def west(self):
        return (self.i, self.j-1)

    def nextPos(self):
        if self.direction == "n":
            return self.north()
        elif self.direction == "e":
            return self.east()
        elif self.direction == "w":
            return self.west()
        elif self.direction == "s":
            return self.south()

    def rotate(self):
        if self.direction == "n":
            self.direction = "e"
        elif self.direction == "e":
            self.direction = "s"
        elif self.direction == "w":
            self.direction = "n"
        elif self.direction == "s":
            self.direction = "w"

    def moveNextPos(self):
        self.i, self.j = self.nextPos()


location = -1, -1
for key in mapping.keys():
    if mapping[key] == "^":
        location = key
        mapping[key] = "X"
        break
guard = Guard(location[0], location[1])
while True:
    nextChar = mapping.get(guard.nextPos(), "_")
    pos = guard.currentPos()
    if nextChar == "#":
        guard.rotate()
    elif nextChar == "." or nextChar == "X":
        mapping[pos] = "X"
        guard.moveNextPos()
    else:
        mapping[pos] = "X"
        break
answer = 0
for key in mapping.keys():
    if mapping[key] == "X":
        answer += 1
print(f"Part 1 answer: {answer}")


def posDetermine(mapping, guard):
    newGuard = Guard(*guard.currentState())
    newMapping = mapping
    if newMapping.get(newGuard.nextPos(), "_") == "_":
        return None
    specialPos = newGuard.nextPos()
    stateList = []
    flag_loop = newGuard.nextPos()
    while newGuard.currentState() not in stateList:
        stateList.append(newGuard.currentState())
        nextChar = newMapping.get(newGuard.nextPos(), "_")
        if nextChar == "#" or newGuard.nextPos() == specialPos:
            newGuard.rotate()
        elif nextChar == "." or nextChar == "X":
            newGuard.moveNextPos()
        else:
            flag_loop = None
            break
    return flag_loop


guard = Guard(location[0], location[1])
positionTable = []
while True:
    nextChar = mapping.get(guard.nextPos(), "_")
    pos = guard.currentPos()
    if nextChar == "#":
        guard.rotate()
    elif nextChar == "." or nextChar == "X":
        positionTable.append(Guard(*guard.currentState()))
        guard.moveNextPos()
    else:
        break
print(f"There are {len(positionTable)} positions to analyze.")

# trying multiprocessing

pool = ThreadPool(16)
results = pool.map(partial(posDetermine, mapping), positionTable)
pool.close()
pool.join()
locations = []
for result in results:
    if result is not None and result not in locations:
        locations.append(result)
print(f"Part 2 answer: {len(locations)}")

# compared to a single threaded version

locations = []

for i in range(len(positionTable)):
    j = posDetermine(mapping, positionTable[i])
    if j is not None and j not in locations:
        locations.append(result)

print(f"Part 2 answer: {len(locations)}")

# both returns a answer higher than the expected answer, and multiprocessing is just marginally faster than the single threaded version.