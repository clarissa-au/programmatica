data = """HIDDEN"""

cleanedData = data.split("\n")
lsA = []
lsB = []
for i in cleanedData:
    a, b = i.split("   ")
    lsA.append(int(a))
    lsB.append(int(b))
lsA.sort()
lsB.sort()
# part 1
answer = 0
for i in range(len(lsA)):
    answer += abs(lsA[i] - lsB[i])
print(f"Part 1 answer: {answer}")
# part 2
dictB = {}
for i in lsB:
    if i in dictB:
        dictB[i] += 1
    else:
        dictB[i] = 1
answer = 0
for i in lsA:
    answer += i * dictB.get(i, 0)
print(f"Part 2 answer: {answer}")
