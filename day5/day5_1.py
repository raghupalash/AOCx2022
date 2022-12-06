from collections import defaultdict

f = open("./day5input.txt").read()
table, moves = f.split("\n\n")
table = table.splitlines()
moves = moves.splitlines()
stackPos = table.pop(-1)

crates = defaultdict(list)

for line in reversed(table):
    for i, pos in enumerate(stackPos):
        if pos == " " or line[i] == " ":
            continue
        crates[int(pos)].append(line[i])


for move in moves:
    move = [x for x in move.split() if x not in {"from", "to", "move"}]
    n, f, t = map(int, move)
    for _ in range(n):
        crates[t].append(crates[f].pop())

stack = []
for _, col in crates.items():
    stack.append(col[-1])

print("".join(stack))






