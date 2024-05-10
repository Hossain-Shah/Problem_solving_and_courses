from itertools import combinations


S, k = input().split()
k = int(k)

for r in range(1, k+1):
    print('\n'.join(sorted(''.join(sorted(p)) for p in combinations(S,r))))