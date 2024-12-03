DATA = """HIDDEN"""

import re

ans = []
cleanedData = DATA.split("\n")
for i in cleanedData:
    txtStr = ""
    number = ""
    for j in i:
        txtStr = txtStr + j
        txtStr = re.sub("one", "1", txtStr)
        txtStr = re.sub("two", "2", txtStr)
        txtStr = re.sub("three", "3", txtStr)
        txtStr = re.sub("four", "4", txtStr)
        txtStr = re.sub("five", "5", txtStr)
        txtStr = re.sub("six", "6", txtStr)
        txtStr = re.sub("seven", "7", txtStr)
        txtStr = re.sub("eight", "8", txtStr)
        txtStr = re.sub("nine", "9", txtStr)

    for j in txtStr:
        try:
            int(j)
        except:
            continue
        number = number + j
    if len(number) > 2:
        number = number[0] + number[-1]
    if len(number) == 1:
        number = number + number
    ans.append(int(number))
print(sum(ans))
print(ans)
