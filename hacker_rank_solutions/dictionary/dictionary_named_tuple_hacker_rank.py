N = int(input())
student_data = list(input().split())
sum = 0


for i in range(N):
    sum += int(list(input().split())[student_data.index('MARKS')])
    

print(sum/N)