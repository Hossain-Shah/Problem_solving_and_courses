import email.utils
import re


n = int(input())


for i in range(n):
    i = input()
    pattern_matched = re.search(r'<[a-zA-Z][\w\.-]*@[a-zA-Z]*\.[a-zA-Z]{1,3}>', i)
    if bool(pattern_matched):
        print(i)