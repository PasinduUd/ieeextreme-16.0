# 92.86%

p = int(input())
n = int(input())
r, c = map(int, input().strip().split(','))
lex = input()

phrases = []
for _ in range(p):
    phrases.append(input())

grid = [[] for x in range(r)]
i = 0
j = 0
for _ in range(n):
    line = input()
    locked = False
    for ch in line:
        if not locked and ch == '<':
            locked = True
        elif not locked:
            grid[i].append(ch)
            if j + 1 < c:
                j += 1
            else:
                if i + 1 < r:
                    i += 1
                    j = 0
                else:
                    break

        elif locked and ch == '>':
            locked = False

if lex == 'S':
    for phrase in phrases:
        crypt = []
        is_break = False
        for letter in phrase:
            for i in range(r):
                is_break = False
                for j in range(c):
                    if letter == grid[i][j]:
                        crypt.append(i+1)
                        crypt.append(j+1)
                        is_break = True
                        break
                if is_break:
                    break
            else:
                crypt = [0]
                break
        print(",".join(map(str, crypt)))
else:
    for phrase in phrases:
        crypt = []
        is_break = False
        for letter in phrase:
            for i in range(r-1, -1, -1):
                is_break = False
                for j in range(c-1, -1, -1):
                    if letter == grid[i][j]:
                        crypt.append(i+1)
                        crypt.append(j+1)
                        is_break = True
                        break
                if is_break:
                    break
            else:
                crypt = [0]
                break
        print(",".join(map(str, crypt)))
