import re


def valid_uid(i):
    if len(re.findall(r"[A-Z]", i)) < 2 or \
            len(re.findall(r"[0-9]", i)) < 3 or \
            not re.match(r"[A-Za-z0-9]{10}$", i) or \
            len(set(i)) != len(i):
        return False
    
    return True

T = int(input())


for i in range(T):
    i = input()
    
    if valid_uid(i):
        print('Valid')
    else:
        print('Invalid')