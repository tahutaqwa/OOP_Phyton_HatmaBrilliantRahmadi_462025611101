class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return (f"Produk : {self.nama}\n"
                f"Harga  : Rp {self.harga:,}\n"
                f"Stok   : {self.stok} pcs")

    def __eq__(self, other):
        return self.harga == other.harga

    def __lt__(self, other):
        return self.harga < other.harga

    def __gt__(self, other):
        return self.harga > other.harga

    def __le__(self, other):
        return self.harga <= other.harga


# --- 3 Objek ---
p1 = Produk("Laptop", 12000000, 5)
p2 = Produk("Mouse", 250000, 50)
p3 = Produk("Monitor", 3500000, 10)

# Print objek (__str__)
print(p1)
print()
print(p2)
print()
print(p3)
print()

# Perbandingan antar objek
print("--- Hasil Perbandingan ---")
print(f"Laptop == Mouse   : {p1 == p2}")   # __eq__
print(f"Mouse < Monitor   : {p2 < p3}")    # __lt__
print(f"Laptop > Monitor  : {p1 > p3}")    # __gt__
print(f"Mouse <= Monitor  : {p2 <= p3}")   # __le__
