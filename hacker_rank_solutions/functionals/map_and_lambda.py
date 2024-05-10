cube = lambda x:x**3 

def fibonacci(n):
    list = [0, 1]
    for i in range(2, n):
        list.append(list[i-1] + list[i-2])
    return(list[0:n])