import time
import sys
import os

# Lirik lagu Stecu
lyrics = [
    "Aduh abang bukan maksud ku begitu, BEHH",
    "Masalah stecu bukan berarti tak mauuu..",
    "Jual mahal dikit kan bisa, HORASS",
    "Coba kasih effortnya saja, BEHH",
    
    "Kalau memang cocok bisa datang kerumah",
    "STECU STECU setelan cuek tapi baru mau",
    "Aduh adek ini mau juga abang yang rayu, BEHH HORAS..",
    "STECU STECU setelan cuek tapi baru mau",
    
    "Aduh adek ini mau juga abang yang maju, ha horaas"
]

# Kecepatan penulisan
char_speed = 0.06  # kecepatan per huruf
line_delay = 1.7   # jeda antar baris

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def karaoke_lirik(lyrics, char_speed, line_delay):
    clear_screen()
    print("🎶 STECU v.Batak 🎶\n")
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_speed)
        print()  # baris baru setelah 1 baris lirik
        time.sleep(line_delay)

        # Tambahkan spasi setiap 4 baris (kecuali setelah baris terakhir)
        if (i + 1) % 4 == 0 and i + 1 != len(lyrics):
            print()  # baris kosong sebagai jarak

    print("\n🎵 End 🎵")

# Jalankan
karaoke_lirik(lyrics, char_speed, line_delay)
