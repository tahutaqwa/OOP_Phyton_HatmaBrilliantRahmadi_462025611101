class Instansi:
    def __init__(self, nama, umur, jk, jabatan):
        self.nama = nama
        self.umur = umur
        self.jk = jk
        self.jabatan = jabatan
        
        if self.jk == "L":
            self.sebutan = "Tuan"
        else:
            self.sebutan = "Nyonya"

    def __str__(self):
        return (f"Nama    : {self.sebutan} {self.nama}\n"
                f"Umur    : {self.umur} tahun\n"
                f"JK      : {self.jk}\n"
                f"Jabatan : {self.jabatan}")

user_1 = Instansi("Budi Santoso", 30, "L", "Manager")
print(user_1)

print()

user_2 = Instansi("Siti Rahayu", 25, "P", "Staff")
print(user_2)