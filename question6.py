x = "100,150,180"

def calculate(D, H=30, C=50):
    return round(((2*C*D)/H)**0.5)

l = x.split(',')

res = ','.join([str(calculate(int(D))) for D in l])
print (res)