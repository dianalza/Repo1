#Exerciții Bonus

# 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept inputuri urmatoarele informatii:
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata
#
# Conditii de imbarcare:
# Daca pers are varsta peste 18 ani si are pasaport
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
#
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate variantele care crezi ca ar trebui testate.
                        # Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
#
# Exemple:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca

varsta = int(input('Introdu varsta copilului.\n'))
pasaport = bool(input('Introdu TRUE/False daca ai pasaport!\n'))

if varsta >= 18 and pasaport is True:
    print(f'Persoana are {varsta} am pasaport.Ma pot imbarca!')
elif varsta < 18:
    if pasaport is True:
        insotit_de_mama = bool(input('Introdu TRUE/False daca merge cu MAMA!\n'))
        insotit_de_tata = bool(input('Introdu TRUE/False daca merge cu TATA!\n'))
        if insotit_de_mama is True and insotit_de_tata is True:
            print(f'Persoana are {varsta} merg cu Mama si Tata. se poate imbarca.')
        elif insotit_de_mama is True and insotit_de_tata is False:
            act_permisiune_tata = bool(input('Introdu TRUE/False daca ai Permisiune de la Tata!\n'))
            if act_permisiune_tata is True:
                print(f'Persoana are {varsta} Merge cu Mama, are permisiune tata. Se poate imbarca.')
            else:
                print(f'Persoana are {varsta} merge insotit de mama dar nu are permisiunea tatalui. NU se poate imbarca!')
        elif insotit_de_mama is False and insotit_de_tata is True:
            act_permisiune_mama = input('Introdu TRUE/False daca ai Permisiune de la Mama!\n')
            if act_permisiune_mama is True:
                print(f'Persoana are {varsta} Merge cu tata, are permisiune mama. Se poate imbarca.')
            else:
                print(f'Persoana are {varsta} merge insotit de tata dar nu are permisiunea mamei. NU se poate imbarca!')
        else:
            print(f'Persoana are {varsta} si are pasaport dar nu e insotit de nici un parinte. NU se poate imbarca!')
    else:
        print(f'Persoana are {varsta} nu are pasaport.NU se poate imbarca!')
else:
    print('Nu am pasaport! Nu ma pot imbarca!')

"""
Scenarii de testare:
1. Adult peste 18 ani cu pasaport valid => Se poate imbarca
2. Adult peste 18 ani cu pasaport invalid => Nu se poate imbarca
3. Copil cu pasaport valid si ambii parinti => Se poate imbarca
4. Copil cu pasaport valid si un singur parinte - permisiune parinte lipsa => Se poate imbarca
5. Copil cu pasaport valid si un singur parinte - fara permisiune parinte lipsa => Nu se poate imbarca
6. Copil fara pasaport valid => Nu se poate imbarca
"""

# 2. Joc de noroc
# Cauta pe net si vezi cum se genereaza un numar random
# Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll. Numarul salvat va fi generat random cu metoda gasita in online
# Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
# Verifica si afiseaza daca utilizatorul a ghicit numarul
# Vor exista 3 optiuni care vor trebui tratate:
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y


import random
dice_roll = random.randint(0, 6)
guess = int(input('Ghiceste zarul'))
if guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}')
elif guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {guess} si zarul a fost {dice_roll}')