import math
from decimal import *

getcontext().prec = 1000

def gauss(a, b, t, p):
    new_a = (a + b) / 2
    new_b = (a * b) ** Decimal('0.5')
    new_t = t - p * ((a - new_a) ** 2)
    new_p = 2 * p
    return (new_a, new_b, new_t, new_p)

def calc(a, b, t, p):
    pi = ((a + b) ** 2) / (4 * t)
    return pi

def main():

    a = 1
    b = Decimal('0.5') * Decimal('2') ** Decimal('0.5')
    t = Decimal('0.25')
    p = 1

    nums = (a, b, t, p)

    loop = int(input("Input number of times to calculate. > "))

    count = 0
    
    for i in range(loop):
        #pi = calc(*nums)
        #pi_length = len(str(pi))
        #print(str(count)+ ":" + str(pi) + ", " + str(pi_length))
        nums = gauss(*nums)
        #count += 1
    
    print(calc(*nums))

main()