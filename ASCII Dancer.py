# 90%

import copy


def turn(s):
    s_copy = copy.deepcopy(s)

    if s_copy[0][0] == "(":
        s[0][2] = ")"
        s[1][2] = " "
    if s_copy[0][2] == ")":
        s[0][0] = "("
        s[1][0] = " "

    if s_copy[1][0] == "<":
        s[0][2] = " "
        s[1][2] = ">"
    elif s_copy[1][0] == "/":
        s[0][2] = " "
        s[1][2] = "\\"
    if s_copy[1][2] == ">":
        s[0][0] = " "
        s[1][0] = "<"
    elif s_copy[1][2] == "\\":
        s[0][0] = " "
        s[1][0] = "/"

    if s_copy[2][0] == "/":
        s[2][2] = "\\"
    elif s_copy[2][0] == "<":
        s[2][2] = ">"

    if s_copy[2][2] == ">":
        s[2][0] = "<"
    elif s_copy[2][2] == "\\":
        s[2][0] = "/"


t = int(input())
for _ in range(t):
    d = int(input())
    s = [[" ", "o", " "], ["/", "|", "\\"], ["/", " ", "\\"]]
    facing_forward = True
    for i in range(d):
        c = input()
        if c[:3] == "say":
            print(c[4:])
        else:
            if c == "left hand to head":
                if facing_forward:
                    s[0][2] = ")"
                    s[1][2] = " "
                else:
                    s[0][0] = "("
                    s[1][0] = " "
            elif c == "left hand to hip":
                if facing_forward:
                    s[0][2] = " "
                    s[1][2] = ">"
                else:
                    s[0][0] = " "
                    s[1][0] = "<"
            elif c == "left hand to start":
                if facing_forward:
                    s[0][2] = " "
                    s[1][2] = "\\"
                else:
                    s[0][0] = " "
                    s[1][0] = "/"
            elif c == "left leg in":
                if facing_forward:
                    s[2][2] = ">"
                    s[2][0] = "/"
                else:
                    s[2][0] = "<"
                    s[2][2] = "\\"
            elif c == "left leg out":
                if facing_forward:
                    s[2][2] = "\\"
                else:
                    s[2][0] = "/"
            elif c == "right hand to head":
                if facing_forward:
                    s[0][0] = "("
                    s[1][0] = " "
                else:
                    s[0][2] = ")"
                    s[1][2] = " "
            elif c == "right hand to hip":
                if facing_forward:
                    s[0][0] = " "
                    s[1][0] = "<"
                else:
                    s[0][2] = " "
                    s[1][2] = ">"
            elif c == "right hand to start":
                if facing_forward:
                    s[0][0] = " "
                    s[1][0] = "/"
                else:
                    s[0][2] = " "
                    s[1][2] = "\\"
            elif c == "right leg in":
                if facing_forward:
                    s[2][0] = "<"
                    s[2][2] = "\\"
                else:
                    s[2][2] = ">"
                    s[2][0] = "/"
            elif c == "right leg out":
                if facing_forward:
                    s[2][0] = "/"
                else:
                    s[2][2] = "\\"
            elif "turn":
                turn(s)
            for x in s:
                print("".join(x))
