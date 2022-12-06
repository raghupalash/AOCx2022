from string import ascii_letters

alphabet = list(ascii_letters)
priority = {}
for i, c in enumerate(alphabet):
    priority[c] = i + 1

f = open("./day3input.txt")
ans = 0
for line in f:
    line = line.strip()
    half = len(line) // 2
    same = set(line[:half]).intersection(line[half:])
    ans += priority[list(same)[0]]

print(ans)