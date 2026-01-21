import time
import json
import os

# ===== GLOBAL =====
timeline = []
hp = 100
score = 0
story_log = []   # buat nyimpen cerita tokoh
SAVE_FILE = "save_queens.json"

# ===== UTIL =====
def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def save_game():
    data = {
        "timeline": timeline,
        "hp": hp,
        "score": score,
        "story_log": story_log
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_game():
    global timeline, hp, score, story_log
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            timeline = data["timeline"]
            hp = data["hp"]
            score = data["score"]
            story_log = data["story_log"]
        slow_print("Save game dimuat 📂")
    else:
        slow_print("Belum ada save game.")

# ===== OPENING =====
def opening():
    slow_print("=== QUEENS OF HISTORY 👑 ===")
    slow_print("Kamu adalah penjelajah waktu.")
    slow_print("Setiap pilihanmu akan membentuk sejarah.\n")

# ===== MENU =====
def main_menu():
    print("1. Main Baru")
    print("2. Load Game")
    print("3. Keluar")
    return input("Pilih: ")

def choose_character():
    slow_print("\nPilih tokoh:")
    print("1. R.A. Kartini")
    print("2. Marie Curie")
    print("3. Cleopatra")
    print("4. Malala")
    return input("Masukkan pilihan: ")

# ===== STORIES =====
def kartini_story():
    global hp, score
    slow_print("\n[KARTINI]")
    slow_print("Kamu hidup di masa perempuan tidak bebas sekolah.")
    print("A. Menulis surat ke Belanda")
    print("B. Menerima nasib")
    choice = input("Pilihan: ")

    if choice.upper() == "A":
        slow_print("Kamu menulis surat penuh harapan tentang kebebasan perempuan.")
        quiz = input("Quiz: Buku Kartini berjudul? ")
        if "gelap" in quiz.lower():
            timeline.append("R.A. Kartini")
            score += 25
            story_log.append(
                "Kartini menyalakan cahaya pendidikan bagi perempuan Indonesia."
            )
            slow_print("Suratmu mengubah sejarah. ✅")
        else:
            hp -= 10
            slow_print("Suratmu kurang dikenal. Sejarah hampir hilang.")
    else:
        hp -= 20
        slow_print("Kartini terkurung adat. Mimpinya padam.")

def curie_story():
    global hp, score
    slow_print("\n[MARIE CURIE]")
    slow_print("Kamu menemukan zat bercahaya misterius.")
    print("A. Menelitinya")
    print("B. Mengabaikannya")
    choice = input("Pilihan: ")

    if choice.upper() == "A":
        slow_print("Kamu bekerja siang malam di laboratorium.")
        quiz = input("Quiz: Unsur yang ditemukan? ")
        if "radium" in quiz.lower() or "polonium" in quiz.lower():
            timeline.append("Marie Curie")
            score += 25
            story_log.append(
                "Marie Curie membuka jalan ilmu radioaktivitas bagi dunia."
            )
            slow_print("Penemuanmu mengubah sains dunia. ✅")
        else:
            hp -= 10
            slow_print("Penelitianmu gagal dipahami dunia.")
    else:
        hp -= 20
        slow_print("Penemuan besar tak pernah terjadi.")

def cleopatra_story():
    global hp, score
    slow_print("\n[CLEOPATRA]")
    slow_print("Mesir terancam kekuasaan Romawi.")
    print("A. Diplomasi")
    print("B. Perang")
    choice = input("Pilihan: ")

    if choice.upper() == "A":
        slow_print("Kamu memilih kecerdikan daripada kekerasan.")
        quiz = input("Quiz: Negara asal Cleopatra? ")
        if "mesir" in quiz.lower():
            timeline.append("Cleopatra")
            score += 25
            story_log.append(
                "Cleopatra mempertahankan Mesir dengan strategi dan diplomasi."
            )
            slow_print("Kamu menjadi ratu legendaris. ✅")
        else:
            hp -= 10
            slow_print("Strategimu gagal dimengerti.")
    else:
        hp -= 15
        slow_print("Perang menghancurkan Mesir.")

def malala_story():
    global hp, score
    slow_print("\n[MALALA]")
    slow_print("Anak perempuan dilarang sekolah.")
    print("A. Berpidato ke dunia")
    print("B. Diam demi keselamatan")
    choice = input("Pilihan: ")

    if choice.upper() == "A":
        slow_print("Suaramu menggema ke seluruh dunia.")
        quiz = input("Quiz: Nobel bidang apa? ")
        if "damai" in quiz.lower():
            timeline.append("Malala")
            score += 25
            story_log.append(
                "Malala menjadi simbol perjuangan pendidikan dunia."
            )
            slow_print("Dunia terinspirasi. ✅")
        else:
            hp -= 10
            slow_print("Pesanmu belum didengar.")
    else:
        hp -= 20
        slow_print("Perjuangan berhenti karena rasa takut.")

# ===== STATUS =====
def show_status():
    print("\n=== STATUS ===")
    print("HP:", hp)
    print("Score:", score)
    print("Timeline:", timeline)
    print(f"Progress: {len(timeline)}/4")

# ===== EPILOG =====
def epilog():
    slow_print("\n=== EPILOG SEJARAH 👑 ===")
    slow_print("Perjalanan waktumu selesai...")
    slow_print("Inilah kisah yang berhasil kamu buka:\n")

    for story in story_log:
        slow_print("- " + story)

    slow_print("\nKamu belajar bahwa sejarah bukan tentang kekuasaan...")
    slow_print("tapi tentang keberanian perempuan untuk bersuara.")
    slow_print("\nFINAL SCORE: " + str(score))

# ===== MAIN GAME LOOP =====
def game_loop():
    global hp
    while hp > 0:
        if len(timeline) == 4:
            epilog()
            break

        choice = choose_character()
        if choice == "1" and "R.A. Kartini" not in timeline:
            kartini_story()
        elif choice == "2" and "Marie Curie" not in timeline:
            curie_story()
        elif choice == "3" and "Cleopatra" not in timeline:
            cleopatra_story()
        elif choice == "4" and "Malala" not in timeline:
            malala_story()
        else:
            slow_print("Tokoh sudah dipilih atau pilihan tidak valid.")

        show_status()
        save_game()

    if hp <= 0:
        slow_print("\n=== BAD ENDING ===")
        slow_print("Kamu kehabisan energi.")
        slow_print("Sejarah perempuan tetap terkunci...")

# ===== PROGRAM START =====
opening()
menu = main_menu()

if menu == "1":
    game_loop()
elif menu == "2":
    load_game()
    game_loop()
else:
    slow_print("Keluar dari game.")
