import os
import time
import pwinput as pw

#inisialisasi kelas user
class user ():
    global username
    username = [] #list untuk menyimpan username
    global password
    password = [] #list untuk menyimpan password
    user = 0
    def __init__(self,store,sandi) -> None:
        self.store = store #nama toko
        self.sandi = sandi #password
        user.user += 1
        username.append(self.store) #menambahkan username ke list username
        password.append(self.sandi) #menambahkan password ke list password

toko_A = user('toko_A','tokoAjaya123') #inisialisasi objek toko_A
toko_B = user('toko_B','tokoBjaya123') #inisialisasi objek toko_B
toko_C = user('toko_C','tokoCjaya123') #inisialisasi objek toko_C


#inisialisasi kelas product
class product ():
    global list_merk
    list_merk = [] #list untuk menyimpan merk
    global list_seri
    list_seri = [] #list untuk menyimpan seri
    global list_stok
    list_stok = [] #list untuk menyimpan stok
    def __init__(self,merk,seri,stok) -> None:
        self.merk = merk #merk produk
        self.seri = seri #seri produk
        self.stok = stok #stok produk
        if merk not in list_merk: #jika merk belum ada di list merk
            list_merk.append(self.merk) #menambahkan merk ke list merk
            list_seri.append(self.seri) #menambahkan seri ke list seri
            list_stok.append(self.stok) #menambahkan stok ke list stok
        else: #jika merk sudah ada di list merk
            if seri in list_seri: #jika seri sudah ada di list seri
                indeks = list_seri.index(self.seri) #mencari indeks seri
                list_stok[indeks] += self.stok #menambahkan stok ke list stok
            else: #jika seri belum ada di list seri
                list_merk.append(self.merk) #menambahkan merk ke list merk
                list_seri.append(self.seri) #menambahkan seri ke list seri
                list_stok.append(self.stok) #menambahkan stok ke list stok

#fungsi untuk menampilkan loading bar
def UI (teks,jumlah):
    x = jumlah//2 #inisialisasi variabel X untuk looping
    string = "" #string  kosong
    for i in range (x+1): #looping untuk membuat string "="
        new_string = string + "="*i + " "*(jumlah-2*i) + "="*(i+1) #membuat string "="
        persen = (i/x)*100 #inisialisasi persentase loading bar
        persen = str(int(persen)) + "%" #mengubah persentase menjadi string
        print(new_string) #menampilkan string "="
        print("||",teks.center(jumlah-5," "),"||") #menampilkan teks
        print("||", "LOADING PROGRESS".center(jumlah-5," "), "||") #menampilkan teks loading progress
        print("||",persen.center(jumlah-5, " "),"||") #menampilkan persentase loading bar
        print(new_string) #menampilkan string "="
        time.sleep(0.1) #jeda sebelum menghapus 
        os.system('cls') #menghapus tampilan sebelumnya

#sign up page
def sign_up ():
    os.system('cls') #menghapus tampilan sebelumnya
    print("="*36)
    print('|', "signup".center(32," "),'|') #menampilkan teks signup
    print("="*36)
    nama_toko = input('username: ') #input username
    sandi = pw.pwinput('password\n(minimal 8 karakter disertai kombinasi angka dan huruf): ') #input password
    while len(sandi) < 8: #jika panjang password kurang dari 8
        print('password minimal 8 karakter')
        sandi = pw.pwinput('password: ') #input password
    print()
    print('sign up berhasil'.center(36," ")) #menampilkan teks sign up berhasil
    time.sleep(1)
    toko = user(nama_toko,sandi) #inisialisasi objek toko
    print()
    landing_page() #kembali ke landing page

#login page
def login ():
    os.system('cls') #menghapus tampilan sebelumnya
    print("="*36)
    print('|', "login".center(32," "),'|') #menampilkan teks login
    print("="*36)
    nama_toko = input('username: ') #input username
    sandi = pw.pwinput('password: ') #input password
    os.system('cls')
    UI (teks="CHECKING YOUR PASSWORD",jumlah=36) #menampilkan loading bar
    if nama_toko in username and sandi in password: #jika username dan password benar
        print('login berhasil'.center(36," ")) #menampilkan teks login berhasil
        time.sleep(1)
        os.system('cls') #menghapus tampilan sebelumnya
        show_menu() #menampilkan menu
        
    else: #jika username atau password salah
        for i in range (2): #looping untuk memasukkan username dan password sebanyak 3 kali
            print('username atau password salah') #pemberitahuan
            nama_toko = input('username: ') #input username
            sandi = pw.pwinput('password: ') #input password
            os.system('cls')
            if nama_toko in username and sandi in password: #jika username dan password benar
                print('login berhasil'.center(36," "))
                time.sleep(0.5)
                os.system('cls')
                show_menu() #menampilkan menu
                break #keluar dari looping
        else: #jika username dan password salah sebanyak 3 kali
            print('mohon maaf anda telah salah memasukkan username atau password sebanyak 3 kali')
            exit () #keluar dari program

#landing page
def landing_page ():
    os.system('cls')
    print("="*36)
    print('|','manajemen gudang kompor listrik'.center(32," "),'|') #menampilkan teks manajemen gudang kompor listrik
    print('|','silahkan login atau sign up'.center(32," "),'|') #menampilkan teks silahkan login atau sign up
    print("="*36)
    print('[1] login\n[2] sign up')
    pilihan = input('pilih menu: ') #input pilihan
    if pilihan == '1' or pilihan == 'login': #jika pilihan 1 atau login
        print()
        login() #memanggil fungsi login
    elif pilihan == '2' or pilihan == 'sign in': #jika pilihan 2 atau sign up
        print()
        sign_up() #memanggil fungsi sign up
    else: #jika pilihan tidak tersedia
        print()
        print('menu tidak tersedia') #menampilkan teks menu tidak tersedia
        time.sleep(1)
        landing_page() #kembali ke landing page

#add product
def add_product ():
    os.system('cls')
    print("="*36)
    print("|",'add product'.center(32," "),"|") #menampilkan teks add product
    print("="*36)
    print("tuntaskan satu jenis merk".center(36," "))
    merk = input('merk: ') #input merk
    seri = input('seri: ') #input seri
    stok = int(input('stok: ')) #input stok
    produk = product(merk,seri,stok) #inisialisasi objek produk
    print()
    desicion = input('apakah anda ingin menambah produk lagi? (y/n):') #input desicion
    if desicion.lower() == 'y': #jika desicion y
        add_product() #memanggil fungsi add product
    else: #jika desicion n
        os.system('cls')
        show_menu() #menampilkan menu


def edit():
    pass

def hapus():
    pass

#list produk
def list_produk():
    os.system('cls') #menghapus tampilan sebelumnya
    print()
    print('produk berhasil ditambahkan') #menampilkan teks produk berhasil ditambahkan
    print()
    print("="*36)
    print("|",'list produk'.center(32," "),"|") #menampilkan teks list produk
    print("="*36)
    column = 'merk'.ljust(10," ") + 'seri'.ljust(10," ") + 'stok' #membuat kolom
    print("|",column.center(32," "),"|") #menampilkan kolom

    all_product = [] #list penggabungan merk, seri, dan stok
    for i in range (len(list_merk)): #looping untuk menampilkan list produk
        x = f'{list_merk[i].ljust(10," ")} {list_seri[i].ljust(10," ")} {list_stok[i]}' #insialisasi variabel x yang menampilkan record produk
        print("|",x.center(32," "),"|") #menampilkan record produk
        all_product.append(x) #menambahkan record produk ke list all_product
    print("="*36)

    print()
    print("1. A-Z\n2. Z-A\n") #menampilkan pilihan urutan
    urutan = input('urutkan berdasarkan (pilih nomer)\nketik "back/b" untuk kembali:') #input urutan
    print()
    if urutan == '1': #jika urutan 1
        print("="*36)
        print("|",'list produk'.center(32," "),"|") #menampilkan teks list produk
        print("="*36)
        column = 'merk'.ljust(10," ") + 'seri'.ljust(10," ") + 'stok' #membuat kolom
        print("|",column.center(32," "),"|") #menampilkan kolom

        all_product.sort() #mengurutkan list produk dari A-Z

        for i in all_product: #looping untuk menampilkan list produk
            print("|",i.center(32," "),"|") #menampilkan record produk
        print("="*36)

    elif urutan == '2': #jika urutan 2
        print("="*36)
        print("|",'list produk'.center(32," "),"|") #menampilkan teks list produk
        print("="*36)
        column = 'merk'.ljust(10," ") + 'seri'.ljust(10," ") + 'stok' #membuat kolom
        print("|",column.center(32," "),"|") #menampilkan kolom

        all_product.sort(reverse=True) #mengurutkan list produk dari A-Z

        for i in all_product: #looping untuk menampilkan list produk
            print("|",i.center(32," "),"|") #menampilkan record produk
        print("="*36)
       
    elif urutan == 'back' or urutan == 'b': #jika memilih kembali
        os.system('cls') #menghapus tampilan sebelumnya
        show_menu() #menampilkan menu jika memilih 3

    else : #jika pilihan tidak tersedia
        print('menu tidak tersedia')
        time.sleep(1)
        list_produk()

    show_menu() #menampilkan menu setelah input urutan

#menu
def show_menu ():
    print("="*36)
    print ('|',"PILIHAN".center(32," "),"|") #menampilkan teks pilihan
    print("="*36)
    for i in range (1,6): #looping untuk menampilkan pilihan
        if i == 1: #jika i = 1
            print(f"|[{i}] add product".ljust(34," "),'|') #menampilkan teks add product
        elif i == 2: #jika i = 2
            print(f'|[{i}] edit'.ljust(34," "),'|') #menampilkan teks edit
        elif i == 3: #jika i = 3
            print(f'|[{i}] hapus'.ljust(34," "), '|') #menampilkan teks hapus
        elif i == 4: #jika i = 4
            print(f'|[{i}] list produk'.ljust(34," "), '|') #menampilkan teks list produk
        else: #jika i = 5
            print(f'|[{i}] exit'.ljust(34," "), '|') #menampilkan teks exit
    print("="*36)
    choice = int(input('pilih nomer opsi:')) #inisialisasi variabel choice untuk input pilihan
    print()
    if choice == 1: #jika pilihan 1
        add_product() #memanggil fungsi add product 
    elif choice == 2: #jika pilihan 2
        edit() #memanggil fungsi edit
    elif choice == 3: #jika pilihan 3
        hapus() #memanggil fungsi hapus 
    elif choice == 4: #jika pilihan 4
        list_produk() #memanggil fungsi list produk
    elif choice == 5: #jika pilihan 5
        dec = input("apakah anda yakin ingin keluar?, JIKA KELUAR DATA AKAN HILANG (y/n): ") #inisialisasi variabel dec untuk input desicion
        if dec.lower() == 'y': #jika desicion y
            os.system('cls')
            string = "logging out"
            for i in range (3):
                string += "."
                print(string)
                time.sleep(1)
                os.system('cls')
            print("terima kasih telah menggunakan program ini".center(36," "))
            exit() #keluar dari program
        else: #jika desicion n
            show_menu() #menampilkan menu
    else: #jika pilihan tidak tersedia
        print('menu tidak tersedia') #menampilkan teks menu tidak tersedia
        time.sleep(1)
        os.system('cls')
    if __name__ == '__main__': #jika program dijalankan
        show_menu() #menampilkan menu

def first_menu(): #menu pertama
    UI(teks="SELAMAT DATANG",jumlah=36) #menampilkan loading bar
    landing_page() #memanggil fungsi landing page

first_menu()