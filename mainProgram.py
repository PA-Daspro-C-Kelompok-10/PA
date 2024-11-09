from prettytable import PrettyTable
import time
import json
import pwinput
import os

jsonPathJasa = r"C:\Users\user\OneDrive\Gambar\Keperluan Praktikum\Dasar Pemrograman\PA\dataJasa.json"

with open(jsonPathJasa, "r") as jsonJasa:
    dataJasa = json.loads(jsonJasa.read())

def saveJsonJasa():
    with open(jsonPathJasa, "w") as jsonJasa:
        json.dump(dataJasa, jsonJasa, indent = 4)

jsonPathUser = r"C:\Users\user\OneDrive\Gambar\Keperluan Praktikum\Dasar Pemrograman\PA\dataUser.json"

with open(jsonPathUser, "r") as jsonUser:
    dataUser = json.loads(jsonUser.read())

def saveJsonUser():
    with open(jsonPathUser, "w") as jsonUser:
        json.dump(dataUser, jsonUser, indent = 4)

data_admin = {
    "dewa": "dewa2024",
    "arul": "arul2024",
    "irpan": "irpan2024"
}

def tabel_layanan():
    table = PrettyTable()
    table.title = "LAYANAN YANG TERSEDIA"
    table.field_names = ["No", "Nama Layanan", "Harga (Rp)"]
    for i, layanan in enumerate(dataJasa["layanan"], start=1):
        table.add_row([i, layanan['nama'], layanan['harga']])
    print(table)

def clear():
    os.system("cls")

def login_berhasil():
    clear()
    print("\t\t             Login Berhasil!  ")
    time.sleep(1.3)
    clear()
    loading()

def login_gagal():
    clear()
    print("+==========================================================================+")
    print("| Username atau Password yang Anda Masukkah Salah, Silakan di Cek Kembali! |")
    print("+==========================================================================+")
    time.sleep(0.8)

def tunggu():
    print("\n\t\t    Mohon Tunggu Sebentar." )
    time.sleep(0.3)
    clear()
    print("\n\t\t    Mohon Tunggu Sebentar.." )
    time.sleep(0.3)
    clear()
    print("\n\t\t    Mohon Tunggu Sebentar..." )
    time.sleep(0.3)
    clear()
    print("\n\t\t    Mohon Tunggu Sebentar...." )
    time.sleep(0.3)
    clear()
    print("\n\t\t    Mohon Tunggu Sebentar....." )
    time.sleep(0.3)
    clear()

def tunggu_invoice():
    print("\n\t\t    Sedang Memuat Invoice Anda." )
    time.sleep(0.4)
    clear()
    print("\n\t\t    Sedang Memuat Invoice Anda.." )
    time.sleep(0.4)
    clear()
    print("\n\t\t    Sedang Memuat Invoice Anda..." )
    time.sleep(0.4)
    clear()
    print("\n\t\t    Sedang Memuat Invoice Anda...." )
    time.sleep(0.4)
    clear()
    print("\n\t\t    Sedang Memuat Invoice Anda....." )
    time.sleep(0.4)
    clear()

def mencari_layanan():
    print("\n\t\t    Sedang Mencari Layanan, Tunggu Sebentar." )
    time.sleep(0.5)
    clear()
    print("\n\t\t    Sedang Mencari Layanan, Tunggu Sebentar.." )
    time.sleep(0.5)
    clear()
    print("\n\t\t    Sedang Mencari Layanan, Tunggu Sebentar..." )
    time.sleep(0.5)
    clear()
    print("\n\t\t    Sedang Mencari Layanan, Tunggu Sebentar...." )
    time.sleep(0.5)
    clear()
    print("\n\t\t    Sedang Mencari Layanan, Tunggu Sebentar....." )
    time.sleep(0.5)
    clear()

def loading():
    print("\t\t\t      Loading...")
    print("\t\t  +================================+")
    print("\t\t  |                                |")
    print("\t\t  +================================+")
    time.sleep(0.7)
    clear()
    print("\t\t\t      Loading...")
    print("\t\t  +================================+")
    print("\t\t  |■■■■                            |")
    print("\t\t  +================================+")
    time.sleep(1)
    clear()
    print("\t\t\t      Loading...")
    print("\t\t  +================================+")
    print("\t\t  |■■■■■■■■■■■                     |")
    print("\t\t  +================================+")
    time.sleep(0.5)
    clear()
    print("\t\t\t      Loading...")
    print("\t\t  +================================+")
    print("\t\t  |■■■■■■■■■■■■■■■■                |")
    print("\t\t  +================================+")
    time.sleep(0.3)
    clear()
    print("\t\t\t      Loading...")
    print("\t\t  +================================+")
    print("\t\t  |■■■■■■■■■■■■■■■■■■■■■■          |")
    print("\t\t  +================================+")
    time.sleep(0.7)
    clear()
    print("\t\t\t      Loading...")
    print("\t\t  +================================+")
    print("\t\t  |■■■■■■■■■■■■■■■■■■■■■■■■■■■     |")
    print("\t\t  +================================+")
    time.sleep(0.2)
    clear()
    print("\t\t\t      Loading...")
    print("\t\t  +================================+")
    print("\t\t  |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■|")
    print("\t\t  +================================+")
    time.sleep(0.2)
    clear()

def daftar_user():
    clear()
    print("+============================================================+")
    print("|                    PENDAFTARAN AKUN USER                   |")
    print("+============================================================+")
    time.sleep(0.5)
    while True:
        try:
            while True:
                nama_baru = str(input("Masukkan Nama (*Min 4 Karakter, Maks 50 Karakter): ")).strip()
                if 4 <= len(nama_baru) <= 50 and nama_baru.isalnum():
                    break
                else:
                    print("\n|> *!* Nama HANYA Terdiri dari Huruf dan Angka, Min 4 Karakter dan Maks 50 Karakter! *!* <|")
            while True:
                password_baru = pwinput.pwinput(prompt="Masukkan Password (*Min 4 karakter, Maks 50 karakter): ").strip()
                if 4 <= len(password_baru) <= 50:
                    break
                else:
                    print("\n|> *!* Password HARUS Min 4 karakter dan maks 50 karakter! *!* <|")
            if nama_baru in dataUser["Nama"] and password_baru in dataUser["Password"]:
                print("\n|> *!* Data ini sudah ada! *!* <|")
                time.sleep(2)
                menu_awal()
                return
            saldo_awal = 0
            dataUser["Nama"].append(nama_baru)
            dataUser["Password"].append(password_baru)
            dataUser["Saldo"].append(saldo_awal)
            saveJsonUser()
            clear()
            print("\n===== Pendaftaran berhasil! Silakan Lakukan Login! =====")
            time.sleep(2.5)
            menu_awal()
            return
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def sebagai_admin():
    clear()
    print("+================================================+")
    print("|       SILAKAN LAKUKAN LOGIN SEBAGAI ADMIN      |")
    print("+================================================+")
    time.sleep(0.5)
    while True:
        try:
            usernameAdmin = input("Masukkan username anda: ").lower()
            passwordAdmin = pwinput.pwinput("Masukkan Password anda: ")
            if usernameAdmin in data_admin and data_admin[usernameAdmin] == passwordAdmin:
                clear()
                login_berhasil()
                menu_admin()
                break
            elif usernameAdmin == "" and passwordAdmin == "":
                print("|> *!*  Input Tidak Boleh Kosong!  *!* <|")
            elif " " in usernameAdmin and " " in passwordAdmin:
                print("|> *!*  Input Tidak Boleh Pakai Spasi!  *!* <|")
            else:
                login_gagal()
                sebagai_admin()
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def sebagai_user():
    clear()
    print("+=============================================+")
    print("|      SILAKAN LAKUKAN LOGIN SEBAGAI USER     |")
    print("+=============================================+")
    time.sleep(0.5)
    while True:
        try:
            usernameUser = input("Masukkan username anda: ").lower()
            passwordUser = pwinput.pwinput("Masukkan Password anda: ")
            if usernameUser in dataUser["Nama"]:
                index = dataUser["Nama"].index(usernameUser)
                if dataUser["Password"][index] == passwordUser:
                    clear()
                    login_berhasil()
                    menu_user(usernameUser)
                    break
                elif usernameUser == "" or passwordUser == "":
                    print("|> *!*  Input Tidak Boleh Kosong!  *!* <|")
                elif " " in usernameUser or " " in passwordUser:
                    print("|> *!*  Input Tidak Boleh Pakai Spasi!  *!* <|")
                else:
                    login_gagal()
            elif usernameUser == "" or passwordUser == "":
                print("|> *!*  Input Tidak Boleh Kosong!  *!* <|")
            elif " " in usernameUser or " " in passwordUser:
                print("|> *!*  Input Tidak Boleh Pakai Spasi!  *!* <|")
            else:
                login_gagal()
                sebagai_user()
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!* Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def create_jasa():
    clear()
    tunggu()
    clear()
    print("+============================================================+")
    print("|               MEMASUKI MENU MENAMBAHKAN LAYANAN            |")
    print("+============================================================+")
    time.sleep(0.5)
    while True:
        try:
            nama_jasa = str(input("Masukkan Nama Layanan (*Ketik '0' Jika Ingin Membatalkan): ")).strip()
            layanan_terdaftar = any(layanan["nama"].lower() == nama_jasa.lower() for layanan in dataJasa["layanan"])
            if nama_jasa == "":
                print("\n|> *!* Input Tidak Boleh Kosong! *!* <|")
            elif nama_jasa == "0":
                clear()
                break
            elif layanan_terdaftar:
                print("\n+===========================================+")
                print("|    LAYANAN SUDAH TERDAFTAR DI DATABASE!   |")
                print("+===========================================+")
            else:
                harga_layanan = input("Masukkan Harga untuk Layanan yang Baru Dimasukkan: ")
                if len(harga_layanan) <= 8 and harga_layanan.isdigit():
                    dataJasa["layanan"].append({"nama": nama_jasa, "harga": int(harga_layanan)})
                    saveJsonJasa()
                    print("\n+============================================+")
                    print("|        LAYANAN BERHASIL DITAMBAHKAN!       |")
                    print("+============================================+")
                    time.sleep(2.3)
                    clear()
                    break
                elif harga_layanan == "":
                    print("\n|> *!* Input Tidak Boleh Kosong! *!* <|")
                else:
                    print("\n|> *!* Input Tidak Valid! *!* <|\n")
                    time.sleep(1)
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!* Tolong Jangan Menekan CTRL dan C Secara Bersamaan! *!* <|")

def read_jasa():
    clear()
    tunggu()
    clear()
    tabel_layanan()
    while True:
        try:
            input("\nTekan ENTER Untuk Kembali......")
            clear()
            menu_admin()
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def update_jasa():
    clear()
    tunggu()
    print("+============================================================+")
    print("|                MEMASUKI MENU MENGEDIT LAYANAN              |")
    print("+============================================================+")
    time.sleep(0.5)
    while True:
        tabel_layanan()
        try:
            pilihan = int(input("Masukkan Nomor Layanan yang Ingin Diupdate (Ketik '0' Untuk Membatalkan): ")) - 1
            if pilihan == -1:
                print("\n===== Pembaruan Layanan Dibatalkan =====")
                clear()
                break
            if pilihan < 0 or pilihan >= len(dataJasa['layanan']):
                print(f"\n|> *!* Nomor Layanan {pilihan} Tidak Ditemukan! *!* <|")
                continue
            nama_baru = input(f"Masukkan Nama Baru Untuk {dataJasa['layanan'][pilihan]['nama']} (*Biarkan Kosong Jika Tidak Ingin Mengubah): ").strip()
            harga_baru = input(f"Masukkan harga baru untuk {dataJasa['layanan'][pilihan]['nama']} (*Biarkan Kosong Jika Tidak Ingin Mengubah): ").strip()
            if nama_baru:
                dataJasa['layanan'][pilihan]['nama'] = nama_baru
            if harga_baru:
                if harga_baru.isdigit():
                    dataJasa['layanan'][pilihan]['harga'] = int(harga_baru)
                else:
                    clear()
                    print("\n|> *!* Harga Harus Berupa Angka! *!* <|")
                    continue
            saveJsonJasa()
            print(f"\n===== LAYANAN BERHASIL DIPERBARUI! =====\n")
            break
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!* Tolong Jangan Menekan CTRL dan C Secara Bersamaan! *!* <|")

def delete_jasa():
    clear()
    tunggu()
    clear()
    print("+============================================================+")
    print("|                MEMASUKI MENU MENGHAPUS LAYANAN             |")
    print("+============================================================+")
    time.sleep(0.5)
    while True:
        tabel_layanan()
        try:
            pilihan = int(input("Masukkan Nomor Layanan yang Ingin Dihapus (*Ketik 0 Jika Ingin Membatalkan): "))
            if 1 <= pilihan <= len(dataJasa["layanan"]):
                del dataJasa["layanan"][pilihan - 1]
                saveJsonJasa()
                clear()
                print("\n===== LAYANAN BERHASIL DIHAPUS! =====\n")
                time.sleep(3)
                clear()
                break
            elif pilihan == 0:
                clear()
                break
            else:
                print(f"\n|> *!* Nomor Layanan {pilihan} Tidak Ditemukan! *!* <|\n")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def menu_admin():
    clear()
    while True:
        print("+========================================================+")
        print("|               Selamat Datang di Menu ADMIN             |")
        print("+========================================================+")
        print("| [1]. Tambahkan Layanan                                 |")
        print("| [2]. Lihat Layanan                                     |")
        print("| [3]. Edit Layanan                                      |")
        print("| [4]. Hapus Layanan                                     |")
        print("| [5]. Kembali                                           |")
        print("+========================================================+")
        try:
            pilihan = int(input("Masukkan Pilihan Menu: "))
            if pilihan == 1:
                create_jasa()
            elif pilihan == 2:
                read_jasa()
            elif pilihan == 3:
                update_jasa()
            elif pilihan == 4:
                delete_jasa()
            elif pilihan == 5:
                menu_awal()
            else:
                clear()
                print(f"|> *!* Pilihan Menu {pilihan} Tidak Ditemukan. *!* <|")
                while True:
                    try:
                        input("\nTekan ENTER untuk kembali.....")
                        clear()
                        break
                    except Exception as e:
                        print(f"|> *!* Error pada {e} *!* <|")
                    except KeyboardInterrupt:
                        print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def invoicePemesanan(nama_layanan, harga_layanan, saldo_user, alamat, usernameUser):
    clear()
    tunggu_invoice()
    clear()
    print(f"                   ___________________                   ")
    print(f"+=================| INVOICE PEMESANAN |=================+")
    print(f"|=======================================================|")
    print(f"| Nama Layanan                  : {nama_layanan}        |")
    print(f"| Atas Nama                     : {usernameUser}        |")
    print(f"| Alamat Tujuan                 : {alamat}              |")
    print(f"| Waktu Kedatangan              : Besok Pukul 9 Pagi    |")
    print(f"| Total Harga Layanan           : Rp {harga_layanan}    |")
    print(f"| Status Pembayaran             : - LUNAS -             |")
    print(f"+-------------------------------------------------------+")
    print(f"| Sisa Saldo Anda               : Rp {saldo_user}       |")
    print(f"+=======================================================+")
    while True:
        try:
            while True:
                try:
                    input("Tekan ENTER Untuk Kembali.....")
                    clear()
                    break
                except Exception as e:
                    print(f"|> *!* Error pada {e} *!* <|")
                except KeyboardInterrupt:
                    print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def pesan_jasa(usernameUser):
    usernameUser in dataUser["Nama"]
    user_index = dataUser["Nama"].index(usernameUser)
    saldo_user = dataUser["Saldo"][user_index]
    clear()
    tunggu()
    clear()
    print("+============================================================+")
    print("|                 MEMASUKI MENU MEMESAN LAYANAN              |")
    print("+============================================================+")
    time.sleep(0.5)
    tabel_layanan()
    while True:
        try:
            pilihan = int(input("Masukkan Nomor Layanan yang Ingin Dipesan (*Ketik '0' Jika Ingin Keluar): "))
            if 1 <= pilihan <= len(dataJasa["layanan"]):
                layanan = dataJasa["layanan"][pilihan - 1]
                harga_layanan = layanan["harga"]
                if saldo_user >= harga_layanan:
                    dataUser["Saldo"][user_index] -= harga_layanan
                    saveJsonUser()
                    alamat = input("Masukkan alamat Anda: ")
                    print(f"\n===== Layanan '{layanan['nama']}' berhasil dipesan! =====")
                    print(f"Layanan akan datang besok pagi ke alamat: {alamat}")
                    input("Tekan ENTER Untuk Melihat Invoice Anda....") 
                    invoicePemesanan(layanan['nama'], harga_layanan, dataUser["Saldo"][user_index], alamat)
                    break
                else:
                    print("\n|> *!* Saldo Anda Tidak Mencukupi Untuk Memesan Layanan Ini. *!* <|")
            elif pilihan == 0:
                clear()
                break
            else:
                print(f"\n|> *!* Nomor Layanan {pilihan} Tidak Ditemukan! *!* <|")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def cek_saldo(usernameUser):
    usernameUser in dataUser["Nama"]
    user_index = dataUser["Nama"].index(usernameUser)
    clear()
    tunggu()
    clear()
    print("+============================================================+")
    print("|                  MEMASUKI MENU MELIHAT SALDO               |")
    print("+============================================================+")
    time.sleep(0.5)
    while True:
        saldo_user = dataUser["Saldo"][user_index]
        print("\n+================================+")
        print(f"| Saldo Anda Saat Ini: Rp {saldo_user} |")
        print("+================================+")
        print("| [1] Top Up Saldo               |")
        print("| [2] Kembali ke Menu User       |")
        print("+================================+")
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                while True:
                    try:
                        top_up = int(input("Masukkan jumlah top up: "))
                        if top_up <= 0:
                            print("\n|> *!* Jumlah Top Up Tidak Boleh Nol atau Negatif! *!* <|.")
                        elif saldo_user + top_up > 6000000:
                            print("\nSaldo Anda tidak boleh melebihi 6 juta.")
                        else:
                            dataUser["Saldo"][user_index] += top_up
                            saveJsonUser()
                            print(f"\nTop up berhasil! Saldo Anda sekarang: Rp {dataUser['Saldo'][user_index]}")
                            time.sleep(1.5)
                            clear()
                            break
                    except Exception as e:
                        print(f"|> *!* Error pada {e} *!* <|")
                    except KeyboardInterrupt:
                        print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")
            elif pilihan == 2:
                clear()
                break
            else:
                clear()
                print(f"|> *!* Pilihan Menu {pilihan} Tidak Ditemukan. *!* <|")
                while True:
                    try:
                        input("\nTekan ENTER Untuk Menginput Ulang....")
                        clear()
                        break
                    except Exception as e:
                        print(f"|> *!* Error pada {e} *!* <|")
                    except KeyboardInterrupt:
                        print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def sort():
    clear()
    tunggu()
    clear()
    print("+============================================================+")
    print("|                   MEMASUKI MENU SORT                       |")
    print("+============================================================+")
    time.sleep(0.5)
    urutan_asli = list(dataJasa["layanan"])
    while True:
        print("\n+========================================================+")
        print("|                 Silakan Pilih Opsi Sort                |")
        print("+========================================================+")
        print("| [1]. Berdasarkan Abjad                                 |")
        print("| [2]. Berdasarkan Harga                                 |")
        print("| [3]. Kembali                                           |")
        print("+========================================================+")
        try:
            pilihan = int(input("Masukkan Pilihan Menu: "))
            if pilihan == 1:
                while True:
                    clear()
                    print("\n+========================================================+")
                    print("|         Silakan Pilih Opsi Pengurutan Abjad            |")
                    print("+========================================================+")
                    print("| [1]. A-Z                                               |")
                    print("| [2]. Z-A                                               |")
                    print("| [3]. Kembali                                           |")
                    print("+========================================================+")
                    pilihan_abjad = int(input("Masukkan Pilihan: "))
                    table = PrettyTable()
                    table.title = "LAYANAN YANG TERSEDIA"
                    table.field_names = ["No", "Nama Layanan", "Harga (Rp)"]
                    if pilihan_abjad == 1:
                        for i, layanan in enumerate(sorted(dataJasa["layanan"], key=lambda x: x["nama"]), start=1):
                            table.add_row([i, layanan['nama'], layanan['harga']])
                        print(table)
                    elif pilihan_abjad == 2:
                        for i, layanan in enumerate(sorted(dataJasa["layanan"], key=lambda x: x["nama"], reverse=True), start=1):
                            table.add_row([i, layanan['nama'], layanan['harga']])
                        print(table)
                    elif pilihan_abjad == 3:
                        break
                    else:
                        print(f"\n|> *!* Pilihan {pilihan_abjad} Tidak Ditemukan. *!* <|")
                        time.sleep(1)
                        continue
                    input("Tekan ENTER Untuk Kembali.....")
                    clear()
                    table.clear_rows()
                    for i, layanan in enumerate(urutan_asli, start=1):
                        table.add_row([i, layanan['nama'], layanan['harga']])
                    print(table)
            elif pilihan == 2:
                while True:
                    clear()
                    print("+========================================================+")
                    print("|          Silakan Pilih Opsi Pengurutan Harga           |")
                    print("+========================================================+")
                    print("| [1]. Terendah ke Termahal                              |")
                    print("| [2]. Termahal ke Terendah                              |")
                    print("| [3]. Kembali                                           |")
                    print("+========================================================+")
                    pilihan_harga = int(input("Masukkan Pilihan: "))
                    table = PrettyTable()
                    table.title = "LAYANAN YANG TERSEDIA"
                    table.field_names = ["No", "Nama Layanan", "Harga (Rp)"]
                    if pilihan_harga == 1:
                        for i, layanan in enumerate(sorted(dataJasa["layanan"], key=lambda x: x["harga"]), start=1):
                            table.add_row([i, layanan['nama'], layanan['harga']])
                        print(table)
                    elif pilihan_harga == 2:
                        for i, layanan in enumerate(sorted(dataJasa["layanan"], key=lambda x: x["harga"], reverse=True), start=1):
                            table.add_row([i, layanan['nama'], layanan['harga']])
                        print(table)
                    elif pilihan_harga == 3:
                        break
                    else:
                        print(f"\n|> *!* Pilihan {pilihan_harga} Tidak Ditemukan. *!* <|")
                        time.sleep(1)
                        continue
                    input("Tekan ENTER Untuk Kembali.....")
                    clear()
                    table.clear_rows()
                    for i, layanan in enumerate(urutan_asli, start=1):
                        table.add_row([i, layanan['nama'], layanan['harga']])
                    print(table)
            elif pilihan == 3:
                clear()
                break
            else:
                clear()
                print(f"\n|> *!* Pilihan Menu {pilihan} Tidak Ditemukan. *!* <|")
                while True:
                    try:
                        input("Tekan ENTER Untuk Kembali.....")
                        clear()
                        break
                    except Exception as e:
                        print(f"|> *!* Error pada {e} *!* <|")
                    except KeyboardInterrupt:
                        print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

def search():
    clear()
    tunggu()
    clear()
    print("+====================================================================+")
    print("|                   MEMASUKI MENU MENCARI LAYANAN                    |")
    print("+====================================================================+")
    time.sleep(0.5)
    while True:
        try:
            namaLayanan = str(input("Masukkan Nama Layanan (*Ketik '0' Jika Ingin Keluar): ")).strip()
            if namaLayanan == "0":
                clear()
                break
            clear()
            mencari_layanan()
            clear()
            for layanan in dataJasa["layanan"]:
                if layanan["nama"].lower() == namaLayanan.lower():
                    table = PrettyTable()
                    table.field_names = ["Nama Layanan", "Harga (Rp)"]
                    table.add_row([layanan["nama"], layanan["harga"]])
                    clear()
                    print("+=====================================+")
                    print("Layanan Ditemukan:")
                    print(table)
                    print("+=====================================+")
                    while True:
                        try:
                            input("Tekan ENTER Untuk Melanjutkan.....")
                            clear()
                            break
                        except Exception as e:
                            print(f"|> *!* Error pada {e} *!* <|")
                        except KeyboardInterrupt:
                            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")
                    break
            else:
                
                clear()
                print(f"+==============================================================================+")
                print(f"| Layanan '{namaLayanan}' Tidak Ada di Database atau INPUT TIDAK BOLEH KOSONG! |")
                print(f"+==============================================================================+")
                while True:
                    try:
                        input("\nTekan ENTER Untuk Melanjutkan.....")
                        clear()
                        break
                    except Exception as e:
                        print(f"|> *!* Error pada {e} *!* <|")
                    except KeyboardInterrupt:
                        print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan! *!* <|")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan! *!* <|")

def menu_user(usernameUser):
    while True:
        print("+========================================================+")
        print("|               Selamat Datang di Menu USER              |")
        print("+========================================================+")
        print("| [1]. Pesan Layanan                                     |")
        print("| [2]. Saldo                                             |")
        print("| [3]. Urutkan Layanan                                   |")
        print("| [4]. Cari Layanan                                      |")
        print("| [5]. Kembali                                           |")
        print("+========================================================+")
        try:
            pilihan = int(input("Masukkan Pilihan Menu: "))
            if pilihan == 1:
                pesan_jasa(usernameUser)
            elif pilihan == 2:
                cek_saldo(usernameUser)
            elif pilihan == 3:
                sort()
            elif pilihan == 4:
                search()
            elif pilihan == 5:
                menu_awal()
            else:
                clear()
                print(f"\n|> *!* Pilihan Menu {pilihan} Tidak Ditemukan. *!* <|")
                while True:
                    try:
                        input("\nTekan ENTER Untuk Kembali.....")
                        clear()
                        break
                    except Exception as e:
                        print(f"|> *!* Error pada {e} *!* <|")
                    except KeyboardInterrupt:
                        print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan! *!* <|")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan! *!* <|")

def menu_awal():
    clear()
    print("+====================================================================+")
    print("|                           SELAMAT DATANG                           |")
    print("|                         SILAKAN PILIH MENU                         |")
    print("+====================================================================+")
    print("| [1] Masuk Sebagai Admin                                            |")
    print("| [2] Masuk Sebagai User                                             |")
    print("| [3] Daftar Akun User                                               |")
    print("| [4] Keluar Program                                                 |")
    print("+====================================================================+")
    while True:
        try:
            pilihan = int(input("Pilih Menu: "))
            if pilihan == 1:
                sebagai_admin()
            elif pilihan == 2:
                sebagai_user()
            elif pilihan == 3:
                daftar_user()
            elif pilihan == 4:
                clear()
                print("+======================================================================+")
                print("|                          KELUAR DARI PROGRAM                         |")
                print("+======================================================================+")
                exit()
            elif pilihan == "":
                print("|> *!*  Input Tidak Boleh Kosong!  *!* <|")
            else:
                clear()
                print(f"|> *!* Pilihan Menu {pilihan} Tidak Ditemukan. *!* <|")
                while True:
                    try:
                        input("\nTekan ENTER untuk kembali.....")
                        menu_awal()
                    except Exception as e:
                        print(f"|> *!* Error pada {e} *!* <|")
                    except KeyboardInterrupt:
                        print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")
        except Exception as e:
            print(f"|> *!* Error pada {e} *!* <|")
        except KeyboardInterrupt:
            print("|> *!*  Tolong Jangan Menekan CTRL dan C Secara Bersamaan!  *!* <|")

menu_awal()