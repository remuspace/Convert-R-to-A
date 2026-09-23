def unos():
    ulaz = input()
    return ulaz


def unos_lista(ulaz):
    ulaz_lista = ulaz.replace(',', '')
    ulaz_lista = ulaz_lista.replace('.', '')
    ulaz_lista = ulaz_lista.split()
    return ulaz_lista


def uzmi_velike_reci(reci):
    velike_reci = []
    for i in range(len(reci)):
        if reci[i].isupper():
            velike_reci.append(reci[i])
    return velike_reci


def proveri(velike_reci):
    rimski = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    for rec in velike_reci:
        for slovo in rec:
            if slovo not in rimski: return False

    return True


def konvertuj(velika_rec):
    rimski = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arapski = [1, 5, 10, 50, 100, 500, 1000]
    slova = list(velika_rec)
    suma = 0
    br = 0
    while br < len(slova):
        gledaj_dalje = True
        if br + 1 < len(slova):
            if slova[br] not in ['I', 'X', 'C']:
                index = rimski.index(slova[br])
                broj = arapski[index]
                suma += broj
            else:
                for x in range((len(rimski) - 1) // 2):
                    if slova[br] == rimski[2 * x] and gledaj_dalje:  # IV
                        for y in range(len(rimski)):
                            if y > 2 * x and slova[br + 1] == rimski[y]:
                                broj = arapski[y] - arapski[2 * x]
                                suma += broj
                                br += 1
                                gledaj_dalje = False
                                break
                        if not gledaj_dalje: break

                        if gledaj_dalje:  # II
                            suma += arapski[2 * x]
                            break
        else:
            index = rimski.index(slova[br])
            broj = arapski[index]
            suma += broj

        br += 1

    return suma


def modifikuj(ulaz, reci, velike_reci):
    reci_tz = ulaz.split()
    izlaz_lista = []
    for i in range(len(velike_reci)):
        arapski_broj = str(konvertuj(velike_reci[i]))

        for n in range(len(reci)):
            if reci[n] == velike_reci[i]:
                reci_tz[n] = reci_tz[n].replace(velike_reci[i], arapski_broj)

        izlaz_lista = reci_tz
    izlaz = ' '.join(izlaz_lista)
    return izlaz


recenica = unos()
reci_bez_tz = unos_lista(recenica)
reci_velike = uzmi_velike_reci(reci_bez_tz)

if proveri(reci_velike):
    print(modifikuj(recenica, reci_bez_tz, reci_velike), end="")
