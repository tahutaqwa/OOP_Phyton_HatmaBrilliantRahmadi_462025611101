class DompetDigital:
    def __init__(self, nama, pin, saldo_awal):
        self.__nama = nama          # private
        self.__pin = pin            # private
        self.__saldo = saldo_awal   # private

    # --- Getter ---
    def get_nama(self):
        return self.__nama

    def get_saldo(self, pin):
        if pin == self.__pin:
            return f"Saldo kamu: Rp {self.__saldo:,}"
        else:
            return "PIN salah! Akses ditolak."

    # --- Validasi: Transfer ---
    def transfer(self, pin, jumlah, tujuan):
        if pin != self.__pin:
            return "PIN salah! Transfer dibatalkan."
        if jumlah > self.__saldo:
            return "Saldo tidak cukup!"
        self.__saldo -= jumlah
        return f"Transfer Rp {jumlah:,} ke {tujuan} berhasil. Sisa saldo: Rp {self.__saldo:,}"

    # --- Validasi: Ganti PIN ---
    def ganti_pin(self, pin_lama, pin_baru):
        if pin_lama != self.__pin:
            return "PIN lama salah! Gagal mengganti PIN."
        self.__pin = pin_baru
        return "PIN berhasil diganti."


# --- Instansiasi ---
akun = DompetDigital("Budi Santoso", "1234", 500000)

# Getter
print("Nama:", akun.get_nama())

# Cek saldo - PIN benar
print(akun.get_saldo("1234"))

# Cek saldo - PIN salah
print(akun.get_saldo("0000"))

print()

# Transfer - PIN benar
print(akun.transfer("1234", 150000, "Siti"))

# Transfer - PIN salah
print(akun.transfer("9999", 100000, "Andi"))

print()

# Ganti PIN - benar
print(akun.ganti_pin("1234", "5678"))

# Ganti PIN - PIN lama salah
print(akun.ganti_pin("1234", "0000"))

print()

# Bukti atribut private tidak bisa diakses langsung dari luar
# akun.__saldo  --> akan error: AttributeError
try:
    print(akun.__saldo)
except AttributeError as e:
    print(f"Terbukti! Atribut private tidak bisa diakses langsung: {e}")
