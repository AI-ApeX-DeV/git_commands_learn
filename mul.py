def mul(a, b):
    return a*b


a = 10
b = 20
print(mul(a, b))
# lets check for conflicts


def mul1(a, b, c):
    return a*b*c


c = 30
print(mul1(a, b, c))
