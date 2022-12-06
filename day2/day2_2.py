# 1 losses to 2
# 2 losses to 3
# 3 looses to 1

oppMap = {"A": "R", "B": "P", "C": "S"}
shapeScore = {"R":1, "P":2, "S":3}
moveMaps = {
    "Z": {"P": "S", "S": "R", "R": "P"}, 
    "X": {"R": "S", "S": "P", "P": "R"},
    "Y": {"R": "R", "S": "S", "P": "P"},
    }
signScore = {"X": 0, "Y": 3, "Z": 6}


def main():
    f = open("./day2input.txt")
    ans = 0
    for line in f:
        line = line.strip()
        opp, sign = line.split(" ")
        opp = oppMap[opp]
        ans += signScore[sign] + shapeScore[moveMaps[sign][opp]]

    print(ans)

if __name__ == "__main__":
    main()
        

