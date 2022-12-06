from collections import deque

f = open("./day6input.txt")
string = [line for line in f][0]
stack = deque(string[0:14])

for i in range(14, len(string)):
    if len(set(stack)) == 14:
        print(i)
        break

    stack.popleft()
    stack.append(string[i])