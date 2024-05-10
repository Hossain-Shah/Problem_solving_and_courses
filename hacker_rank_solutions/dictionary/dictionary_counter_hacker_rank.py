from collections import Counter


X = int(input())
M = Counter(map(int, input().split()))
N = int(input())
sum = 0


for i in range(N):    
    shoe_size_info, x = map(int, input().split())
    if M[shoe_size_info]: 
        sum = sum + x
        M[shoe_size_info] -= 1
print(sum)