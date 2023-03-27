'''ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui'''
print('-----------EX 2----------')

class GeometricShape:
    PI = 3.14

    def area(self):
        pass

    def describe(self):
        print("Most probably have corners")


class Square(GeometricShape):
    def __init__(self, side):
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value

    @side.deleter
    def side(self):
        del self.__side

    def area(self):
        return self.side ** 2


class Circle(GeometricShape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    @radius.deleter
    def radius(self):
        del self.__radius

    def area(self):
        return self.PI * self.radius ** 2

    def describe(self):
        print("I have no corners")


# Create a Square object and play with its methods
square = Square(5)
print(square.side)  # Output: 5
square.side = 10
print(square.area())  # Output: 100
square.describe()  # Output: Most probably have corners

# Create a Circle object and play with its methods
circle = Circle(3)
print(circle.radius)  # Output: 3
circle.radius = 5
print(circle.area())  # Output: 78.5
circle.describe()  # Output: I have no corners
