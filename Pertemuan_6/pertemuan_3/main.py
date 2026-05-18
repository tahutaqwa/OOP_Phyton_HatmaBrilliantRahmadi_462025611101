class Instansi:
    def __init__(self, nama, umur, jabatan, gelar, exp):
        self.nama = nama
        self.umur = umur
        self.jabatan = jabatan
        self.gelar = gelar
        self.exp = exp
        self.level_kerja = Instansi.level(self.exp)

    def __str__(self):
        return (f"Nama    : {self.nama}\n"
                f"Umur    : {self.umur} tahun\n"
                f"Jabatan : {self.jabatan}\n"
                f"gelar   : {self.gelar}\n"
                f"level   : {self.level_kerja}"
                )
        
    def ubah_gelar(self, gelar_baru):
        self.gelar = gelar_baru
        return f"{self.gelar}"
    
    @staticmethod
    def level(exp):
        if exp < 2:
            return "Junior"
        elif exp < 5:
            return "Mid-level"
        else:
            return "Senior"
        
user_1 = Instansi("Budi Santoso", 30, "team marketing", "S2", 6)
print(user_1)

print()

user_2 = Instansi("Siti Rahayu", 25, "Staff", "S1", 3)
print(user_2)