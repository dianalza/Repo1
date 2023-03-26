#Ex_1 - Având lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
#Folosește un for că să iterezi prin toată lista și să afișezi;
#'Mașina mea preferată este x’.
# Fă același lucru cu un for each.
# Fă același lucru cu un while.

for i in range (len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

# for each
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# while
i = 0
while i < len(masini):
  print(f'Masina mea preferata este', masini[i])
  i = i + 1

#Ex_2 -  Aceeași listă:
#Folosește un for else
#În for: Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
#În else: Printează lista.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
for i in masini:
    print(i.removeprefix('Audi').removesuffix('Opel').upper())
else:
    print(masini)

#Ex_3 - Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes: Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel: Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

for x in masini:
    if x == 'Mercedes':
        print('Am gasit masina dorita de dvs')
        break
    else:
        print(f'Am gasit masina {x}. Mai cautam')

#Ex_4 - Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# Dacă mașina e Trabant sau Lăstun: Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# Printează S-ar putea să vă placă mașina x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

for x in masini:
    if x == 'Lastun' or x == 'Trabant':
        continue
    print(f'S-ar putea să vă placă mașina {x}')

#Ex_5 - Modernizează parcul de mașini:
#Crează o listă goală, masini_vechi.
#Itereaza prin mașini.
#Când găsesti Lăstun sau Trabant: - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# Printează Modele vechi: x.
# Modele noi: x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
masini_vechi = []

for x in range(len(masini)):
    if masini[x] == 'Lastun' or masini[x] == 'Trabant':
        masini_vechi.append(masini[x])
        masini[x] = 'Tesla'

print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

#Ex_6 - Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
#Vine un client cu un buget de 15000 euro.
# Prezintă doar mașinile care se încadrează în acest buget.
# Itereaza prin dict.items() și accesează mașina și prețul.
# Printează Pentru un buget de sub 15000 euro puteți alege mașină x Lastun
# Iterează prin listă.


for key, value in pret_masini.items():
    if value <= 15000:
        print(f'Pentru un buget de sub 15000 euro puteți alege mașină', key, 'la pretul de', value,'euro')

#Ex_7 - Având lista: numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print("3 occurrence: ",len([i for i in numere if i==3]))

#Ex_8 - Aceeași listă:
# Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s=0
for numar in numere:
    s=s + numar
print(f'Suma totala a numerelor este {s}')

#Ex_9- Aceeași listă:
# Iterează prin ea.
# Afișază cel mai mare număr (nu ai voie să folosești max).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
largest_number = None
for number in numere:
    if largest_number is None or largest_number < number:
        largest_number = number
print(f'Cel mai mare numar este', largest_number)

#Ex_10 - Aceeași listă:
# Iterează prin ea.
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă. Ex: dacă e 3, să devină -3
# Afișază noua listă.

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3] #itineram prin lista si schimbam valoarea numerelor
for i in range(len(numere)):
    numere[i] = -numere[i]
print(numere)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]  #schimbam valoarea direct
numerenoi= [ -x for x in numere]
print(numerenoi)


