from tabulate import tabulate
headers=['Id','Nama','Kamar','Alamat','Umur'] 
list_pasien=[
     ['Wisnu',1,'Jogja',32], 
     ['Raffa',2,'Medan',23],
     ['Niel',3,'Medan',25]
     ]

#keywordnya a b c
#fungsi untuk tabulatetable
def menampilkan_pasien(): #menu1
    if not list_pasien:
        print('Tidak ada data pasien\n')
        return

    print('Daftar Pasien Rumah Sakit 2304\n')
    formatted_list_pasien = []
    for index, pasien in enumerate(list_pasien, start=1):
        formatted_pasien = [index, pasien[0], pasien[1], pasien[2], pasien[3]]
        formatted_list_pasien.append(formatted_pasien)
    table = tabulate(formatted_list_pasien, headers=headers, tablefmt='pretty', showindex=False)
    print(table)

    while True:
        nomor_pasien = input("Masukkan nomor pasien yang ingin ditampilkan (atau tekan Enter untuk kembali): ")
        if nomor_pasien.strip() == '':
            break
        elif nomor_pasien.isdigit():
            nomor_pasien = int(nomor_pasien)
            if 1 <= nomor_pasien <= len(list_pasien):
                pasien = list_pasien[nomor_pasien - 1]
                print("Detail Pasien:")
                print(f"Nama: {pasien[0]}")
                print(f"Id Pasien: {pasien[1]}")
                print(f"Alamat: {pasien[2]}")
                print(f"Umur: {pasien[3]}")
                break
            else:
                print("Nomor pasien tidak valid. Silakan masukkan nomor pasien yang sesuai.")
        else:
            print("Masukkan harus berupa angka atau tekan Enter untuk kembali.")

# Fungsi untuk meminta input huruf
def inputHuruf(pesan):
    huruf = input(pesan)
    while not huruf.isalpha():
        print("Mohon masukkan huruf saja.")
        huruf = input(pesan)
    return huruf

# Function untuk menambah pasien
def menambah_Pasien(): 
    nama = input("Masukkan nama pasien yang baru: ")
    while not nama.isalpha():
        print("Mohon Masukkan Huruf yang Benar.")
        nama = input("Masukkan nama baru pasien: ")
    while True:
        kamar = input("Masukkan nomor kamar pasien yang baru: ")
        if kamar.isdigit():
            kamar = int(kamar)
            break
        else:
            print("Mohon Masukkan Angka yang Benar")     
    alamat = input("Masukkan alamat pasien yang baru: ")
    while True:
        alamat = input("Masukkan alamat pasien yang baru: ")
        if alamat.replace(" ", "").isalpha():
            break
        else:
            print("Mohon masukkan huruf saja dalam alamat.")
    while True:
        umur_input = input("Masukkan umur pasien yang baru: ")
        if umur_input.isdigit():
            umur = int(umur_input)
            break
        else:
            print("Mohon masukkan angka saja.")
    
    # Konfirmasi kepada pengguna sebelum menambahkan pasien
    konfirmasi = input("Apakah Anda yakin ingin menambahkan pasien? (Ya/Tidak): ")
    if konfirmasi.lower() == 'Ya':
        list_pasien.append([nama, kamar, alamat, umur])
        print("Pasien berhasil ditambahkan.")
    else:
        print("Penambahan pasien dibatalkan.")

def submenu_menambah_Pasien(): #submenu 2
    while True:
            nama = input("Masukkan nama pasien yang baru: ")
            while True:
                kamar_input = input("Masukkan nomor kamar pasien yang baru: ")
                if kamar_input.isdigit():
                    kamar = int(kamar_input)
                    break
                else:
                    print("Mohon Maaf Input Tidak valid, Silahkan Coba Lagi.")
            alamat = input("Masukkan alamat pasien yang baru: ")
            while True:
                umur_input = input("Masukkan umur pasien yang baru: ")
                if umur_input.isdigit():
                    umur = int(umur_input)
                    break
                else:
                    print("Mohon Maaf Input Tidak valid, Silahkan Coba Lagi.")

            # Tambahkan pasien baru ke list_pasien
            list_pasien.append([nama, kamar, alamat, umur])
            print("Pasien berhasil ditambahkan.")
            pilihan = input("Apakah Anda ingin menambahkan pasien lagi? (ya/tidak): ")
            if pilihan.lower() == "tidak":
                break
            elif pilihan.lower() != "ya":
                print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")

# Fungsi untuk menghapus pasien
def menghapus_pasien(): #menu 3
    if len(list_pasien) > 0:
        menampilkan_pasien()
        idx = int(input("Pilih nomor index pasien yang ingin dihapus: ")) - 1
        if 0 <= idx < len(list_pasien):
            del list_pasien[idx]
            print("Pasien berhasil dihapus.")
        else:
            print("Nomor pasien tidak valid.")
    else:
        print("Belum ada pasien terdaftar.")

def submenu_menghapus_pasien(): #submenu 3
    if len(list_pasien) > 0:
        menampilkan_pasien()
        idx = int(input("Pilih nomor index pasien yang ingin dihapus: ")) - 1
        if 0 <= idx < len(list_pasien):
            del list_pasien[idx]
            print("Pasien berhasil dihapus.")
        else:
            print("Nomor pasien tidak valid.")
    else:
        print("Belum ada pasien terdaftar.")
def menghapus_pasien(): 
    while True:
        submenu_menghapus_pasien()
        pilihan = input("Apakah Anda ingin menghapus pasien lagi? (ya/tidak): ")
        if pilihan.lower() == "tidak":
            break
        elif pilihan.lower() != "ya":
            print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")

# Fungsi untuk mengedit data pasien
def submenu_mengedit_pasien():   #menu 4
    if len(list_pasien) > 0:
        while True:
            idx_input = input("Masukkan Id pasien yang ingin diedit (atau tekan Enter untuk kembali ke submenu): ")
            if idx_input.strip() == '':
                return  # Kembali ke submenu sebelumnya jika input kosong
            elif idx_input.isdigit():
                idx = int(idx_input)
                if 0 <= idx < len(list_pasien):
                    break
                else:
                    print("Id pasien tidak valid. Harap masukkan Id yang sesuai.")
            else:
                print("Mohon masukkan Id pasien yang valid.")

        while True:
            nama = input("Masukkan nama baru pasien: ")
            while not nama.isalpha():
                print("Mohon masukkan huruf saja.")
                nama = input("Masukkan nama baru pasien: ")
            while True:
                kamar_input = input("Masukkan kamar pasien yang baru: ")
                if kamar_input.isdigit():
                    kamar = int(kamar_input)
                    break
                else:
                    print("Mohon maaf, input tidak valid. Silakan coba lagi.")
            alamat = input("Masukkan alamat pasien yang baru: ")
            while not alamat.replace(" ", "").isalpha():
                print("Mohon masukkan huruf yang benar.")
                alamat = input("Masukkan alamat pasien yang baru: ")
                break
            while True:
                umur_input = input("Masukkan umur baru pasien: ")
                if umur_input.isdigit():
                    umur = int(umur_input)
                    list_pasien[idx] = [nama, kamar, alamat, umur]
                    break
                else:
                    print("Mohon masukkan angka saja.")
            
            pilihan = input("Apakah Anda ingin mengedit pasien lagi? (ya/tidak): ")
            if pilihan.lower() == "tidak":
                break
            elif pilihan.lower() != "ya":
                print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
                print("Data pasien berhasil diperbarui.")
                break
            else:
                print("Belum ada pasien terdaftar.")
            
def mengedit_pasien():   #submenu 4
    while True:
        submenu_mengedit_pasien()
        pilihan = input("Apakah Anda ingin mengedit pasien lagi? (ya/tidak): ")
        if pilihan.lower() == "tidak":
            break
        elif pilihan.lower() != "ya":
            print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")

#fungsi untuk mencari pasien
def mencari_Pasien(): #submenu1 pilihan 2
    while True:
        keyword = input("Masukkan nomor Id untuk mencari pasien: ")
        if keyword.isdigit():  # Periksa apakah input adalah nomor
            keyword = int(keyword)
            if 1 <= keyword <= len(list_pasien):  # Periksa apakah nomor indeks valid
                pasien = list_pasien[keyword - 1]  # Ambil data pasien berdasarkan nomor indeks
                print("Hasil Pencarian:")
                print(f"Nama Pasien: {pasien[0]}, Kamar: {pasien[1]}, Alamat: {pasien[2]}, Umur: {pasien[3]}")
                break
            else:
                print("Nomor indeks tidak valid. Silakan masukkan nomor indeks yang sesuai.")
        else:  
            hasil_pencarian = [pasien for pasien in list_pasien if keyword.lower() in pasien[0].lower()]
            if hasil_pencarian:
                print("Hasil Pencarian:")
                for pasien in hasil_pencarian:
                    print(f"Nama Pasien: {pasien[0]}, Kamar: {pasien[1]}, Alamat: {pasien[2]}, Umur: {pasien[3]}")
                break
            else:
                print("Pasien tidak ditemukan.")

#fungsi untuk hanya menginput angka
def inputAngka(prompt):
    while True:
        angka = input(prompt)
        if angka.isdigit():  # Memeriksa apakah input harus angka
            return angka
        else:
            print("Masukkan harus berupa angka. Silakan coba lagi.")

# Program utama
while True: 
    menu= inputAngka('''
    Selamat Datang di rumah sakit 2304 

    Menu:       
    1. Menampilkan Daftar Pasien
    2. Menambah Nama Pasien
    3. Menghapus Nama Pasien
    4. Mengedit Data Pasien
    5. Exit Program
    Masukan Angka Menu Yang Ingin Dijalankan : ''')

    if menu == '1':    #submenu (menu utama1)
        while True:
            menu1 = inputAngka('''
                Submenu Menampilkan Daftar Pasien
                1. Menampilkan Daftar Nama Pasien
                2. Mencari Pasien
                3. Kembali Ke Menu Utama 
                Masukkan Menu yang Ingin Dijalankan :  ''')
            if menu1 == '1':
                menampilkan_pasien()
            elif menu1 == '2':
                mencari_Pasien()
            elif menu1 == '3':
                break  # Keluar dari loop dan kembali ke menu utama
            else:
                print("Menu tidak valid. Silakan masukkan pilihan yang sesuai.")
    
    if menu == '2':      #submenu (menu utama2)
        while True:
            menu2 = inputAngka('''
                Submenu Untuk Menambahkan Data Pasien
                1.Menambahkan Data Pasien
                2.Kembali Ke Menu Utama
                Masukkan Menu yang Ingin Dijalankan : ''')
            if menu2 == '1':
                menambah_Pasien()
            elif menu2 =='2':
                break #keluar dari loop dan kembali ke menu utama 
            else:
                print("Menu tidak valid. Silakan masukkan pilihan yang sesuai.")

    if menu == '3':     #submenu (menu utama3)
        while True:
            menu3 = inputAngka('''
                Submenu Untuk Menghapus Data Pasien
                1.Menghapus Data Pasien
                2.Kembali ke Menu Utama
                Masukkan Menu yang Ingin Dijalankan : ''')
            if menu3 == '1':
                menghapus_pasien()
            elif menu3 == '2':
                break #keluar dari loop dan kembali ke menu utama 
            else :
                print("Menu tidak valid. Silakan masukkan pilihan yang sesuai.")

    if menu == '4':     #submenu (menu utama4)
        while True:
            menu4 = inputAngka('''
                Submenu Untuk Mengedit Data Pasien
                1.Mengedit Data Pasien 
                2.Kembali ke Menu Utama
                Masukkan Menu yang Ingin Dijalankan : ''')
            if menu4 == '1':
                mengedit_pasien()
            elif menu4 == '2':
                break  #keluar dari loop dan kembali ke menu utama 
            else : 
                print("Menu tidak valid. Silakan masukkan pilihan yang sesuai.")
    
    if menu == '5':
        print('Terimakasih, Anda Sudah Keluar dari Program')
        break
    else : 
        print('Mohon Masukkan Nomor Sesuai Dengan Menu yang Tersedia')




