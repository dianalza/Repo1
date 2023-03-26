#Ex_1 - Declara o lista note_muzicale in care sa pui do re mi etc pana la do
#a. Afiseaz-o
#b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza varianta actuala (inversata)
#c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la varianta inițială
#Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim in acel moment.

note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
note_muzicale2 = note_muzicale[::-1] #inversam ordinea prin slicing + suprascriem lista
print(note_muzicale2)
note_muzicale2.reverse() #metoda prin care inversam ordinea listei automat
print('Reversed list:', note_muzicale2)

#Ex_2 - Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale.count('do'))

#Ex_3 - Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1+lista2 #toate se adauga intr-o lista noua 'lista3'
lista1.extend(lista2) #adaugi elemente intr-o lista existenta 'adaugam elementele din lista 2 in lista 2'
print(f'lista3 este: {lista3}')
print(f'lista1 extinsa este: {lista1}')

#Ex_4 - Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista folosind o functie si apoi afiseaza din nou lista
lista3.sort() #sortam lista
print(lista3)
lista3.pop(0) #stergem numarul 0 din lista
print(lista3)

#Ex_5 - Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
#- Lista este goala (IF)
#- Lista nu este goala (ELSE)
if not lista3:
   print('Empty list')
else:
   print('List is not Empty \n',lista3)

#Ex_6 - Foloseste o functie care sa goleasca lista de la exercitiul 3.
lista3.clear()
print(lista3)

#Ex_7 - Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala
if not lista3:
   print('Empty list')
else:
   print('List is not Empty \n',lista3)

#Ex_8 - Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa afisezi Elevii (cheile)
dict1 = {'Ana' : 8,
         'Gigel' : 10,
         'Dorel' : 5
         }
print(dict1.keys())

#Ex_9 - Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
#Ex: ‘Ana a luat nota {x}’.
#Doar nota o vei lua folosindu-te de cheie
print(f'Ana a luat nota:', dict1.get('Ana'))
print(f'Gigel a luat nota:', dict1.get('Gigel'))
print(f'Dorel a luat nota:', dict1.get('Dorel'))

#Ex_10 - Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
#Modifica nota lui Dorel in 6
#Printeaza nota lui dupa modificare
dict1['Dorel'] = 6
print(f'Dorel a luat nota',dict1.get('Dorel'),'dupa contestatie')

#Ex_11 - Imagineaza-ti ca Gigel se transfera din clasa.
# Cauta o functie care sa il stearga
# Vine un coleg nou.
# Adaugati-l in lista pe Ionica, cu nota 9
# Printati dictionarul cu noii elevi
dict1.pop('Gigel')
print(dict1) #l-am sters pe Gigel din dict
dict1['Ionica'] = 9
print(dict1) #l-am adaugat pe Ionica cu nota 9 in dict


#Ex_12 - Ai urmatoarele seturi:
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
#Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
#Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt) #zilele saptamanii au ramas aceleasi deoarece ziua de luni era in lista iar seturile nu accepta valori duplicate (ele sunt unice), de asemenea valorile si-au schimbat ordinea

#Ex_13 - Foloseste un if si verifica daca:
# Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se regasesc intre elementele din setul zile_sapt)
# Weekend nu este un subset al zilelor din sapt
# Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui punct de mai sus va fi un boolean
if weekend.issubset(zile_sapt):
    print ('True')
else:
    print('False')

#Ex_14 - Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu sunt in weekend si invers)
print(zile_sapt.difference(weekend)) #returns a set with elements unique to set zile_sapt
print(weekend.difference(zile_sapt)) #returns a set with elements unique to set weekend

#Ex_15 - Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in ambele seturi). Hint: Va puteti folosi de o functie
print(zile_sapt.intersection(weekend)) #returns a new set with elements that are common to all sets


#EXERCITII OPTIONALE

#1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
lista_jucatori_teren= ['Messi','Xavi','Araujo','Torres','Busquets']
lista_jucatori_rezerva= ['Dembele','Leva','Pedri','Gavi','Pique']
lista_jucatori_scosi = []
schimbari_efectuate = 0
SCHIMBARI_MAX = 3

# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
if ('Araujo' in lista_jucatori_teren and SCHIMBARI_MAX >= 3):
    print(f'Araujo e in teren si mai avem {SCHIMBARI_MAX} schimbari la dizpozitie')

# Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe teren
lista_jucatori_teren[2]= 'Leva' #Schimbam pe Araujo cu Leva
print(lista_jucatori_teren)
schimbari_efectuate = 1
print(schimbari_efectuate)

# Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
lista_jucatori_scosi.append('Araujo')
print(lista_jucatori_scosi)

# Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori de rezerva
lista_jucatori_rezerva.pop(1)
print(lista_jucatori_rezerva)

# Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele variabilelor voastre)
print(f'A intrat {lista_jucatori_teren[2]}, a iesit {lista_jucatori_scosi[0]}. Mai avem {SCHIMBARI_MAX-1} schimbari')

# Daca jucatorul pe care vrem sa il schimbam nu e in teren:
# Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Altfel, afisati ecran: ‘mai aveti z schimbari’
if 'Kessie' not in lista_jucatori_teren:
	print (f'Nu se poate efectua schimbarea deoarece Kessie nu e in teren')
else:
    print (f'Mai aveti {SCHIMBARI_MAX-1} schimbari')