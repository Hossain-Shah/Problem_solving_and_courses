n = int(input())
s = set(map(int, input().split()))
N = int(input())


for i in range(N):
    operations = input().split()
    if(operations[0]) == "remove":
        s.remove(int(operations[1]))
    elif(operations[0]) == "discard":
        s.discard(int(operations[1]))
    else:
        s.pop()
    
print(sum(s))