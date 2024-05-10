import re


N = int(input())


for i in range(N):
    i = input()
    s = i.split()
    if len(s)>1  and  '{' not in s:
        x = re.findall(r'#[a-fA-F0-9]{3,6}', i)
        [print(j) for  j in x]