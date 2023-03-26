#1.Clasa Cerc
#Atribute: raza, culoare
#Constructor pentru ambele atribute
#Metode:
# descrie_cerc() - va PRINTA culoarea și raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
print('-------EX 1-----------')
class Cerc:
    raza = 3
    culoare = 'alb'

    # Constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # Methods
    def descriere_cerc(self):
        return f'Cercul are culoarea {self.culoare} si raza {self.raza}'

    def aria(self):
        return 3.14 * self.raza ** 2

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return 2 * 3.14 * self.raza

# create an instance of Cerc class
cerc_nou = Cerc(5,"rosu")

# access fields
print(cerc_nou.raza)
print(cerc_nou.culoare)

# access methods
print(cerc_nou.aria())
print(cerc_nou.diametru())
print(cerc_nou.circumferinta())

#2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
#descrie()
#aria()
#perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
print('--------EX 2--------')

class Dreptunghi:
    lungime = 8
    latime = 4
    culoare = 'mov'

# Constructor

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

# Methods

    def descrie(self):
        return f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}'

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self):
        culoare = 'alb'
        self.culoare = culoare
        print(f'Culoarea dreptunghiului este {self.culoare}')

# create an instance for Dreptunghi class
dreptunghi = Dreptunghi (10,5,'rosu')

# access methods
print(dreptunghi.descrie())
print(dreptunghi.aria())
print(dreptunghi.perimetru())

#3.Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
#descrie()
#nume_complet()
#salariu_lunar()
#salariu_anual()
#marire_salariu(procent)
print('--------EX 3---------')

class Angajat:
    nume = 'Maricica'
    prenume = 'Soare'
    salariu = 7000

# Constructor
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

# Methods

    def descrie(self):
        print(f'Numele meu este {self.nume}, {self.prenume}, iar salariul meu este de ,{self.salariu} ron')

    def nume_complet(self):
        return f'Numele meu complet este {self.nume}, {self.prenume}'

    def salariu_lunar(self):
        return f'Salariul lunar este de {self.salariu} ron'

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        return f'Salariul anual este de {salariu_anual} ron'

    def marire_salariu(self):
        marire_salariu = self.salariu * 1.2
        return f'Marirea salariala a fost de 20%, adica {marire_salariu} ron'

# create an instance for Angajat class
angajat1 = Angajat ('Floricica', 'Ban', 5000)

# access methods
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
print(angajat1.marire_salariu())

# 4 Clasa Cont
#Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
print('-------EX 4----------')

class Cont:
    iban = 'RO1000'
    titular_cont = 'Diana'
    sold = 700

# Constructor
    def __init__(self, iban, titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

# Methods

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def creditare_cont(self, suma):
        self.sold += suma
        print(f'Ati alimentat {suma} lei')

    def debitare_cont(self,suma):
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma} lei')

# create an instance for Cont class
cont1 = Cont('RO200', 'Maria', 400)

#access methods
cont1.afisare_sold()
cont1.debitare_cont(100)
cont1.creditare_cont(200)


