import math
import matplotlib.pyplot as plt
import networkx as nx

policySet = """HIDDEN"""
toCheckData = """HIDDEN"""

policySet = policySet.split("\n")
policySet = [i.split("|") for i in policySet]

toCheckData = toCheckData.split("\n")
toCheckData = [i.split(",") for i in toCheckData]

dependencyTable = {}
for policy in policySet:
    precedent, antecedent = policy
    if antecedent not in dependencyTable:
        dependencyTable[antecedent] = [precedent]
    else:
        dependencyTable[antecedent].append(precedent)

# simplification of dependency table
# if b and c both have a as a dependency, and c has b as a dependency, remove ac

# deepcopy dependency table, too tired to research how to correctly use deepcopy
simplifiedDependencyTable = {}
for i in dependencyTable.keys():
    for j in dependencyTable[i]:
        if i not in simplifiedDependencyTable:
            simplifiedDependencyTable[i] = [j]
        else:
            simplifiedDependencyTable[i].append(j)

flagSimplification = None
loopCount = 0
simplified = 0
while flagSimplification != False:
    flagSimplification = False
    loopCount += 1
    simplified = 0
    for i in simplifiedDependencyTable.keys():
        for j in simplifiedDependencyTable.keys():
            if i == j:
                continue
            if i not in simplifiedDependencyTable[j]:
                continue
            iSet = set(simplifiedDependencyTable[i])
            jSet = set(simplifiedDependencyTable[j])
            overlap = iSet.intersection(jSet)
            if len(overlap) > 0:
                newJSet = jSet - overlap
                simplifiedDependencyTable[j] = set(newJSet)
                simplified += len(overlap)
                flagSimplification = True
    print(f"Loop {loopCount}, removed {simplified} redundant dependencies.")
print(f"The simplified Dependency Table is as follows: {simplifiedDependencyTable}")

# visualization of the ouroboros as summarized above
fullLoop = ['19']
while True:
    nextNode = list(simplifiedDependencyTable[fullLoop[-1]])[0]
    if nextNode == fullLoop[0]:
        break
    fullLoop.append(nextNode)

pos = {fullLoop[i]: (4*math.sin(i/len(fullLoop)*2*math.pi),
                     4*math.cos(i/len(fullLoop)*2*math.pi)) for i in range(len(fullLoop))}

G = nx.DiGraph(simplifiedDependencyTable)

nx.draw_networkx(G, pos)

ax = plt.gca()
ax.margins(0)
plt.axis("off")
plt.show()

# if a dependency comes later then it is flagged
answer = 0
for check in toCheckData:
    goodBook = True
    negSet = set()
    for item in check:
        if item in negSet:
            goodBook = False
            break
        negSet = negSet.union(set(dependencyTable[item]))
    if goodBook:
        answer += int(check[len(check)//2])
print(f"Part 1 answer: {answer}")

def checkGoodBook(book, policy):
    goodBook = True
    negSet = set()
    for item in book:
        if item in negSet:
            goodBook = False
            break
        negSet = negSet.union(set(policy[item]))
    return goodBook

answer = 0
for check in toCheckData:
    flag_badData = False
    print(f"Beginning Book:    {check}")
    while not checkGoodBook(check, dependencyTable):
        flag_badData = True
        for i in range(len(check)):
            for j in range(len(check)):
                if i != j and check[j] in dependencyTable[check[i]] and i < j:
                    check[i], check[j] = check[j], check[i]
                    print(f"Intermediate Book: {check}")
    print(f"Final Recovered Book is as follows: {check}")
    if flag_badData:
        answer += int(check[len(check)//2])
print(f"Part 2 answer: {answer}")
