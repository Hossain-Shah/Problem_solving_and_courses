N = int(input())
conditions = list(input().split())


if all (int(i)>0 for i in conditions) and any(i ==i[::-1] for i in conditions):
    print ('True')
else: 
    print('False')