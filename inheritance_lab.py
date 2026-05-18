class Staff:
    def __init__(self, nama, keahlian, **kwargs):
        self.nama = nama
        self.keahlian = keahlian

    def identitas(self):
        print(f"[Staff] Nama: {self.nama} | Keahlian: {self.keahlian}")

    def __str__(self):
        return (f"nama     : {self.nama}\n"
                f"keahlian : {self.keahlian}")


class StaffDokter(Staff):
    def __init__(self, nama, keahlian, spesialis, **kwargs):
        super().__init__(nama=nama, keahlian=keahlian, **kwargs)
        self.spesialis = spesialis

    def identitas(self):
        print(f"[Dokter] {self.nama} | Spesialis: {self.spesialis}")
        super().identitas()

    def diagnosa(self):
        print(f"{self.nama} sedang melakukan diagnosa pasien.")


class StaffSuster(Staff):
    def __init__(self, nama, keahlian, bidang, **kwargs):
        super().__init__(nama=nama, keahlian=keahlian, **kwargs)
        self.bidang = bidang

    def identitas(self):
        print(f"[Suster] {self.nama} | Bidang: {self.bidang}")
        super().identitas()

    def rawat(self):
        print(f"{self.nama} sedang merawat pasien.")


class DokterJaga(StaffDokter, StaffSuster):
    def __init__(self, nama, keahlian, spesialis, bidang):
        super().__init__(nama=nama, keahlian=keahlian, spesialis=spesialis, bidang=bidang)

    def identitas(self):
        print(f"[DokterJaga] {self.nama} bertugas malam ini.")
        super().identitas()


# ============================================

if __name__ == "__main__":
    print("=" * 45)
    print("   SISTEM RUMAH SAKIT - DIAMOND PROBLEM")
    print("=" * 45)

    dj = DokterJaga("Dr. Andi", "Medis Umum", "Bedah", "ICU")

    print("\nIdentitas Lengkap :")
    dj.identitas()

    print("\nStatus Dokter :")
    dj.diagnosa()

    print("\nStatus Suster :")
    dj.rawat()

    print("\nInfo Staff :")
    print(dj)
