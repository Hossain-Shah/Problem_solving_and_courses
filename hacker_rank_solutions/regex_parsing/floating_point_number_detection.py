import re
T = int(input())
N = []

for i in range(T):
    i = input()
    N.append(i)
    
    
for i in N: 
    print(bool(re.search(r"^[-+]?[0-9]*\.[0-9]+$", i)))