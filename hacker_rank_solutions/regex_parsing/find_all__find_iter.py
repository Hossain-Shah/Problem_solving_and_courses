import re


S = input()
match = re.findall(r"(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])", S, re.IGNORECASE)

if match:
    print(*match, sep="\n")
else:
    print(-1)
