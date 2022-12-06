from typing import List

def doesOverlap(a: List[int], b: List[int]) -> bool:
    # does the two ranges overlap at all
    i, j = a
    x, y = b
    if x <= i <= y:
        return True
    if i <= x <= j:
        return True
    return False

f = open("./day4input.txt")
ans = 0
for line in f:
    r1, r2 = line.strip().split(",")
    r1 = list(map(int, r1.split("-")))
    r2 = list(map(int, r2.split("-")))

    if doesOverlap(r1, r2):
        ans += 1

print(ans)