#Ex_1 - Functie care sa calculeze si sa returneze suma a 2 numere
print('-------EX 1-------')
def suma_mea(x, y):
    suma = x + y
    return suma

print(suma_mea(5,10))

#Ex_2 - Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
print('-------EX 2-------')
def numar_par_impar(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(numar_par_impar(4))
print(numar_par_impar(3))

#Ex_3-Functie care returneaza numarul total de caractere din numele tau complet. (nume, prenume, nume_mijlociu)
print('-------EX 3-------')
def numecomplet(name,surname,middlename):
    total_caractere = len(name)+len(surname)+len(middlename)
    return total_caractere
print(numecomplet('Laza', 'Diana', 'Anamaria'))


#Ex_4 - Functie care returneaza aria dreptunghiului.
print('-------EX 4-------')
def aria_dreptunghiului(lungime,latime):
    arie = (lungime * latime)
    return arie
print(aria_dreptunghiului(10,4))
print(aria_dreptunghiului(20,8))

#Ex_5 - Functie care returneaza aria cercului
print('-------EX 5-------')
def aria_cercului(raza):
    arie = 3.14 * (raza*raza)
    return arie
print(aria_cercului(4))
print(aria_cercului(2))

#Ex_6 - Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
print('-------EX 6-------')
def caracterX(string):
    gasitcaracterX = 'X'
    if gasitcaracterX in string:
        return True
    else:
        False
print(caracterX('Afara sunt X grade'))
print(caracterX('Afara sunt 35 de grade'))

#Ex_7. Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y
print('-------EX 7-------')
def numar_caractere(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(f'Nr de caractere lower case este {lower}')
    print(f'Nr de caractere upper case este {upper}')
numar_caractere('Azi am fost la Iulius Mall')

#Ex_8 - Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
print('-------EX 8-------')
def lista (list):
    positive_list = []
    for i in list:
        if i > 0:
            positive_list.append(i)
    return positive_list

print(lista([1,2,-4,6,8,-3]))

#Ex_9 - Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
#Primul numar x este mai mare decat al doilea nr y
#Al doilea nr y este mai mare decat primul nr x
#Numerele sunt egale.
print('-------EX 9-------')
def number(x,y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    elif y > x:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print(f'Numerele sunt egale')
number(7,10)
number(8,8)
number(11,3)

#Ex_10 - Functie care primeste un numar si un set de numere.
#Printeaza ‘am adaugat numarul nou in set’ + returneaza True
#Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
print('-------EX 10-------')

def functie(numar,set):
    if numar not in set:
        set.add(numar)
        print(f'am adaugat numarul nou in set')
        print(set)
        return True
    else:
        print(f'nu am adaugat numarul in set. Acesta exista deja')
        return False

print(functie(1,{2,4,8}))
print(functie(12,{12,13,8}))















