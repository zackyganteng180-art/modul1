class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def tampilkan_hasil(self):
        print(f"Panjang   : {self.panjang}")
        print(f"Lebar     : {self.lebar}")
        print(f"Luas      : {self.hitung_luas()}")
        print(f"Keliling  : {self.hitung_keliling()}")

# Program utama
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

pp = PersegiPanjang(panjang, lebar)
pp.tampilkan_hasil()
