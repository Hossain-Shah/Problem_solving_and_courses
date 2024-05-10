T = int(input())


for i in range(T):
    a = int(input()); A = input().split()
    b = int(input()); B = input().split()
    
    if(len(set(A) - set(B))==0):
        print("True")
    else:
        print("False")