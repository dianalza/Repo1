#Ex_1 - Explica ce este o variabila
# o variabila este o parte din memoria calculatorului care pastreaza date

#Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:

prenume = "Diana" #variabiila de tip string
varsta = 27 #variabila de yip integer
inaltime = 1.74 #variabila de tip float
sex_feminin = True #variabila de tip boolean


print(f'Ma numesc {prenume}, am {27} de ani, inaltimea mea este de {inaltime} cm si sexul meu este feminin {sex_feminin}')

#Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.

print(type(prenume)) # python automatically converts nume to str
print(type(varsta)) # python automatically converts varsta to int
print(type(inaltime)) # python automatically converts inaltime to float
print(type(sex_feminin)) # python automatically converts sex_feminin to bool

#Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere),
# apoi verifică din nou tipul de date al acesteia.

inaltime = round(1.74)
print(inaltime)
print(type(inaltime))

#Ex_5 - Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin orice modalitate dorești (type casting, printare cu formatare).

nume = "Laza"
prenume = "Diana"
varsta = 27
inaltime = 1.74
sex_feminin = True
print(f'Numele meu este {prenume} {nume}')
print(f'Diana are varsta de {varsta} ani')
print(f'Diana are intaltimea de {inaltime} cm')
print(f'Sexul Dianei este feminin {sex_feminin}')

#Ex_6 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.

nume = input('Numele este:')
prenume = input('Prenumele este:')
print(f'Numele complet are {len(nume+prenume)} caractere')


#Ex_7 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.

lungime = int(input('Lungimea dreptunghiului este:'))
latime = int(input('Latimea dreptunghiului este:'))
print(f'Aria dreptunghuilui este {lungime * latime} metrii patrati.')

#Ex_8 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare cuvântul 'the' în acest string
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print('Number of occurrence of word "the":',propozitie.count('the'))


#Ex_9 - Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.replace("the","THE"))


#Ex_10 -  Folosindu-te de string-ul de la exercițiul 8 foloseste un assert ca să verifici dacă acest string conține doar numere.
propozitie = 'Coral is either the stupidest animal or the smartest rock'
assert propozitie.isdigit() is True, 'Propozitia nu contine doar cifre'
print('Coral is either the stupidest animal or the smartest rock'.isnumeric()) #varianta alternativa fara asssert

"""
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google)
"""
#Ex_11 - Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
# Nu se va verifica daca string-ul este impar (se presupune ca vom introduce un numar corect de caractere),
#Ci doar se va printa pe ecran caracterul din mijloc.
text = str(input('Scrie un string:'))
print(f'Caractereul din mijloc este:{text[(len(text)//2)]}')

#Ex_12 - Folosind assert, verifică dacă un string este palindrom.
text = 'dad'
assert text == text[::-1], 'Cuvantul nu este palindrom'

#Ex_13 - Citește un string format din 2 cuvinte de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.
text = input('Scrie un string:')
a,b = text.split(' ')
print(f'Primul cuvant este:{a}')
print(f'Ultimul cuvant este: {b}')

#Ex_14 - Citește un text format din 2 cuvinte de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:
# salvează primul caracter într-o variabilă
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
text = input('Scrie un text:')
primul_caracter = text[0]
text_modificat = text [0] + text[1:-1].replace(primul_caracter,primul_caracter.capitalize()) + text[-1]
print(text)
print(text_modificat)

#Ex_15 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere'

user = str (input('User-ul este:'))
parola = str (input('Introdu parola:'))
parola_ascunsa = '*' * len(parola)
print(f'Parola pentru userul {user} este {parola_ascunsa} si are {len(parola)} caractere')