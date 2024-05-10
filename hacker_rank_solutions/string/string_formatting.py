def print_formatted(number):
    l = len(bin(number)) - 2
    for i in range(1, number + 1):
        f = ""
        for c in "doXb":
            if f:
                f += " "
            f += "{:>" + str(l) + c + "}"
        print(f.format(i, i, i, i))