data = """HIDDEN"""

data = [list(i) for i in data.split("\n")]

grid_list = data
export_grid_keys = []

# sampled solution

grid = {(x, y): grid_list[y][x] for y in range(len(grid_list))
        for x in range(len(grid_list[0]))}

# end of sampled solution

mapping = {}
assert len(data) == len(data[0])
print(data)
print(len(data))
size = len(data)
for i in range(len(data)):
    for j in range(len(data)):
        mapping[(j, i)] = data[i][j]  # remux into standardey carte coords

assert grid == mapping

# sampled solution

GRID_WIDTH, GRID_HEIGHT = (len(grid_list[0]), len(grid_list))

# directions
DIRECTIONS = {'^': (0, -1),
              '>': (1, 0),
              'v': (0, 1),
              '<': (-1, 0)}

NEXT_DIRECTIONS = {'^': '>',
                   '>': 'v',
                   'v': '<',
                   '<': '^'}

BLOCKAGE = '#'

# find START_POSITION
START_POSITION = None
START_DIRECTION = '^'

for y, row in enumerate(grid_list):
    if not START_POSITION:
        for x, position in enumerate(row):
            if position == '^':
                START_POSITION = (x, y)
                break

# end of sampled solution

walls = []
pos = (-1, -1)
direction = "^"
for key in mapping:
    if mapping[key] == "^":
        pos = key
    if mapping[key] == "#":
        walls.append(key)

assert START_POSITION == pos
assert START_DIRECTION == direction

# sampled solution

def trace_path(grid=grid, start_position=START_POSITION, start_direction=START_DIRECTION):
    steps_taken = set()
    current_position = start_position
    current_direction = start_direction
    # next_position = None
    while True:
        x_current, y_current = current_position
        x_direction, y_direction = DIRECTIONS[current_direction]
        next_position = (x_current + x_direction, y_current + y_direction)
        x_next, y_next = next_position
        # break out of loop if out of grid bounds
        if x_next < 0 or x_next > GRID_WIDTH - 1 or y_next < 0 or y_next > GRID_HEIGHT - 1:
            break
        if grid[(x_next, y_next)] == BLOCKAGE:  # change direction if blockage hit
            current_direction = NEXT_DIRECTIONS[current_direction]
            continue
        current_position = next_position  # take a step
        steps_taken.add(next_position)
    return steps_taken


print(len(trace_path()))
print(trace_path())

# end of sampled solution

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

comparison = trace_path()
for key in locs:
    if key not in comparison:
        print(key)

# there is just a single out of bounds key that does not affect the answer, as my soln doesn't count the first exited step but count the final arrived step out of bounds.

# this solution is me rewriting my old solution while comparing it to the sampled solution

num_of_loops = 0
resolved = 0
for x in range(size):
    for y in range(size):
        steps_taken = set()
        subPos = pos
        subDir = direction
        while True:
            nextDelta = NEXT_STEP[subDir]
            nextPos = (subPos[0] + nextDelta[0], subPos[1] + nextDelta[1])
            if nextPos[0] < 0 or nextPos[0] > size - 1 or nextPos[1] < 0 or nextPos[1] > size - 1:
                break
            if nextPos in walls or nextPos == (x, y):
                subDir = ROTATION[subDir]
                continue
            subPos = nextPos
            subPosInfo = (subPos, subDir)
            if subPosInfo in steps_taken:
                num_of_loops += 1
                break
            steps_taken.add(subPosInfo)
        resolved += 1
        if resolved % 100 == 0:
            print(f"Resolved {resolved} positions (found {
                  num_of_loops}), progress {resolved/size/size*100}%")
print(num_of_loops)
