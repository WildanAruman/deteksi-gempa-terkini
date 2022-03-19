"""
APLIKASI DETEKSI GEMPA
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    hasil = dict()
    hasil['tanggal'] = '24 agustus 2022'
    hasil['waktu'] = '12:05:52 WIB'
    hasil['magnitudo'] = 4.0
    hasil['lokasi'] = {'ls': 1.48, 'BT': 134.01}
    hasil['pusat'] = 'Pusat gempa beradada di darat 19 km barat laut aceh'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Manokwari, II-III Aceh'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan data BMKG')
    print(f"Tanggal, {result['tanggal']}")
    print(f"waktu, {result['waktu']}")
    print(f"Magnitudo, {result['magnitudo']}")
    print(f"Lokasi: LS = {result['lokasi']['ls']}, BT = {result['lokasi']['ls']} ")
    print(f"Pusat, {result['pusat']}")
    print(f"Dirasakan, {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)