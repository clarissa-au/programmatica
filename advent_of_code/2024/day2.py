def identificator(toTry):
    flagIncr = "undecided"
    flagSafe = True
    ptr = None
    for j in toTry:
        if ptr == None:
            ptr = j
        else:
            if flagIncr == "undecided":
                if j > ptr:
                    if not (1 <= abs(j - ptr) <= 3):
                        flagSafe = False
                        break
                    flagIncr = "increasing"
                else:
                    if not (1 <= abs(j - ptr) <= 3):
                        flagSafe = False
                        break
                    flagIncr = "decreasing"
                ptr = j
            else:
                if flagIncr == "increasing" and not (1 <= (j - ptr) <= 3):
                    flagSafe = False
                    break
                if flagIncr == "decreasing" and not (-1 >= (j - ptr) >= -3):
                    flagSafe = False
                    break
                ptr = j
    return flagSafe

def problemDampener(lst):
    for elem in range(len(lst)):
        yield lst[:elem] + lst[elem+1:]


cleanedData = data.split("\n")
doubleCleanedData = []
for i in cleanedData:
    doubleCleanedData.append([int(j) for j in i.split(" ")])
# part 1
answer = 0
for i in doubleCleanedData:
    safe = identificator(i)
    if safe:
        answer += 1

print(f"Part 1 answer: {answer}")
# part 2
answer = 0
for i in doubleCleanedData:
    safe = identificator(i)
    if safe:
        answer += 1
    else:
        for altern in problemDampener(i):
            if identificator(altern):
                answer += 1
                break

print(f"Part 2 answer: {answer}")
