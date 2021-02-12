if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    largeur = len(fichier.readline())
    montableau=[fichier.read().split('\n')]
    increment=0
    y=0
    x = 0
     while montableau:

        print(montableau)
        if x == largeur:
            y = y + 1
            x = 0

