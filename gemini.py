import time
import random
import os
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Fare kontrolü için pyautogui kütüphanesini içe aktarıyoruz
try:
    import pyautogui
except ImportError:
    print("HATA: 'pyautogui' kütüphanesi eksik!")
    print("Lütfen terminale 'pip install pyautogui' yazarak yükleyin.")
    time.sleep(5)
    exit()

# 1. AŞAMA: Matrix Ekranı
os.system("color 0a")
os.system("cls")

print("=== SİSTEME GİRİŞ YAPILIYOR ===")
time.sleep(1)

# Ekranda akan havalı Matrix sayıları
for i in range(25):
    satir = "".join(random.choice(["0", "1", "!", "%", "&", "#", "$", "*"]) for _ in range(75))
    print(satir)
    time.sleep(0.05)

print("\n[+] GÜVENLİK DUVARI AŞILDI!")
time.sleep(1)

# 2. AŞAMA: Fareyi Ele Geçirme (Videodaki Kısım)
print("\n[!] SİSTEM KONTROLÜ ELE GEÇİRİLDİ. FARE DEVRE DIŞI!")
time.sleep(1)

# Ekranın genişliğini ve yüksekliğini otomatik algıla
ekran_genislik, ekran_yukseklik = pyautogui.size()

# Fareyi 15 kez ekranın rastgele yerlerine ışınla/kaydır
for _ in range(15):
    rastgele_x = random.randint(100, ekran_genislik - 100)
    rastgele_y = random.randint(100, ekran_yukseklik - 100)
    # Fareyi o noktaya 0.2 saniyede kaydırır (gerçekçi bir hareket hissi verir)
    pyautogui.moveTo(rastgele_x, rastgele_y, duration=0.2)

# 3. AŞAMA: YouTube Videosu Açma (Efsane Rickroll Şakası)
print("\n[!] Tarayıcı ele geçirildi. Veriler aktarılıyor...")
# Tarayıcıda efsanevi şaka şarkısı "Never Gonna Give You Up" açılır
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
time.sleep(3) # Şarkının açılması için 3 saniye bekle

# 4. AŞAMA: Not Defteri Açma
print("[!] Sisteme not bırakılıyor...")
dosya_adi = "HACKER_NOTU.txt"
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    dosya.write("SİSTEME TAMAMEN SIZILDI!\n\n")
    dosya.write("Farenin nasıl kendi kendine hareket ettiğini gördün mü? :)\n")
    dosya.write("Müzik de fena değilmiş bence...\n\n")
    dosya.write("Merak etme, sadece oyun oynuyoruz. Hiçbir dosyan silinmedi.\n")

os.startfile(dosya_adi)
time.sleep(2)

# 5. AŞAMA: Komik Uyarı Penceresi
root = tk.Tk()
root.withdraw() # Arkadaki gereksiz boş pencereyi gizle

messagebox.showwarning(
    "DİKKAT: SİSTEM ELE GEÇİRİLDİ!", 
    "Tüm dosyaların şifrelendi!\n\nKurtuluş bedeli: 1 adet çikolatalı kurabiye.\n\nŞifreyi çözmek için gülümse ve 'Tamam'a bas!"
)

messagebox.showinfo(
    "GÖREV TAMAMLANDI", 
    "Gülümsediğin tespit edildi!\n\nVirüs kendini imha etmeye karar verdi. Sebep: Fazla komik olması.\nToplam Zarar: 0 TL."
)

print("\nSistemden çıkış yapılıyor... İyi günler! :)")
time.sleep(3)