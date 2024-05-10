N, X = map(int, input().split())
average = []


for i in range(X):
    average.append(map(float, input().split()))
    
    
for j in zip(*average): 
    print(sum(j)/len(j))