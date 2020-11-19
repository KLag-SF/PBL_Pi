def main():
    pi = 0
    loop = int(input(" > "))
    
    for i in range(loop):
        a = (-1) ** i / (2 * i + 1)
        b = (1 / 5) ** (2 * i + 1)
        c = ((-1) ** (i + 1)) / (2 * i + 1)
        d = (1 / 239) ** (2 * i + 1)
        
        pi += 4 * a * b + c * d
    
    print(4 * pi)

main()