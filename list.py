makanan = ["Nasi Goreng", "Mie Ayam", "Bakso", "Rendang"]

print("Daftar Makanan:")
for m in makanan:
    print("-", m)

makanan.append("Ayam Geprek")
makanan.remove("Bakso")

print("\nDaftar Makanan Terbaru:")
for m in makanan:
    print("-", m)
