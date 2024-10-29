import requests
import os
import time
from colorama import Fore, Back, Style, init

# Inisialisasi colorama
init(autoreset=True)

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

class ProxyConnection:
    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.proxy = f"http://{username}:{password}@{host}:{port}"

    def get_ip_info(self):
        try:
            # Menggunakan proxy untuk mendapatkan informasi IP
            response = requests.get("https://ipinfo.io/json", proxies={"http": self.proxy, "https": self.proxy})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"{Fore.RED}Koneksi gagal: {e}")
            return None

def read_data(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def write_data(filename, data):
    with open(filename, 'w') as file:
        file.writelines(data)

def tampilkan_menu():
    tampilkan_logo()  # Tampilkan logo sebelum menu

    # Menampilkan garis di atas menu pilihan
    print(Back.YELLOW + Fore.BLACK + "┌───────────────────────────────────────────────┐")
    print(Back.YELLOW + Fore.BLACK + "│  Selamat datang!                              │")
    print(Back.YELLOW + Fore.BLACK + "│  Harap add proxy dulu baru di jalankan :      │")
    print(Back.YELLOW + Fore.BLACK + "└───────────────────────────────────────────────┘")
    print()  # Tambahkan baris kosong untuk jarak

    print(Back.WHITE + Fore.BLACK + "┌───────────────────────────────────────────────┐")
    print(Back.WHITE + Fore.BLACK + "│  [1] dataimpluse                              │")
    print(Back.WHITE + Fore.BLACK + "│  [2] superoroxy                               │")
    print(Back.WHITE + Fore.BLACK + "│  [3] proxylab                                 │")
    print(Back.WHITE + Fore.BLACK + "│  [4] custom (belum tersedia)                  │")
    print(Back.WHITE + Fore.BLACK + "│  [5] add proxy                                │")
    print(Back.WHITE + Fore.BLACK + "└───────────────────────────────────────────────┘")

def koneksi_dataimpluse():
    filename = 'dataimpluse.txt'
    data = read_data(filename)

    # Menampilkan isi file dengan warna hijau
    print(Fore.GREEN + "Isi dari dataimpluse.txt:")
    for line in data:
        print(line.strip())

    # Meminta input untuk kode negara
    country_code = input(f"{Fore.RED}Masukkan kode negara (contoh: pk): {Fore.RESET}")

    # Mengupdate username dengan kode negara
    username = data[0].split(': ')[1].strip()  # Mendapatkan username
    username_parts = username.split('.')
    username_parts[-1] = country_code
    new_username = '.'.join(username_parts)
    data[0] = f"username: {new_username}\n"  # Memperbarui username

    # Mendapatkan password, host, dan port dari file
    password = data[1].split(': ')[1].strip()  # Mendapatkan password
    host = data[2].split(': ')[1].strip()      # Mendapatkan host
    port = data[3].split(': ')[1].strip()      # Mendapatkan port

    # Menyimpan perubahan
    write_data(filename, data)

    print(Fore.GREEN + "Data telah diperbarui.")

    # Membuat objek koneksi proxy
    proxy_connection = ProxyConnection(new_username, password, host, port)

    # Mengambil informasi IP
    ip_info = proxy_connection.get_ip_info()
    
    # Menampilkan hasil
    print("\n" + "-" * 50)
    if ip_info:
        print(f"{Fore.GREEN}Koneksi berhasil!")
        print(f"{Fore.YELLOW}{"IP:":<10} {ip_info.get('ip')}")
        print(f"{Fore.YELLOW}{"Kota:":<10} {ip_info.get('city')}")
        print(f"{Fore.YELLOW}{"Wilayah:":<10} {ip_info.get('region')}")
        print(f"{Fore.YELLOW}{"Negara:":<10} {ip_info.get('country')}")
        
        # Menampilkan loading screen dan redirect
        print(f"{Fore.YELLOW}\nKembali ke halaman awal dalam 7 detik...")
        for i in range(7, 0, -1):
            print(f"{Fore.CYAN}Loading... {i} detik tersisa", end="\r")
            time.sleep(1)

        # Mengarahkan kembali ke main.py
        os.system("python main.py")  # Gantilah ini sesuai dengan cara Anda menjalankan main.py

def add_proxy():
    # Menampilkan catatan untuk menambahkan proxy
    print(Back.WHITE + Fore.YELLOW + "┌───────────────────────────────────────────┐")
    print(Back.WHITE + Fore.YELLOW + "│ Catatan: Harap isi sama kayak super proxy │")
    print(Back.WHITE + Fore.YELLOW + "└───────────────────────────────────────────┘")
    
    print()  # Tambahkan baris kosong untuk jarak

    print(Back.WHITE + Fore.YELLOW + "┌───────────────────────────────────────────┐")
    print(Back.WHITE + Fore.YELLOW + "│ Setelah proxy berhasil di simpan test dulu│")
    print(Back.WHITE + Fore.YELLOW + "└───────────────────────────────────────────┘")
    
    # Mengambil input dari pengguna
    username = input(f"{Fore.GREEN}Username: {Fore.RESET}")
    password = input(f"{Fore.GREEN}Password: {Fore.RESET}")
    host = input(f"{Fore.GREEN}Proxy Host: {Fore.RESET}")
    port = input(f"{Fore.GREEN}Proxy Port: {Fore.RESET}")

    print(f"{Fore.YELLOW}Ketik 1 untuk simpan, ketik 2 untuk cancel.")
    pilihan = input(f"{Fore.GREEN}Pilihan Anda: {Fore.RESET}")

    if pilihan == '1':
        # Menyimpan data ke file
        data = [
            f"username: {username}\n",
            f"password: {password}\n",
            f"Proxy Host: {host}\n",
            f"Proxy Port: {port}\n"
        ]
        write_data('dataimpluse.txt', data)
        
        # Debug: Menampilkan isi data yang disimpan
        print(Fore.GREEN + "Data yang disimpan:")
        for line in data:
            print(line.strip())

        print(Fore.GREEN + "Proxy berhasil disimpan.")
        
        # Mengarahkan kembali ke main.py setelah menyimpan
        os.system("python main.py")  # Gantilah ini sesuai dengan cara Anda menjalankan main.py
    elif pilihan == '2':
        print(Fore.RED + "Batal menyimpan data.")
        # Mengarahkan kembali ke main.py jika dibatalkan
        os.system("python main.py")  # Gantilah ini sesuai dengan cara Anda menjalankan main.py

def main():
    tampilkan_menu()
    pilihan = input(Fore.YELLOW + "Masukkan pilihan Anda (1-5): ")

    if pilihan == '1':
        koneksi_dataimpluse()
    elif pilihan == '2':
        print(Fore.GREEN + "Anda memilih superoroxy.")
        # Tambahkan logika untuk superoroxy di sini
    elif pilihan == '3':
        print(Fore.GREEN + "Anda memilih proxylab.")
        # Tambahkan logika untuk proxylab di sini
    elif pilihan == '4':
        print(Fore.RED + "Custom belum tersedia.")
    elif pilihan == '5':
        add_proxy()
    else:
        print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()  # Pastikan tidak ada karakter tambahan setelah
def koneksi_superoroxy():
    print(Fore.GREEN + "Fungsi koneksi ke superoroxy belum diimplementasikan.")

def koneksi_proxylab():
    print(Fore.GREEN + "Fungsi koneksi ke proxylab belum diimplementasikan.")

def main():
    tampilkan_menu()
    pilihan = input(Fore.YELLOW + "Masukkan pilihan Anda (1-5): ")

    if pilihan == '1':
        koneksi_dataimpluse()
    elif pilihan == '2':
        koneksi_superoroxy()
    elif pilihan == '3':
        koneksi_proxylab()
    elif pilihan == '4':
        print(Fore.RED + "Custom belum tersedia.")
    elif pilihan == '5':
        add_proxy()
    else:
        print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()  # Pastikan tidak ada karakter tambahan setelah