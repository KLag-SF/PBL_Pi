from sys import argv

path = argv[1]
with open(path, 'r+') as f:
    lines = f.readlines()
    res = ""
    for l in lines:
        l.replace(" ", "").replace("\n", "")
        res += l

    f.write(res)