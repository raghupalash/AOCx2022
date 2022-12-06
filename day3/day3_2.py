from string import ascii_letters

alphabet = list(ascii_letters)
priority = {}
for i, c in enumerate(alphabet):
    priority[c] = i + 1

f = open("./day3input.txt")
ans = 0
groupSet = set()
for i, line in enumerate(f):
    lineSet = set(line.strip())
    if groupSet: lineSet = lineSet.intersection(groupSet)
    groupSet = lineSet

    if (i + 1) % 3 == 0:
        c = list(groupSet)[0]
        ans += priority[c]
        groupSet = set()

print(ans)