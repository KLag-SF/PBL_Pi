from sys import argv
path1 = argv[1]
path2 = argv[2]
skip_letter = [" ", "\n"]
i = 0

with open(path1, 'r') as f1, open(path2, 'r') as f2:
    s1 = f1.read()
    s2 = f2.read()

    """for i in range(len(s1)):
        try:
            if (s1[i] in skip_letter) or (s2[i] in skip_letter):
                continue
            elif s1[i] != s2[i]:
                print(s1[i - 5 : i + 5])
                print(s2[i - 5 : i + 5])
                print(str(i) + "digits correct.")
                break
        except IndexError:
            print(str(i) + "digits correct.")
            break
    """

    while(s1[i] == s2[i]):
        try:
            if (s1[i] in skip_letter) or (s2[i] in skip_letter):
                pass
            else:
                i += 1
        except IndexError:
            print("Reached EOF.")
            print(str(i) + "digits correct.")
            break
    else:
        print(s1[i - 5 : i + 5])
        print(s2[i - 5 : i + 5])
        print(str(i) + "digits correct.")
    