from itertools import combinations_with_replacement


S, k = input().split()
k = int(k)

print('\n'.join(sorted(''.join(sorted(c)) for c in combinations_with_replacement(S,k))))
