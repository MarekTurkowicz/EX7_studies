class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def przesun(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x},{self.y})"


class Linia:
    def __init__(self, p1=Punkt(), p2=Punkt()):
        self.p1 = Punkt(p1.x, p1.y)
        self.p2 = Punkt(p2.x, p2.y)

    def przesun(self, dx, dy):
        self.p1.przesun(dx, dy)
        self.p2.przesun(dx, dy)

    def __str__(self):
        return f"{self.p1} -> {self.p2}"


class Trojkat:
    def __init__(self, l1=Linia(), l2=Linia(), l3=Linia()):
        self.l1 = Linia(l1.p1, l1.p2)
        self.l2 = Linia(l2.p1, l2.p2)
        self.l3 = Linia(l3.p1, l3.p2)

    def przesun(self, dx, dy):
        self.l1.przesun(dx, dy)
        self.l2.przesun(dx, dy)
        self.l3.przesun(dx, dy)

    def __str__(self):
        return f"Trojkaty: {self.l1}, {self.l2}, {self.l3}"


class Czworokat:
    def __init__(self, l1=Linia(), l2=Linia(), l3=Linia(), l4=Linia()):
        self.l1 = Linia(l1.p1, l1.p2)
        self.l2 = Linia(l2.p1, l2.p2)
        self.l3 = Linia(l3.p1, l3.p2)
        self.l4 = Linia(l4.p1, l4.p2)

    def przesun(self, dx, dy):
        self.l1.przesun(dx, dy)
        self.l2.przesun(dx, dy)
        self.l3.przesun(dx, dy)
        self.l4.przesun(dx, dy)

    def __str__(self):
        return f"Czworokat: {self.l1}, {self.l2}, {self.l3}, {self.l4}"


class Obraz:
    def __init__(self):
        self.figury = []

    def dodaj_figure(self, figura):
        self.figury.append(figura)

    def przesun(self, dx, dy):
        for element in self.figury:
            element.przesun(dx, dy)

    def __str__(self):
        result = "Trojkaty:\n"
        for figura in self.figury:
            if isinstance(figura, Trojkat):
                result += f"{figura}\n"
        result += "Czworokaty:\n"
        for figura in self.figury:
            if isinstance(figura, Czworokat):
                result += f"{figura}\n"
        return result

obraz = Obraz()
while True:
        #os.system('cls')
        print("Co chcesz zrobic?")
        print("1. Dodaj trojkat")
        print("2. Dodaj czworakat")
        print("3. Przesun trojkaty i czworokaty")
        print("4. Wyswietl trojkaty i czworokaty")
        print("5. Zakoncz")

        wybor = input("Podaj numer opcji: ")

        if wybor == "1":
            p1 = Punkt(int(input("Podaj x1: ")), int(input("Podaj y1: ")))
            p2 = Punkt(int(input("Podaj x2: ")), int(input("Podaj y2: ")))
            p3 = Punkt(int(input("Podaj x3: ")), int(input("Podaj y3: ")))
            trojkat = Trojkat(Linia(p1, p2), Linia(p2, p3), Linia(p3, p1))
            obraz.dodaj_figure(trojkat)
            print("Dodano trojkat")

        elif wybor == "2":
            p1 = Punkt(int(input("Podaj x1: ")), int(input("Podaj y1: ")))
            p2 = Punkt(int(input("Podaj x2: ")), int(input("Podaj y2: ")))
            p3 = Punkt(int(input("Podaj x3: ")), int(input("Podaj y3: ")))
            p4 = Punkt(int(input("Podaj x4: ")), int(input("Podaj y4: ")))
            czworokat = Czworokat(Linia(p1, p2), Linia(p2, p3), Linia(p3, p4), Linia(p4, p1))
            obraz.dodaj_figure(czworokat)
            print("Dodano czworokat")

        elif wybor == "3":
            dx = int(input("Podaj przesuniecie w osi x: "))
            dy = int(input("Podaj przesuniecie w osi y: "))
            obraz.przesun(dx, dy)
            print("Przesunieto")

        elif wybor == "4":
            print(obraz)

        elif wybor == "5":
            print("Koniec programu")
            break

        else:
            print("Niepoprawny wybor")
