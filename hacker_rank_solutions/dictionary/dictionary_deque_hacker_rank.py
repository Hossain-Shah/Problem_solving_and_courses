from collections import deque


N = int(input())
operations = deque()


for i in range(N):
    operations_name, *operations_values = input().split()
    if operations_values:
        num1 = int(operations_values[0])
    if operations_name == 'append':
        operations.append(num1)
    elif operations_name == 'appendleft':
        operations.appendleft(num1)
    elif operations_name == 'pop':
        operations.pop()
    elif operations_name == 'popleft':
        operations.popleft()
        
        
for i in range(len(operations)):
    print(operations.popleft(), end = ' ')