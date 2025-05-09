def func(x):
    dict1 = {}
    for i in range (1, x+1):
        dict1[i] = i*i
    return dict1

n= int(input("n = "))
print(func(n))