# https://csacademy.com/ieeextreme-practice/task/array/
# 20%

n, m, p = map(int, input().strip().split())
rules = []
for _ in range(m):
    l, r, k = map(int, input().strip().split())
    rules.append([l-1, r-1, k])

rules.sort()
arr = [0]*n
locked = []
for rule in rules:
    l, r, k = rule[0], rule[1], rule[2]
    rule_satisfaction = False
    for i in range(r, l-1, -1):
        if i in locked:
            continue
        else:
            summ = sum(arr[l:r+1])
            if k-summ >= 0:
                arr[i] = k-summ
            else:
                arr[i] = p+k-summ
            rule_satisfaction = True
            locked.extend(list(range(l, r+1)))
            break

    if not (rule_satisfaction):
        print("None")
        quit()

print(*arr)
