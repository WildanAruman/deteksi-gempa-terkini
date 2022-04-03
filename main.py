"""
APLIKASI DETEKSI GEMPA
MODULARISASI DENGAN FUNCTION
MODULARISAI DENGAN PACKAGE

"""
#from gempaterkini import GempaTerkini
import gempaterkini
if __name__ == '__main__':
    gempa_di_indeonesia = gempaterkini.GempaTerkini('https://bmkg.go.id')
    print(f'Aplikasi utama menggunkan package yang memiliki deskripsi {gempa_di_indeonesia.description}')

    gempa_di_indeonesia.tampilkan_keterangan()
    gempa_di_indeonesia.run()

