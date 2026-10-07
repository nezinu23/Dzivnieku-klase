import random


class Dzivnieks:
    def __init__(self, vards, vecums, svars):
        self.vards = vards
        self.vecums = vecums
        self.svars = svars

    def apraksts(self):
        print("Vards:", self.vards)
        print("Vecums:", self.vecums, "gadi")
        print("Svars:", self.svars, "kg")

    def svara_statuss(self):
        if self.svars < 10:
            print("Mazs dzivnieks")
        else:
            print("Liels dzivnieks")


class Suns(Dzivnieks):
    def __init__(self, vards, vecums, svars, skirne):
        super().__init__(vards, vecums, svars)
        self.skirne = skirne

    def apraksts(self):
        super().apraksts()
        print("Skirne:", self.skirne)


dzivnieki = [
    Dzivnieks("Muris", 3, 5),
    Dzivnieks("Puka", 7, 12),
    Suns("Reksis", 5, 20, "Vacu aitu suns")
]


def videjais_vecums(dzivnieki):
    summa = 0

    for dzivnieks in dzivnieki:
        summa += dzivnieks.vecums

    return summa / len(dzivnieki)


for dzivnieks in dzivnieki:
    print("--------------------")
    dzivnieks.apraksts()
    dzivnieks.svara_statuss()


print("--------------------")
print("Videjais vecums:", videjais_vecums(dzivnieki), "gadi")


nejauks = random.choice(dzivnieki)

print("--------------------")
print("Nejauši izvelets dzivnieks:", nejauks.vards)
