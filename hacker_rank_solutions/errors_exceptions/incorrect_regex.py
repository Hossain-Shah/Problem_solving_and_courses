import re


T = int(input())


for i in range(T):
    S = input()
    try:
        print(bool(re.compile(S)))
    except re.error:
        print('False')