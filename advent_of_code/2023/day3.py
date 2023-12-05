DATA = """HIDDEN"""

cleanedData = DATA.splitlines()
SYMBOL = "+/-=_?!@#$%^&()"
DIGITS = "1234567890"
tot = 0
i = None
j = None
k = None
l = None
m = None
oldTestData = None
symbolSet = set()
for i in DATA:
    if i not in ".1234567890" and i not in "\n":
        symbolSet.add(i)
print(symbolSet)
print(symbolSet.issubset(set(SYMBOL)))
print(cleanedData)
cleanedData.insert(0, "".join(["." for p in range(0, len(cleanedData[0]))]))
cleanedData.append("".join(["." for p in range(0, len(cleanedData[0]))]))
for i in range(0, len(cleanedData)):
    cleanedData[i] = "." + cleanedData[i] + "."
for i in range(0, len(cleanedData)):
    for j in range(0, len(cleanedData[0])):
        assert (all(len(ckc) == len(cleanedData[0]) for ckc in cleanedData))
        try:
            if cleanedData[i][j] in SYMBOL:
                for (k, l) in ((i+1, j), (i+1, j+1), (i, j+1), (i-1, j+1), (i-1, j), (i-1, j-1), (i, j-1), (i+1, j-1)):
                    try:
                        if str(cleanedData[k][l]) in DIGITS:
                            while str(cleanedData[k][l]) in DIGITS:
                                l -= 1
                            l += 1
                            m = l
                            while str(cleanedData[k][m]) in DIGITS:
                                m += 1
                            m -= 1
                            # tot += int(cleanedData[k][l:m+1])
                            cleanedData[k] = cleanedData[k][:l] + \
                                ("".join(["." for p in range(l, m+1)])
                                 ) + cleanedData[k][m+1:]
                    except IndexError:
                        continue
            if cleanedData[i][j] == "*":
                tempStorage = []
                for (k, l) in ((i+1, j), (i+1, j+1), (i, j+1), (i-1, j+1), (i-1, j), (i-1, j-1), (i, j-1), (i+1, j-1)):
                    try:
                        if str(cleanedData[k][l]) in DIGITS:
                            while str(cleanedData[k][l]) in DIGITS:
                                l -= 1
                            l += 1
                            m = l
                            while str(cleanedData[k][m]) in DIGITS:
                                m += 1
                            m -= 1
                            tempStorage.append(int(cleanedData[k][l:m+1]))
                            cleanedData[k] = cleanedData[k][:l] + \
                                ("".join(["." for p in range(l, m+1)])
                                 ) + cleanedData[k][m+1:]
                    except IndexError:
                        continue
                print(tempStorage)
                if len(tempStorage) == 2:
                    tot += tempStorage[0] * tempStorage[1]
                # else:
                #    tot += sum(tempStorage)
        except:
            raise Exception((i, j, k, l, m, tot))
print(tot)
