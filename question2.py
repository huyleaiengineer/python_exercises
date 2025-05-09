def fact(x):
    if x < 2:
        return 0
    sum = 1
    for i in range(2, x+1):
        sum *= i
    return sum

x = int(input("x = "))
print(fact(x))