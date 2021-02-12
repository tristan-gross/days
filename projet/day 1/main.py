if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    content = fichier.read()
    monTableau = [int(i) for i in content.split('\n')]
    for e in monTableau:
        for d in monTableau:
            for f in monTableau:
                if e + d + f == 2020:
                    print(e, "+", d, "+",f)
                    print(e*d*f)
