@echo off
chcp 65001 > nul
title MAOPKKB - Başlatıcı Menüsü
color 0A

:menu
cls
echo ===================================================
echo               MAOPKKB ANA MENÜ
echo ===================================================
echo.
echo  [1] Uygulamayı / Oyunu Çalıştır
echo  [2] Yeniden Kurulum Yap (install.bat)
echo  [3] Proje Klasörünü Aç
echo  [4] Çıkış
echo.
echo ===================================================
set /p secim="Lütfen bir işlem seçin (1-4): "

if "%secim%"=="1" goto baslat
if "%secim%"=="2" goto kur
if "%secim%"=="3" goto klasor
if "%secim%"=="4" goto cikis

echo.
echo [!] Geçersiz seçim, lütfen tekrar deneyin.
timeout /t 2 > nul
goto menu

:baslat
cls
echo [+] MAOPKKB başlatılıyor...
echo.

:: Otomatik olarak çalıştırılacak ana dosyayı kontrol eder
if exist "RoLauncher.exe" (
    start "" "RoLauncher.exe"
) else if exist "main.py" (
    python main.py
) else if exist "index.html" (
    start "" "index.html"
) else (
    echo [!] Başlatılacak ana dosya (.exe, .py veya .html) bulunamadı!
    pause
)
goto menu

:kur
cls
echo [+] Kurulum dosyası çalıştırılıyor...
call install.bat MAOPKKB
pause
goto menu

:klasor
explorer "%~dp0"
goto menu

:cikis
exit
