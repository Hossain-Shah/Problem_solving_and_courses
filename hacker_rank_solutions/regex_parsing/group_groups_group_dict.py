import re
S = input()
match = re.search(r'([0-9a-zA-Z])\1', S)
print(match.group(1) if match else -1)