"""
APLIKASI DETEKSI GEMPA
MODULARISASI DENGAN FUNCTION
MODULARISAI DENGAN PACKAGE
"""
import gempaterkini
if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)