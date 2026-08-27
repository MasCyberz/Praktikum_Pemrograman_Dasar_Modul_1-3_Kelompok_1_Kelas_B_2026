class Dosen:
    def __init__(self, nama, nidn, mata_kuliah):
        self.nama = nama
        self.nidn = nidn
        self.matkul = mata_kuliah

    def info(self):
        print(f"Nama dosen: {self.nama}\nNidn: {self.nidn}\nMata kuliah: {self.matkul}")

    def update_mata_kuliah(self):
        mk_baru = (input("masukan nama mata kuliah baru: "))
        self.matkul = mk_baru
        print(f"Nama dosen: {self.nama}\nNidn: {self.nidn}\nMata kuliah: {self.matkul}")
  

dsn1 = Dosen("andre", 123, "astronomi")
dsn2 = Dosen("Dimas", 456, "Perkembangbiakan tumbuhan")
dsn3 = Dosen("Justin", 789, "kriminalogi")

dsn1.info()
dsn2.info()
dsn3.info()
dsn1.update_mata_kuliah()

