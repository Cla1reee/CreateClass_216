class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

panjang = float(input("Masukkan panjang persegi panjang (cm): "))
lebar = float(input("Masukkan lebar persegi panjang (cm): "))

persegi_panjang = PersegiPanjang(panjang, lebar)

keliling = persegi_panjang.hitung_keliling()
luas = persegi_panjang.hitung_luas()

print(persegi_panjang)
print(f"Keliling: {keliling} cm")
print(f"Luas: {luas} cm²")
