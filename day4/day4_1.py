from typing import List

def doesContain(a: List[int], b: List[int]) -> bool:
    # does a contain b?
    i, j = a
    x, y = b
    if i <= x and j >= y:
        return True
    if x <= i and y >= j:
        return True
    return False

f = open("./day4input.txt")
ans = 0
for line in f:
    r1, r2 = line.strip().split(",")
    r1 = list(map(int, r1.split("-")))
    r2 = list(map(int, r2.split("-")))

    if doesContain(r1, r2):
        ans += 1

print(ans)

    
    
