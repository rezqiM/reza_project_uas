list_merk = ['rania','signora','vaganza']
list_merk.sort()
rania_seri = ['alpha','beta','gamma']
signora_seri = ['X','Y','Z']
vaganza_seri = ['1','2','3']

print(f'berikut list merk yang kami miliki')
for i in range (1,len(list_merk)+1):
    print(f'{i}. {list_merk[i-1]}')
print()

def formulir ():

    nama = input('nama:') #nama pembeli
    alamat = input('alamat:') #alamat pembeli
    merk = input('merk:')
    if merk in list_merk: #jika merk yang disebutkan ada didalam list
        if merk == 'rania': #jika merk nya adalah rania

            print('berikut list seri dari produk rania')
            for i in range (1,len(rania_seri)+1):
                if i == 1:
                    print(f'{i}. {rania_seri[i-1]}, harga = 2.300.000')
                elif i == 2:
                    print(f'{i}. {rania_seri[i-1]}, harga = 2.800.000')
                else:
                    print(f'{i}. {rania_seri[i-1]}, harga = 2.900.000')

            seri = input('masukkan seri yang anda inginkan:')
            if seri in rania_seri: #mengecek apakah seri yang disebutkan ada di dalam list seri rania
                if seri == 'alpha':
                    harga = 2300000
                elif seri == 'beta':
                    harga = 2800000
                else:
                    harga = 2900000
            else:
                while seri not in rania_seri: #jika seri yang dimasukkan tidak ada di dalam list, maka program akan terus menanyakan serinya
                    print('seri tidak ada/invalid, mohon masukkan seri dengan benar')
                    seri = input('masukkan seri yang anda inginkan:')
                if seri == 'alpha':
                    harga = 2300000
                elif seri == 'beta':
                    harga = 2800000
                else:
                    harga = 2900000
        elif merk == 'signora':
            pass
        else:
            pass
    else:
        while merk not in list_merk :
            print('merk tidak ada/invalid')
            merk = input('merk:')

        if merk == 'rania': #jika merk nya adalah rania
            print('berikut list seri dari produk rania')
            for i in range (1,len(rania_seri)+1):
                if i == 1:
                    print(f'{i}. {rania_seri[i-1]}, harga = 2.300.000')
                elif i == 2:
                    print(f'{i}. {rania_seri[i-1]}, harga = 2.800.000')
                else:
                    print(f'{i}. {rania_seri[i-1]}, harga = 2.900.000')

            seri = input('masukkan seri yang anda inginkan:')
            if seri in rania_seri: #mengecek apakah seri yang disebutkan ada di dalam list seri rania
                if seri == 'alpha':
                    harga = 2300000
                elif seri == 'beta':
                    harga = 2800000
                else:
                    harga = 2900000
            else:
                while seri not in rania_seri: #jika seri yang dimasukkan tidak ada di dalam list, maka program akan terus menanyakan serinya
                    print('seri tidak ada/invalid, mohon masukkan seri dengan benar')
                    seri = input('masukkan seri yang anda inginkan:')
                if seri == 'alpha':
                    harga = 2300000
                elif seri == 'beta':
                    harga = 2800000
                else:
                    harga = 2900000
        elif merk == 'signora':
            pass
        else:
            pass

    jumlah_pesanan = int(input('jumlah pesanan:'))
    telepon = input('telepon:')
    if len(telepon) >= 10 and len(telepon) <= 13 and telepon.isnumeric() == True: #panjang nomer telepon antara 11-12 angka dan semua berupa angka, tdk boleh selain angka
        pass
    else: #jika panjang nomer telepon >12 atau <11 atau nomer telepon terdapat karakter selain angka
        while len(telepon) < 10 or len(telepon) > 13 or telepon.isnumeric() == False:
            print('masukkan nomer dengan benar')
            telepon = input("telepon:")

    total = harga*jumlah_pesanan
    # jumlah_harga = jumlah_pesanan*merk_kompor[f'{merk}']['harga']

    print("="*36)
    print('FORMULIR PEMESANAN'.center(36," "))
    print()
    print(f'nama\t :{nama}')
    print(f'alamat\t :{alamat}')
    print(f'telepon\t :{telepon}')
    print(f'merk\t :{merk}')
    print(f'seri\t :{seri}')
    print(f'jumlah\t :{jumlah_pesanan}')
    print(f'total\t :{total}')
    print("="*36)

formulir()
