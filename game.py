import random

def main():
    """
    Game Tebakan Angka dengan Kode Rahasia 888
    """
    secret_code = 888
    print("=" * 50)
    print("       SELAMAT DATANG DI GAME TEBAKAN ANGKA")
    print("=" * 50)
    print("\nBerapa kali Anda ingin bermain?")
    
    try:
        jumlah_game = int(input("Masukkan jumlah game (1-5): "))
        if jumlah_game < 1 or jumlah_game > 5:
            print("Jumlah game harus antara 1-5!")
            return
    except ValueError:
        print("Input tidak valid! Harus berupa angka.")
        return
    
    total_poin = 0
    
    for game_ke in range(1, jumlah_game + 1):
        print(f"\n{'=' * 50}")
        print(f"GAME KE-{game_ke}")
        print(f"{'=' * 50}")
        
        # Cek apakah ada yang menebak kode rahasia
        poin = play_game(secret_code)
        total_poin += poin
    
    print(f"\n{'=' * 50}")
    print(f"TOTAL POIN AKHIR: {total_poin}")
    print(f"{'=' * 50}")
    
    if total_poin >= jumlah_game * 20:
        print("🎉 LUAR BIASA! Anda Juara! 🎉")
    elif total_poin >= jumlah_game * 10:
        print("👍 Bagus! Anda Hebat!")
    else:
        print("💪 Terus berlatih, Anda pasti bisa!")

def play_game(secret_code):
    """
    Fungsi untuk bermain satu putaran game
    Poin: 
    - Jika menebak kode rahasia 888 = 50 poin bonus
    - Setiap tebakan yang lebih dekat dengan angka = poin
    """
    random_angka = random.randint(100, 999)
    kesempatan = 7
    poin = 0
    tebakan_sebelumnya = []
    
    print(f"Saya sudah memikirkan angka antara 100-999")
    print(f"Anda memiliki {kesempatan} kesempatan untuk menebak")
    print(f"\n💡 PETUNJUK: Ada kode rahasia tersembunyi (888)")
    print(f"Jika Anda menemukan kode rahasia, Anda akan mendapat bonus 50 poin!\n")
    
    while kesempatan > 0:
        try:
            tebakan = int(input(f"Tebakan ke-{8-kesempatan} (kesempatan tersisa: {kesempatan}): "))
            
            # Validasi input
            if tebakan < 100 or tebakan > 999:
                print("⚠️  Angka harus antara 100-999!")
                continue
            
            if tebakan in tebakan_sebelumnya:
                print("⚠️  Anda sudah menebak angka ini!")
                continue
            
            tebakan_sebelumnya.append(tebakan)
            kesempatan -= 1
            
            # CEK KODE RAHASIA
            if tebakan == secret_code:
                print(f"\n🎯 SELAMAT!!! Anda menemukan KODE RAHASIA: {secret_code}!")
                print(f"🌟 BONUS 50 POIN! 🌟\n")
                poin += 50
                return poin
            
            # Cek apakah tebakan benar
            if tebakan == random_angka:
                poin = 30 - (7 - kesempatan) * 2  # Semakin cepat menebak, semakin banyak poin
                print(f"\n✅ BENAR! Angka yang saya pikirkan adalah {random_angka}!")
                print(f"Anda membutuhkan {7 - kesempatan} kali tebakan untuk menebaknya.")
                print(f"Poin yang didapat: {poin}\n")
                return poin
            
            # Berikan petunjuk
            if tebakan > random_angka:
                print(f"↓ Angka terlalu BESAR. Coba lebih kecil!")
            else:
                print(f"↑ Angka terlalu KECIL. Coba lebih besar!")
            
            # Hint tentang kode rahasia
            if kesempatan == 3:
                print(f"💡 Petunjuk: Kode rahasia dimulai dengan 8...")
            if kesempatan == 1:
                print(f"💡 Petunjuk akhir: Angka yang mirip dengan tahun adalah kode rahasia!")
        
        except ValueError:
            print("⚠️  Input tidak valid! Masukkan angka saja.")
            continue
    
    print(f"\n❌ HABIS! Angka yang saya pikirkan adalah {random_angka}.")
    print(f"Kesempatan Anda telah habis. Poin: 0\n")
    return 0

if __name__ == "__main__":
    main()
