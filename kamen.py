print("")
hrac = input('Zadej svoje jméno: ')
print("")
print("Tak ty jsi", hrac, ". Ahoj.")
dotaz = "Můžeme hrát? "

print('něco')
for i in range(100):
    print("")
    start = input(dotaz)
    if  start == 'ano':
        print("")
        print("Hrajeme ...")
        print("")

        from random import randrange
        pocitac = randrange(0, 3)
        if pocitac == 0:
            tah_pocitace = 'kámen'
        if pocitac == 1:
            tah_pocitace ="nůžky"
        if pocitac == 1:
            tah_pocitace ="papír"

        tah_cloveka = input('Jsi na tahu. kámen, nůžky nebo papír? ')
        print("")
        print("Já hraju ", tah_pocitace)
        print("")
        dotaz = "Můžeme pokračovat? "
        if tah_cloveka == 'kámen':
            if tah_pocitace == 'kámen':
                print('Plichta.')
            elif tah_pocitace == 'nůžky':
                print('Vyhrála jsi!')
            elif tah_pocitace == 'papír':
                print('Vyhrál jsem.')
        elif tah_cloveka == 'nůžky':
            if tah_pocitace == 'kámen':
                print('Vyhrál jsem.')
            elif tah_pocitace == 'nůžky':
                print('Plichta.')
            elif tah_pocitace == 'papír':
                print('Vyhrála jsi!')
        elif tah_cloveka == 'papír':
            if tah_pocitace == 'kámen':
                print('Vyhrála jsi!')
            elif tah_pocitace == 'nůžky':
                print('Vyhrál jsem.')
            elif tah_pocitace == 'papír':
                print('Plichta.')
        else:
            print('Nerozumím.')

    elif start == 'ne':
        print('')
        print('Tak tedy ne ...')
        break
    elif start != 'ne':
        print('')
        print('Nerozumím ... končíme :(')
        break
