# https://csacademy.com/ieeextreme-practice/task/pizza-cutter/
# 100%

t = int(input())
for _ in range(t):
    row = list(map(int, input().split()))
    if row[0] == 0:
        print(1)
    else:
        angs = []
        n = row[0]
        row = row[1:]
        for i in row:
            temp = i
            if temp < 0:
                temp = ((temp % 360) + 360) % 360
            elif temp >= 360:
                temp = temp % 360
            if temp >= 180:
                temp = temp - 180
            if temp not in angs:
                angs.append(temp)
        # print(angs)
        print(len(angs)*2)
