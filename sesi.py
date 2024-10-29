from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def akses_facebook_selenium():
    # Set opsi untuk Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server=http://username:password@host:port")  # Ganti dengan informasi proxy yang benar

    # Inisialisasi browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # Mengakses Facebook
    driver.get("https://www.facebook.com")

    # Tunggu beberapa detik untuk melihat halaman
    driver.implicitly_wait(5)  # Tunggu hingga 5 detik

    # Menampilkan judul halaman
    print(driver.title)

    # Menutup browser
    driver.quit()

if __name__ == "__main__":
    akses_facebook_selenium()