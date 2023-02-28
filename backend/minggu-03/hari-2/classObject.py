class Person:
    def __init__ (self, name, money):
        self.name = name
        self.money = money
    
    def sisa_uang(self):
        print (f"uang {self.name} sisa {self.money}")
    def pinjam(self, other, jumlah):
        print (f"{self.name} meminjam uang {other.name} sebanyak {jumlah}")
        self.money += jumlah
        self.sisa_uang()
        other.dipinjam(self)
        other.money -= jumlah
        other.sisa_uang()
    def dipinjam(self, other):
        print (f"uang {self.name} dipinjam {other.name}")
        self.sisa_uang()

budi = Person('budi', 100)
andi = Person('andi', 200)
budi.pinjam(andi, 10)
# andi.pinjam(budi, 10)
# budi.dipinjam(andi)

