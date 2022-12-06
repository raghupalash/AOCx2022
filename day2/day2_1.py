# 1 losses to 2
# 2 losses to 3
# 3 looses to 1

p1Map = {"A": "R", "B": "P", "C": "S"}
p2Map = {"X": "R", "Y": "P", "Z": "S"}
shapeScore = {"R":1, "P":2, "S":3}

winSet = {("P", "S"), ("S", "R"), ("R", "P")}
looseSet = {("R", "S"), ("S", "P"), ("P", "R")}

def score(opp, user):
    score = shapeScore[user]
    if opp == user:
        return score + 3
    if (opp, user) in winSet:
        return score + 6
    if (opp, user) in looseSet:
        return score

def main():
    f = open("./day2input.txt")
    ans = 0
    for line in f:
        line = line.strip()
        opp, user = line.split(" ")
        opp = p1Map[opp]
        user = p2Map[user]
        ans += score(opp, user)

    print(ans)

if __name__ == "__main__":
    main()
        

