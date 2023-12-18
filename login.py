import os
import time
import pwinput as pw
import random
import re


raw_ID = []


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
    global list_product
    list_product = []
    global list_merk
    list_merk = [] #list untuk menyimpan merk
    global list_seri
    list_seri = [] #list untuk menyimpan seri
    global list_stok
    list_stok = [] #list untuk menyimpan stok
    global list_ID
    list_ID = [] #list untuk menyimpan ID
    
    def __init__(self,ID,merk,seri,stok) -> None:
        self.ID = ID #ID produk
        self.merk = merk #merk produk
        self.seri = seri #seri produk
        self.stok = stok #stok produk
        list_ID.append(self.ID) #menambahkan ID ke list ID
        if merk not in list_merk: #jika merk belum ada di list merk
            list_merk.append(self.merk) #menambahkan merk ke list merk
            list_seri.append(self.seri) #menambahkan seri ke list seri
            list_stok.append(self.stok) #menambahkan stok ke list stok
            list_product.append(self.merk + self.seri)
        else: #jika merk sudah ada di list merk
            item = merk + seri
            if item in list_product: #jika seri sudah ada di list product
                indeks = list_product.index(item) #mencari indeks seri
                list_stok[indeks] += self.stok #menambahkan stok ke list stok
            else: #jika seri belum ada di list seri
                list_merk.append(self.merk) #menambahkan merk ke list merk
                list_seri.append(self.seri) #menambahkan seri ke list seri
                list_stok.append(self.stok) #menambahkan stok ke list stok
                list_product.append(self.merk + self.seri)

def check_password(password):
    """
    Memeriksa apakah sandi memenuhi persyaratan.

    Returns:
        True jika sandi memenuhi persyaratan, False jika tidak.
    """

    # Persyaratan:
    # - Panjang >= 8
    # - Mengandung huruf kecil
    # - Mengandung huruf kapital
    # - Mengandung angka

    # Pastikan panjang sandi >= 8.
    if len(password) < 8:
        return False

    # Pastikan sandi mengandung huruf kecil.
    if not re.search("[a-z]", password):
        return False

    # Pastikan sandi mengandung huruf kapital.
    if not re.search("[A-Z]", password):
        return False

    # Pastikan sandi mengandung angka.
    if not re.search("[0-9]", password):
        return False

    # Sandi memenuhi persyaratan.
    return True

#fungsi untuk menampilkan loading bar
def UI (teks,jumlah):

    """memberikan tampilan loading bar"""

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

    """membuat akun baru"""

    os.system('cls') #menghapus tampilan sebelumnya
    print("="*36)
    print('|', "signup".center(32," "),'|') #menampilkan teks signup
    print("="*36)
    nama_toko = input('username: ') #input username
    while len(nama_toko) < 4 : #jika panjang username kurang dari 4
        print("nama setidaknya terdapat 4 karakter")
        time.sleep(1)
        os.system('cls')
        # nama_toko = input("username: ")
        sign_up() 
    sandi = pw.pwinput('password\n(minimal 8 karakter disertai kombinasi angka dan huruf): ') #input password

    while check_password(sandi) == False: #jika panjang password kurang dari 8
        print()
        print('password lemah'.center(36," "))
        time.sleep(1.5)
        os.system('cls')
        print(f"username: {nama_toko}")
        sandi = pw.pwinput('password: ') #input password
    print()
    print('sign up berhasil'.center(36," ")) #menampilkan teks sign up berhasil
    time.sleep(1)
    toko = user(nama_toko,sandi) #inisialisasi objek toko
    print()
    landing_page() #kembali ke landing page

#login page
def login ():

    """login ke akun yang sudah dibuat"""

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
            time.sleep(2)
            landing_page () #kembali ke menu landing page

#landing page
def landing_page ():

    """menu awal"""

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

    """menambahkan produk baru"""

    os.system('cls')
    print("="*36)
    print("|",'add product'.center(32," "),"|") #menampilkan teks add product
    print("="*36)
    print("tuntaskan satu jenis merk kompor".center(36," "))
    print("ketik b/back pada merk untuk kembali".center(36," "))
    print()

    product_id = random.randint(0,999) #inisialisasi ID produk
    while product_id in raw_ID: #jika ID produk sudah ada
        product_id = random.randint(0,999) #membuat ID produk baru
    else:
        raw_ID.append(product_id) #menambahkan ID produk ke list raw_ID
    product_id = str(product_id) #mengubah ID produk menjadi string

    if len(product_id) == 1: #jika panjang ID produk 1
        new_id = product_id.zfill(3)
        product_id = 'P' + new_id
    elif len(product_id) == 2: #jika panjang ID produk 2
        new_id = product_id.zfill(3)
        product_id = 'P' + new_id
    else:
        product_id = 'P' + product_id

    merk = input('merk: ') #input merk
    if merk == 'b' or merk == 'back': #jika memilih kembali
        os.system('cls')
        show_menu() #menampilkan menu jika memilih 3

    seri = input('seri: ') #input seri
    while len(seri) == 0 :
        print('seri tidak boleh kosong')
        seri = input('seri: ')

    try:
        stok = int(input('stok: ')) #input stok
    except ValueError: #jika input stok bukan integer
        print('stok harus berupa angka')
        time.sleep(1)
        add_product()
        
    produk = product(product_id,merk,seri,stok) #inisialisasi objek produk
    print()
    desicion = input('apakah anda ingin menambah produk lagi? (y/n):') #input desicion
    if desicion.lower() == 'y': #jika desicion y
        add_product() #memanggil fungsi add product
    elif desicion.lower() == 'n': #jika desicion n
        os.system('cls')
        show_menu() #menampilkan menu
    else:
        print('menu tidak tersedia') #menampilkan teks menu tidak tersedia
        time.sleep(1)
        add_product()


def edit():

    """mengedit produk"""

    print("="*38)
    print("|",'list produk'.center(34," "),"|") #menampilkan teks list produk
    print("="*38)
    column = 'ID'.ljust(10," ") +'merk'.ljust(10," ") + 'seri'.ljust(10," ") + 'stok' #membuat kolom
    print("|",column.center(32," "),"|") #menampilkan kolom

    all_product = [] #list penggabungan merk, seri, dan stok
    for i in range (len(list_merk)): #looping untuk menampilkan list produk
        x = f'{list_ID[i].ljust(9," ")} {list_merk[i].ljust(9," ")} {list_seri[i].ljust(10," ")} {list_stok[i]:<3}' #insialisasi variabel x yang menampilkan record produk
        print("|",x.center(32," "),"|") #menampilkan record produk
        all_product.append(x) #menambahkan record produk ke list all_product
    print("="*38)

    print('edit'.center(36,"="))
    print("pilih produk yang ingin diedit".center(36," "))
    print()
    id= input('masukkan id produk atau \nketik back/b untuk kembali: ')
    print()
    if id in list_ID:
        desicion = input("apa anda yakin ingin mengubahnya?[y/n]: ")
        print()
        if desicion == 'y':
            i= list_ID.index(id)
            merk_baru= input('merk baru: ')
            seri_baru= input('seri baru: ')
            stok_baru= False 
            while type(stok_baru) is not int:
                try:
                    stok_baru=int(input("stok baru (int): "))
                except ValueError:
                    print('stok harus berupa angka')
            list_merk[i]= merk_baru
            list_stok[i]= stok_baru
            list_seri[i]= seri_baru
            print()
            print('produk berhasil diedit'.center(36," ")) 
            time.sleep(1)        
            os.system('cls')
            show_menu()
        elif desicion == 'n':
            os.system("cls")
            show_menu()
        else:
            print("pilihan tidak sesuai")
            time.sleep(1.5)
            os.system('cls')
            edit()
    elif id=='back'or id=='b':
        os.system('cls')
        show_menu()
    else:
        print()
        print('id salah'.center(36," "))
        time.sleep(1)
        os.system('cls')
        print('tidak ditemukan id yang sesuai')
        print()
        edit()

def hapus():

    """menghapus produk"""


    print("="*38)
    print("|",'list produk'.center(34," "),"|") 
    print("="*38)
    column = 'ID'.ljust(10," ") +'merk'.ljust(10," ") + 'seri'.ljust(10," ") + 'stok' #membuat kolom
    print("|",column.center(32," "),"|") #menampilkan kolom

    all_product = [] #list penggabungan merk, seri, dan stok
    for i in range (len(list_merk)): #looping untuk menampilkan list produk
        x = f'{list_ID[i].ljust(9," ")} {list_merk[i].ljust(9," ")} {list_seri[i].ljust(10," ")} {list_stok[i]:<3}' #insialisasi variabel x yang menampilkan record produk
        print("|",x.center(32," "),"|") #menampilkan record produk
        all_product.append(x) #menambahkan record produk ke list all_product
    print("="*38)
    
    print('hapus'.center(36,"="))
    print("pilih produk yang ingin dihapus".center(36," "))
    print()
    id= input('masukkan id produk atau \nketik back/b untuk kembali: ')
    print()
    if id in list_ID:
        desicion = input("apa anda yakin ingin menghapusnya?[y/n]: ")
        if desicion == 'y':
            i= list_ID.index(id)
            del list_ID[i]
            del list_merk[i]
            del list_seri[i]
            del list_stok[i]
            print()
            print('produk berhasil dihapus'.center(36," ")) #menampilkan teks sign up berhasil
            time.sleep(1)        
            os.system('cls')
            show_menu()
        elif desicion == 'n':
            os.system("cls")
            show_menu()
        else:
            print("pilihan tidak sesuai")
            time.sleep(1.5)
            os.system('cls')
            hapus()
    elif id=='back'or id=='b':
        os.system('cls')
        show_menu()
    else:
        print()
        print('id salah'.center(36," "))
        time.sleep(1)
        os.system('cls')
        print('tidak ditemukan id yang sesuai')
        print()
        hapus()
        

#list produk
def list_produk():

    """menampilkan list produk"""

    os.system('cls') #menghapus tampilan sebelumnya
    print()
    print('produk berhasil ditambahkan') #menampilkan teks produk berhasil ditambahkan
    print()
    print("="*38)
    print("|",'list produk'.center(34," "),"|") #menampilkan teks list produk
    print("="*38)
    column = 'ID'.ljust(10," ") +'merk'.ljust(10," ") + 'seri'.ljust(10," ") + 'stok' #membuat kolom
    print("|",column.center(32," "),"|") #menampilkan kolom

    global all_product
    all_product = [] #list penggabungan merk, seri, dan stok
    for i in range (len(list_merk)): #looping untuk menampilkan list produk
        record = f'{list_ID[i].ljust(9," ")} {list_merk[i].ljust(9," ")} {list_seri[i].ljust(10," ")} {list_stok[i]:<3}' #insialisasi variabel record yang menampilkan record produk
        print("|",record.center(32," "),"|") #menampilkan record produk
        all_product.append(record) #menambahkan record produk ke list all_product
    print("="*38)

    print()
    print("sorting:")
    print("1. A-Z\n2. Z-A\n") #menampilkan pilihan urutan
    urutan = input('urutkan berdasarkan (pilih nomer)\nketik "back/b" untuk kembali:') #input urutan
    print()
    if urutan == '1': #jika urutan 1
        os.system('cls')
        sorting_list()

    elif urutan == '2':
        os.system('cls')
        sorting_list(True)
       
    elif urutan == 'back' or urutan == 'b': #jika memilih kembali
        os.system('cls') #menghapus tampilan sebelumnya
        show_menu() #menampilkan menu jika memilih 3

    else : #jika pilihan tidak tersedia
        print('menu tidak tersedia')
        time.sleep(1)
        list_produk()


def sorting_list (urutkan = False):

    """fungsi untuk mengurutkan list produk"""

    print("produk berhasil diurutkan")
    print()
    print("="*38)
    print("|",'list produk'.center(34," "),"|") #menampilkan teks list produk
    print("="*38)
    column = 'ID'.ljust(10," ") +'merk'.ljust(10," ") + 'seri'.ljust(10," ") + 'stok' #membuat kolom
    print("|",column.center(32," "),"|") #menampilkan kolom

    all_product.sort(reverse=urutkan) #mengurutkan list produk dari A-Z

    for i in all_product: #looping untuk menampilkan list produk
        print("|",i.center(32," "),"|") #menampilkan record produk
    print("="*38)
    print()
    desicion = input('ketik "back/b" untuk kembali: ')
    if desicion == 'b' or desicion == 'back':
        list_produk()
    else:
        print()
        print("menu tidak ada")
        time.sleep(1.5)
        os.system('cls')
        sorting_list()

#menu
def show_menu ():

    """menampilkan menu utama dan pilihan"""
    
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
    try:
        choice = int(input('pilih nomer opsi:')) #inisialisasi variabel choice untuk input pilihan
    except ValueError:
        print()
        print('pilihan harus berupa angka')
        time.sleep(1)
        os.system('cls')
        show_menu()
    print()
    if choice == 1: #jika pilihan 1
        add_product() #memanggil fungsi add product 
    elif choice == 2: #jika pilihan 2
        os.system('cls')
        edit() #memanggil fungsi edit
    elif choice == 3: #jika pilihan 3
        os.system('cls')
        hapus() #memanggil fungsi hapus 
    elif choice == 4: #jika pilihan 4
        list_produk() #memanggil fungsi list produk
    elif choice == 5: #jika pilihan 5
        dec = input("apakah anda yakin ingin keluar?, JIKA KELUAR DATA AKAN HILANG y/n): ") #inisialisasi variabel dec untuk input desicion
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
        elif dec.lower() == 'n': #jika desicion n
            os.system('cls')
            show_menu()
        else: #jika desicions selain itu
            print()
            print("menu tidak tersedia".center(36," "))
            time.sleep(1.5)
            os.system('cls')
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
