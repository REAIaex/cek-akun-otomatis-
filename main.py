import os
import time
from colorama import Fore, Back, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk membersihkan terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan logo berwarna merah
def tampilkan_logo():
    logo = """
 █████╗ ███████╗██╗  ██╗    ██████╗ ███████╗ █████╗ ██╗     
██╔══██╗██╔════╝╚██╗██╔╝    ██╔══██╗██╔════╝██╔══██╗██║     
███████║█████╗   ╚███╔╝     ██████╔╝█████╗  ███████║██║     
██╔══██║██╔══╝   ██╔██╗     ██╔══██╗██╔══╝  ██╔══██║██║     
██║  ██║███████╗██╔╝ ██╗    ██║  ██║███████╗██║  ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
"""
    print(Fore.RED + logo)

# Fungsi untuk menampilkan note dalam kolom
def tampilkan_note():
    print(Back.YELLOW + Fore.BLACK + "┌───────────────────────────────────────────────────────┐")
    print(Back.YELLOW + Fore.BLACK + "│  Note: Harap setting proxy terlebih dahulu sebelum    │")
    print(Back.YELLOW + Fore.BLACK + "│  menjalankan program agar tidak terjadi kesalahan.    │")
    print(Back.YELLOW + Fore.BLACK + "└───────────────────────────────────────────────────────┘\n")

# Fungsi untuk menampilkan menu dengan kolom
def tampilkan_menu():
    print(Fore.GREEN + "tindakan:")
    print(Back.WHITE + Fore.BLACK + "┌───────────────────────────────────────────────┐")
    print(Back.WHITE + Fore.BLACK + "│  [1] Buka Results Otomatis                    │")
    print(Back.WHITE + Fore.BLACK + "│  [2] Buka Setujui Masuk                       │")
    print(Back.WHITE + Fore.BLACK + "│  [3] VDA Google                               │")
    print(Back.WHITE + Fore.BLACK + "│  [4] Setting Proxy                            │")
    print(Back.WHITE + Fore.BLACK + "└───────────────────────────────────────────────┘")

# Fungsi untuk menjalankan res.php
def buka_results_otomatis():
    print("\nMembuka results otomatis...")
    time.sleep(2)
    os.system("php res.php")

# Fungsi untuk membuka sesi.py
def buka_sesi():
    print("\nMengalihkan ke sesi masuk...")
    os.system("python sesi.py")

# Fungsi untuk menjalankan vda.py
def jalankan_vda():
    print("\nVerifikasi tanpa Google...")
    os.system("python vda.py")

# Fungsi pengaturan proxy dan menyimpan ke proxy.txt
def atur_proxy():
    # Menjalankan proxy.py tanpa input dari pengguna
    os.system("python proxy.py")
    

# Main program
if __name__ == "__main__":
    clear_terminal()  # Bersihkan terminal
    tampilkan_logo()
    tampilkan_note()
    tampilkan_menu()
    
    pilihan = input(Fore.GREEN + "\nMasukkan pilihan : ")

    if pilihan == "1":
        buka_results_otomatis()
    elif pilihan == "2":
        buka_sesi()
    elif pilihan == "3":
        jalankan_vda()
    elif pilihan == "4":
        atur_proxy()
    else:
        print(Fore.RED + "pilih yang benar goblok sesui nomer.")