# Aplikasi Pemesanan jasa kebersihan komersial

## Diskripsi Program
Program ini adalah sebuah program pemesanan jasa kebersihan komersial yang dimana terdapat 2 role yaitu admin dan user, Untuk role admin sendiri dapat melakukan C.R.U.D. (Create, Read, Update dan Delete), dan untuk role user itu dapat mengisi saldo dan memesan layanan jasa yang tersedia.

## Library
Terdapat 5 library yang kami gunakan di program ini yaitu:
1. PrettyTable untuk membuat tabel secara otomatis dan rapi,
2. *os* disini kami gunakan untuk membersihkan tampilan di terminal,
3. pwinput untuk membuat password tidak langsung terlihat,
4. time disini kami gunakan untuk loading,
5. json untuk mengakses dan mengupdate json.

## Nama Anggota Kelompok
Reswara Ganendra Rashi Dewa (2409116100)
Ahmad Qomarul Arifin (2409116114)
Muhammad Irpan (2409116119)

## Fitur
### User
1. Pesan layanan
2. saldo
3. Urutkan layanan
4. cari layanan

   
### Admin
1. Menambahkan layanan
2. Lihat layanan
3. Edit layanan
4. Hapus layanan


# Penggunaan Program

## Menu Awal

![Screenshot 2024-11-09 222358](https://github.com/user-attachments/assets/fe6aa58f-cedc-4f24-8b68-f4135cb554a9)

Tampilan yang pertama kali muncul saat menjalankan program adalah menu awal. Disini terdapat 3 pilihan yaitu masuk sebagai admin, masuk sebagai user, daftar akun user, keluar

## Menu Login
### Login User

![Screenshot 2024-11-09 222456](https://github.com/user-attachments/assets/c5cb82be-71a1-4bb3-9aa7-f04daa67d799)

Sebelum melakukan login, user terlebih dahulu melakukan daftar akun user, dengan mengisi nama user dan kata sandi user

![Screenshot 2024-11-09 223150](https://github.com/user-attachments/assets/1e7827e2-34fd-4ce7-9fd4-8b9e0e3e618e)

Setelah berhasil daftar akun, masuk kembali ke menu awal lalu lakukan login memasukkan nama dan kata sandi user.
Jika berhasil login akan ada muncul login berhasil dan akan dimasukkan dimenu user.

### Daftar Akun

![Screenshot 2024-11-09 224126](https://github.com/user-attachments/assets/7d9dc9a0-d271-476f-a7c9-dd7a3d0e55c9)

Jika nomor 2 yang di input di menu awal, maka akan memunculkan menu daftar akun. Pertama masukkan nama akun yang ingin di daftarkan.

![Screenshot 2024-11-09 224205](https://github.com/user-attachments/assets/4e1c1716-0d0f-4a46-aa49-7d7dcb9fdc1e)

Lalu masukkan password.

![Screenshot 2024-11-09 224216](https://github.com/user-attachments/assets/70a65ff0-4c44-4dcb-a8e6-7588888a2657)

jika telah selesai memamsukkan nama dan password maka akan muncul tulisan berhasi melakukan pendaftaran akun.

### Login Admin

![Screenshot 2024-11-09 224645](https://github.com/user-attachments/assets/3664cfa5-5e5b-47a8-965d-4af9f2f9d86c)

Jika ingin masuk ke menu admin maka masukkan:\
nama akun : a\
password : 1\
Jika benar maka akan di arahkan ke menu admin

### Keluar Program

![Screenshot 2024-11-09 224808](https://github.com/user-attachments/assets/8e05896e-baba-444e-82fc-508c831495b5)

Jika memilih no 4 maka akan memunculkan pesan seperti gambar diatas.

## Menu User

![Screenshot 2024-11-09 224957](https://github.com/user-attachments/assets/3a962e83-6c7a-4c6c-96ef-bb9f8d453968)

Jika nama akun dan password di menu login benar, maka akan memunculkan menu user. Disini terdapat 5 pilihan yaitu pesan layanan, saldo, urutkan layanan, cari layanan, kembali

### Pesan Layanan

![Screenshot 2024-11-09 225344](https://github.com/user-attachments/assets/0616ab5f-f19e-400e-a27a-c142e11b5a0c)

Jika nomor 1 yang di input di menu user, maka akan masuk ke menu pesan layanan.

![Screenshot 2024-11-09 225606](https://github.com/user-attachments/assets/8068e491-a215-4553-870f-b821c87c7e43)

Jika sudah memilih layanan maka akan diberikan invoice

### Saldo

![Screenshot 2024-11-09 225745](https://github.com/user-attachments/assets/6fa41d23-85a2-4526-ac7f-d483f5cb8044)

Jika nomor 2 yang di input di menu user, maka akan masuk ke menu saldo, disini terdapat infromasi saldo, pengisian saldo dan kembali ke menu user
Dan jika ingin mengisi saldo, akan terdapat pesan masukkan saldo yang diisi, setelah memasukkan saldo maka akan ada pesan saldo berhasil ditambahkan dan tertera total saldo.

#### Kembali

![Screenshot 2024-11-09 230136](https://github.com/user-attachments/assets/3524c5ab-270b-43fd-b212-5b428e2246e6)

Jika nomor 2 yang diinput maka akan kembali ke menu user.

### Urutkan Layanan

![Screenshot 2024-11-09 230226](https://github.com/user-attachments/assets/3a4f7234-d122-4615-9f7d-623af407f814)

Jika nomor 3 yang di input di menu user, maka akan masuk ke menu urutkan layanan3. Disini terdapat 3 pilihan yaitu berdasarkan Abjad, berdasarkan harga dan kembali

#### Berdasarkan Abjad

![Screenshot 2024-11-09 230418](https://github.com/user-attachments/assets/887017ab-6c6e-4646-83ef-df4cf7418732)

Jika nomor 1 yang di input di menu urutkan layanan, maka akan muncul tabel pengurutan abjad dari A-Z dan Z-A

### Berdasarkan Harga

![Screenshot 2024-11-09 230638](https://github.com/user-attachments/assets/b114138a-0f4f-42e8-81c7-bdd19b9347f3)

Jika nomor 2 yang di input di menu urutkan layanan, maka akan muncul tabel data layanan yang sudah diurutkan berdasarkan harga terendah ke termahal dan termahal ke terendah.

#### Kembali

![Screenshot 2024-11-09 230806](https://github.com/user-attachments/assets/8414f2a3-e02e-48d6-89ac-026e8f52830a)

Jika nomor 3 yang diinput maka akan kembali ke menu user.

### Cari Layanan

![Screenshot 2024-11-09 231026](https://github.com/user-attachments/assets/449522e8-e92b-4d36-99e1-5189516ed37f)

Jika memlilih pilihan 4 maka akan masuk ke menu mencari layanan, menu ini berisi input masukkan nama layanan yang ingin dicari.

### Kembali

![Screenshot 2024-11-09 231249](https://github.com/user-attachments/assets/5611d1b2-49f8-4c72-98a2-49c676387ff8)

Jika nomor 5 yang diinput maka akan kembali ke menu awal.

## Menu Admin

![Screenshot 2024-11-09 231504](https://github.com/user-attachments/assets/5d8c4adf-d099-473f-8f6b-90a04a1a2642)

Berikut adalah menu admin jika di menu login memasukkan nama dan password admin.

### Tambahkan Layanan

![Screenshot 2024-11-09 231622](https://github.com/user-attachments/assets/cdc9c79f-f120-4198-ad47-f41d56a9e937)

Jika nomor 1 diinput maka akan masuk di mmenu menambahkan layanan di menu ini silahkan langsung menambahkan menu layanan mulai dari nama layanan dan harga layanan.

### Lihat Layanan

![Screenshot 2024-11-09 231812](https://github.com/user-attachments/assets/c66dd2d4-6c4c-4403-8797-ad0aa30f795c)

Jika nomor 2 diinput maka akan masuk di menu lihat layanan yang berisi tabel layanan beserta harga layanannya.

### Edit Layanan

![Screenshot 2024-11-09 232007](https://github.com/user-attachments/assets/f0da030e-3c61-487b-ab7e-578bf6033030)

Jika nomor 3 yang diinput maka akan memunculkan menu edit data layanan. Lalu pilih data mana yang ingin di edit.

### Hapus Layanan

![Screenshot 2024-11-09 232114](https://github.com/user-attachments/assets/6b41c9c4-a9aa-48d5-9bb9-cf5e6695c66c)

Jika nomor 4 yang diinput maka akan masuk di tabel data layanan, lalu ilih data layanan mana yang akan dihapus.


### kembali

![Screenshot 2024-11-09 232348](https://github.com/user-attachments/assets/79de813a-71c0-4fb6-b1c5-432f76f41737)

Jika nomor 5 yang diinput maka akan kembali ke menu awal.

