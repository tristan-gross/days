if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    content = fichier.read()
    monTableau = [i for i in content.split("\n")]
    y=0
    x = 0
    for d in monTableau:

        moncode = d.split(":")
        mdp = d.split(" ")[2]
        lettre = d.split(" ")[1].split(":")[0]
        mini = int(d.split(" ")[0].split('-')[0])
        maxi = int(d.split(" ")[0].split('-')[1])

        z = 0
        v = 0
        v2 = 0
        for l in mdp:
            z=z+1
            if z==mini:
                if l==lettre:
                    v = 1
            if z== maxi:
                if l==lettre:
                    v2 = 1
        if v2 != v:
            x=x+1
    print(x)





    print(y)
