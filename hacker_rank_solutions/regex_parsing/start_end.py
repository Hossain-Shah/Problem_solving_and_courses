import re


S = input()
k = input()

match = re.compile(k).search(S)


if not match:
    print("(-1, -1)")


while match:
    print((match.start(), match.end() - 1))
    # print("({0}, {1})".format(match.start(), match.end() - 1))
    match = re.compile(k).search(S,match.start() + 1)