import re


N = int(input())


for i in range(N):
    i = input()
    match = re.match(r'^[7-9]{1}[0-9]{9}\n?\r?$', i)
    
    
    if match:
        print('YES')
    else:
        print('NO')