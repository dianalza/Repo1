#Ex_1 - Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else.
# Functia "if else" executa anumite comenzi cand o conditie este adevarata si alte comenzi cand aceasta este falsa.
# Prin aceasta functie reusim sa controlam fluxul unui program, executand blocuri specifice de cod in functie de valoarea unor date.

#Ex_2 - Verifica si afiseaza daca x este numar natural sau nu.
x = 3
if x >= 0:
    print('Numarul este natural')
else:
    print('Numarul nu este natural')

#Ex_3 - Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru.
x = 3
if x > 0:
    print ('Numar pozitiv')
elif x == 0:
    print ('Numar neutru')
elif x < 0:
    print('Numar negativ')

#Ex_4 - Verifica si afiseaza daca x este intre -2 si 13.
x = 3
if (x >= -2 and x <= 13):
    print ('True')
else:
    print('False')

#Ex_5 - Verifica si afiseaza daca diferenta dintre X si Y este mai mica de 5.
x=30
y=5
if x-y < 5:
    print('True')
else:
    print('False')

#Ex_6 - Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’).
x = 30
if not (x >= 5 and x <= 27):
    print ('True')
else:
    print ('False')

#Ex_7 - X si Y (int) Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare.
x = 24
y = 9
if x == y:
    print('Numerele X si Y sunt egale')
elif x > y:
    print('Valoarea lui X este mai mare decat valoarea lui Y')
else:
    print('Valoarea lui Y e mai mare decat valoarea lui X')

#Ex_8 - X, Y, Z - laturile unui triunghi. Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
x = 12
y = 20
z = 12
if x == y == z:
    print('Triunghi echilateral')
elif (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print('Triunghi isoscel')
elif x != y != z:
    print ('Triunghi oarecare')

#Ex_9 - Citeste o litera de la tastatura. Verifica si afiseaza daca este vocala sau nu.
litera = str (input('Introdu o litera:'))
litera = litera.lower()
if litera.isdigit():
    print('Nu ai introdus o litera, ci altceva')
elif litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print('Vocala')
else:
    print('Nu e vocala')

#Ex_10 - Transforma si printeaza notele din sistem romanesc in  >
x = 4
if (x >=9 or x >=10):
    print('A')
elif x >= 8:
    print('B')
elif x >= 7:
    print('C')
elif x >= 6:
    print('D')
elif x > 4:
    print('E')
elif (x >= 4 or x > 0):
    print('F')
else:
    print('Nu ati afisat o nota de la 0 la 10')

#Ex_11.Verifica daca X are minim 4 cifre (x e int) Ex: 7895 are 4 cifre, 10 nu are minim 4 cifre).

x = 13567
if (x > 999 or x <-999):
     print('Are minim 4 cifre')
else:
    print('Nu are minim 4 cifre')

#Ex_12 - Verifica daca x are exact 6 cifre.

if len(str(x)) == 6:
        print('Are exact 6 cifre')
else:
        print('Nu are exact 6 cifre')

#Ex_13 - Verifica daca x este numar par sau impar (x e int).
x = 8
if (x % 2 == 0):
        print('Numar par')
else:
        print('Numar impar')

#Ex_14 - x, y, z (int). Afiseaza care este cel mai mare dintre ele?
x = 20
y = 40
z = 50
if (x>=y and x>=z):
    print('X este cel mai mare')
elif (y>=x and y>=z):
    print('Y este cel mai mare')
else:
    print('Z este cel mai mare')

#Ex_15 - x, y, z - reprezinta unghiurile unui triunghi. Verifica si afiseaza daca triunghiul este valid sau nu.
x = 90
y = 60
z = 120
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print ('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

#Ex_16 - Avand stringul: 'Coral is either the stupidest animal or the smartest rock'·
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
prop = 'Coral is either the stupidest animal or the smartest rock'
x = int (input('Introdu un numar:'))
print (prop[0:-x])

#Ex_17 - Acelasi string. Declara un string nou care sa fie format din primele 5 caractere + ultimele 5.
prop = 'Coral is either the stupidest animal or the smartest rock'
prop2 = prop[:5] + prop[-5:]
print('String nou:', prop2)

#Ex_18. acelasi string. Salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '
prop = 'Coral is either the stupidest animal or the smartest rock'
prop_2 = prop.split()
print(prop_2)
prop_3 = prop_2[9]
print(prop_3)
print(prop_3[:1])
print(" ".join(prop_2[0:9]))
#alta varianta
string = 'Coral is either the stupidest animal or the smartest rock'
index_rock = string.index('rock')
print(string[:index_rock])


#Ex_19.  - citeste de la tastatura un string. verifica daca primul si ultimul caracter sunt la fel
#se va folosi un assert
#atentie: se doreste ca programul sa fie case insensitive
#'apA' e acceptat
s = input("Pune un string: ")
s = s.lower()
assert s[0] == s[-1], 'Primul si ultimul caracter sunt diferite'

#Ex_20.- Avand stringul '0123456789'
#afisati doar numerele pare
#acum afisati doar numerele impare
#hint: folositi slicing, controlati din pas)

string = '0123456789'
print(string[0::2])
print(string[1::2]) #string indexing




