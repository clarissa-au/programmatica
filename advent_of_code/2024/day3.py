import re

# part 1
matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", data)
answer = 0
for match in matches:
    answer += int(match[0]) * int(match[1])
print(f"Part 1 answer: {answer}")

# part 2
# i'm pretty sure there is a elegant regex solution
# of course you can reparse it into a ary containing only cond and numbers and use a state snippet to calculate it
# after spending 50 mins: im pretty sure im looking at varlen lookahead and lookbehind modifying a main snippet

matches = re.findall(r"(do(?:n't)?\(\))|(mul\([0-9]{1,3},[0-9]{1,3}\))", data)
answer = 0
stateContinue = True
for match in matches:
    if match[0] == "":
        if stateContinue:
            numbers = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", match[1])
            answer += int(numbers[0][0]) * int(numbers[0][1])
    else:
        if match[0] == "do()" and not stateContinue:
            stateContinue = True
        if match[0] == "don't()" and stateContinue:
            stateContinue = False
print(f"Part 2 answer: {answer}")
