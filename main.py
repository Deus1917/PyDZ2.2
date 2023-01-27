class Avtobus():
    list_passjir = []

    def __init__(self, speed, maxkol, maxSpeeds, passajirs, svobodapopugaem, seats, i=0, list_passjir=[]):
        self.speed = speed
        self.maxkol = maxkol
        self.maxSpeeds = maxSpeeds
        self.passajirs = passajirs
        self.svobodapopugaem = svobodapopugaem
        self.seats = seats
        while i < passajirs:
            familia = (input("Введите фамилию пассажира: "))
            self.list_passjir.append(familia)
            i = i + 1
        i = 0
        while i < passajirs:
            print(i)
            print(self.list_passjir[i])
            i = i + 1

    def posadka(self):
        vopros = int(input("Что вы хотите сделать: высадить(1) или посадить(2) пассажиров?"))
        if vopros == 1:
            vibros = int(input("Сколько вы хотите высадить пассажиров?"))
            self.svobodapopugaem = self.svobodapopugaem + vibros
            print(f"Было высаженно {vibros} человек, теперь свободно {self.svobodapopugaem} мест")
        elif vopros == 2:
            zaxod = int(input("Сколько вы хотите посадить пассажиров?"))
            self.svobodapopugaem = self.svobodapopugaem - zaxod
            print(f"Было посажено {zaxod} человек, теперь свободно {self.svobodapopugaem} мест")
        else:
            print("Error, неправильно введены данные, попробуйте заново")

    def skorost(self):
        vopros2 = input("Что вы хотите сделать: увеличить(up) или уменьшить(down) скорость?")
        if vopros2 == "up":
            speed_up = int(input("Введите значение, на которое хотите увеличить скорость автобуса"))
            self.speed = self.speed + speed_up
            print(f"Теперь скорость равна {self.speed} км/ч")
        elif vopros2 == "down":
            speed_down = int(input("Введите значение, на которое хотите уменьшить скорость"))
            self.speed = self.speed - speed_down
            print(f"Теперь скорость равна {self.speed} км/ч")
        else:
            print("Error, неправильно введены данные, попробуйте снова")

    def zadan_famil(self, i=0):
        vopros3 = int(input("Что вы хотите сделать: высадить(1) или посадить(2) пассажира(ов)?"))
        while i < len(self.list_passjir):
            print(f"Пассажир {i} = {self.list_passjir[i]}")
            i = i + 1
        i = 0
        if vopros3 == 1:
            vopros4 = int(input("Сколкьо вы хотите использовать пассажиров?"))
            while i < vopros4:
                vopros0 = input("Введите фамилию пассажира")
                self.list_passjir.remove(vopros0)
                i = i + 1
            i = 0
        elif vopros3 == 2:
            vopros5 = int(input("Сколкьо вы хотите использовать пассажиров?"))
            while i < vopros5:
                vopros01_1 = input("Введите фамилию пассажира")
                self.list_passjir.append(vopros01_1)
                i = i + 1
            i = 0
        while i < len(self.list_passjir):
            print(f"Пассажир {i} = {self.list_passjir[i]}")
            i = i + 1
        i = 0

Avtobus71 = Avtobus(60, 40, 120, 3, 5, 10)
Avtobus71.posadka()
Avtobus71.skorost()
Avtobus71.zadan_famil()
