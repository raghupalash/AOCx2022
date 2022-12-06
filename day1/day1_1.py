# --- Day 1: Calorie Counting ---
f = open("./day1input.txt")
maxCalories = [0, 0, 0]
currElf = 0
for line in f:
    if line == "\n":
        maxCalories.sort()
        maxCalories[0] = max(maxCalories[0], currElf)
        currElf = 0
    else:
        currElf += int(line)

maxCalories.sort()
maxCalories[0] = max(maxCalories[0], currElf)

print(sum(maxCalories))


