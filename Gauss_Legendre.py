import math
from decimal import Decimal

def gauss(a, b, t, p):
    new_a = (a + b) / 2
    new_b = (a * b) ** Decimal('0.5')
    new_t = t - p * ((a - new_a) ** 2)
    new_p = 2 * p
    return (new_a, new_b, new_t, new_p)

def calc(a, b, t, p):
    return ((a + b) ** 2) / (4 * t)

def main():
    a = 1
    b = Decimal('0.5') * Decimal('2') ** Decimal('0.5')
    t = Decimal('0.25')
    p = 1

    nums = (a, b, t, p)

    loop = int(input("Input number of times to calculate. > "))

    count = 0
    
    for i in range(loop):
        print(str(count)+ ":" + str(calc(*nums)))
        nums = gauss(*nums)
        count += 1
    
main()