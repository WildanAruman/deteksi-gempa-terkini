"""
APLIKASI DETEKSI GEMPA
MODULARISASI DENGAN FUNCTION
MODULARISAI DENGAN PACKAGE
"""
from gempaterkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)