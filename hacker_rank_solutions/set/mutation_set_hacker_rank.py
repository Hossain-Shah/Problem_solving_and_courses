elements_A = input()
A = set(map(int, input().split()))

N = int(input())


for i in range(N):
    elements_B = input().strip().split(); B = set(map(int, input().split()))
    eval("A." + elements_B[0] + "(  B  )")
print(sum(A))
