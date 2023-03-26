print('-------EX 5---------')
#Ex - 5. Clasa Factura
#Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#Constructor: toate atributele, fara serie
#Metode:
#schimba_cantitatea(cantitate)
#schimba_pretul(pret)
#schimba_nume_produs(nume)
#genereaza_factura() - va printa tabelar daca reusiti

#Factura seria x numar y
#Data: generati automat data de azi
#Produs | cantitate | pret bucata | Total
#Telefon |      7       |       700       | 49000

from datetime import date

class Invoice:

    # Constants
    SERIE = "INV2023"

    # Constructor
    def __init__(self, number, product_name, quantity, price_unit):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.price_unit = price_unit

    # Methods
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

    def change_price(self, new_price):
        self.price_unit = new_price

    def change_product_name(self, new_product_name):
        self.product_name = new_product_name

    def generate_invoice(self):
        # Calculate the total price
        total = self.quantity * self.price_unit

        # Create the table
        table = f"Invoice serie {self.SERIE} number {self.number}\n"
        table += f"Date: {date.today().strftime('%Y-%m-%d')}\n"
        table += f"Product    | quantity | price/unit   | Total\n"
        table += f"{self.product_name.ljust(10)} |{self.quantity:^9}|{self.price_unit:^9.2f}|{total:^7.2f}\n"

        return table

# Create an invoice
invoice = Invoice(22, "Rose", 100, 5)

# Print the invoice table
print(invoice.generate_invoice())

# Change the quantity and price
invoice.change_quantity(70)
invoice.change_price(7)

# Print the updated invoice table
print(invoice.generate_invoice())


#Ex - 6 Clasa Masina
#Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
#Constructor: model, viteza_maxima
#Metode:
#descrie() (se vor printa toate atributele, inafara de culori_disponibile)
#inmatriculare() - va schimba atributul inmatriculata in True
#vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
#accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
#franeaza() - masina se va opri si va avea viteza 0

print('-------EX 6---------')

class Masina:

#atribute/fields
    marca = 'Volvo'
    model = 'SUV'
    viteza_maxima = 240
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'alb','rosu','negru','albastru','argintiu'}
    inmatriculare = False

#Constructor

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
#Methods

    def descrie(self): #se vor printa toate atributele, inafara de culori_disponibile)
        print(f'Marca {self.marca}')
        print(f'Model {self.model}')
        print(f'Viteza maxima {self.viteza_maxima} km/h')
        print(f'Viteza actuala {self.viteza_actuala} km/h')
        print(f'Culoare {self.culoare}')
        print(f'Inmatriculare {self.inmatriculare}')


    def inmatriculare(self): #va schimba atributul inmatriculata in True
        return self.inmatriculare == True

    def vopseste(self,culoare): #se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f"Masina a fost vopsita in culoarea {culoare}.")
        else:
            print(f'Error: Culoarea {culoare} nu exista in lista de culori')

    def accelereaza(self,viteza): #se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
        if viteza < 0:
            print(f'Error: viteza nu poate avea valoare negativa')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self): #masina se va opri si va avea viteza 0
        self.viteza_actuala = 0

Masina1 = Masina('X40',180)
Masina1.descrie()
Masina1.inmatriculare()
Masina1.vopseste('portocaliu')
Masina1.accelereaza(240)
Masina1.franeaza()


#Ex-7 Clasa TodoList
#Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
#La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
#Metode:
#adauga_task(nume, descriere) - se va adauga in dict
#finalizează_task(nume) - se va sterge din dict
#afișează_todo_list() - doar cheile
#afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
#Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
#Dacă acesta răspunde nu - la revedere
#Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict

class Todolist:
    def __init__(self):
        self.todo = {}

    def add_task(self, name, description):
        self.todo[name] = description

    def finalize_task(self, name):
        del self.todo[name]

    def display_todo_list(self):
        print("Todo list:")
        for task_name in self.todo:
            print("- " + task_name)

    def display_addition_details(self, task_name):
        if task_name in self.todo:
            print(f"Task: {task_name}")
            print(f"Description: {self.todo[task_name]}")
        else:
            answer = input(f"Task '{task_name}' not found. Do you want to add it? (y/n) ")
            if answer.lower() == "y":
                description = input(f"Enter task description for '{task_name}': ")
                self.add_task(task_name, description)
                print(f"Task '{task_name}' added to the list.")
            else:
                print("Goodbye.")


# Create a new todo list
my_todolist = Todolist()

# Add some tasks
my_todolist.add_task("Buy groceries", "Milk, eggs, bread, cheese")
my_todolist.add_task("Clean the house", "Vacuum, mop, dust")

# Display the list of tasks
my_todolist.display_todo_list()

# Display details of a task
my_todolist.display_addition_details("Buy groceries")
my_todolist.display_addition_details("Do laundry")

# Add a new task
my_todolist.display_addition_details("Take out the trash")


