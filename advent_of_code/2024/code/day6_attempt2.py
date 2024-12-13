data = """HIDDEN"""

data = [list(i) for i in data.split("\n")]

mapping = {}
assert len(data) == len(data[0])
print(data)
print(len(data))
size = len(data)
for i in range(len(data)):
    for j in range(len(data)):
        mapping[(j, i)] = data[i][j]  # remux into standardey carte coords

walls = []
pos = (-1, -1)
direction = "^"
for key in mapping:
    if mapping[key] == "^":
        pos = key
    if mapping[key] == "#":
        walls.append(key)

ROTATION = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}
NEXT_STEP = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

trace = []
tracePos = (pos[0], pos[1])
traceDir = direction
while tracePos[0] >= 0 and tracePos[0] < size and tracePos[1] >= 0 and tracePos[1] < size:
    nextDelta = NEXT_STEP[traceDir]
    nextPos = (tracePos[0] + nextDelta[0], tracePos[1] + nextDelta[1])
    print(tracePos, traceDir, nextPos)
    if nextPos in walls:
        traceDir = ROTATION[traceDir]
    else:
        trace.append(((nextPos[0], nextPos[1]), traceDir))
        tracePos = nextPos
locs = []
for t in trace:
    if t[0] not in locs:
        locs.append(t[0])
print(f"Part 1 answer: {len(locs)}")
print(locs)


def printField(tracePos, traceDir, walls=walls, boundary=size):
    for i in range(boundary):
        for j in range(boundary):
            if (j, i) in walls:
                print("#", end="")
            elif (j, i) == tracePos:
                print(traceDir, end="")
            else:
                print(".", end="")
        print()


def posChecker(tracePos, traceDir, walls=walls, pos=pos, debug=False):
    trace = []
    nextDelta = NEXT_STEP[traceDir]
    nextPos = (tracePos[0] + nextDelta[0], tracePos[1] + nextDelta[1])
    specialWall = nextPos
    if specialWall in walls:
        return False
    if not (specialWall[0] >= 0 and specialWall[0] < size and specialWall[1] >= 0 and specialWall[1] < size):
        return False
    if specialWall == pos:
        return False  # you can't place a wall at the starting pos
    while True:
        nextDelta = NEXT_STEP[traceDir]
        nextPos = (tracePos[0] + nextDelta[0], tracePos[1] + nextDelta[1])
        if (nextPos[0] < 0 or nextPos[0] > size - 1 or nextPos[1] < 0 or nextPos[1] > size - 1):
            break
        if nextPos in walls or nextPos == specialWall:
            traceDir = ROTATION[traceDir]
            continue
        tracePos = nextPos
        if (tracePos, traceDir) in trace:
            return (tracePos, traceDir)
        trace.append((tracePos, traceDir))
    return False


print(len(trace))
locs = []
duplicates = []
resolvedPos = 0
for t in trace:
    print(f"Resolving {t}.")
    wall = posChecker(t[0], t[1])
    resolvedPos += 1
    if resolvedPos % 500 == 0:
        print(f"Resolved {resolvedPos} positions, found {
              len(locs)} possibilities.")
    if wall and wall[0] not in locs:
        locs.append(wall)
    if wall and wall[0] in locs:
        duplicates.append(wall)
print(f"Part 2 answer: {len(locs)}")

# this is still higher than the expected answer, but it is faster than attempt 1 as the whole field is not being sent as argument.
# continued in attempt 3.