M = int(input())
elements_M = set(map(int, input().split()))

N = int(input())
elements_N = set(map(int, input().split()))

symmetric_different = sorted((elements_M.difference(elements_N)).union(elements_N.difference(elements_M)))

print("\n".join([str(element) for element in symmetric_different]))