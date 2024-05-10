A = set(map(int, input().split()))
n = int(input())


for i in range(n):
    x = set(map(int, input().split()))
    if A.issuperset(x) != True or len(A) == len(x): 
        print(False)
        break 
else:
    print(True)