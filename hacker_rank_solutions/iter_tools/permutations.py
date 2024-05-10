from itertools import permutations


S, k = input().split()
k = int(k)

print('\n'.join(sorted(''.join(p) for p in permutations(S,k))))