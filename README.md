# Event-Organizer-Kapi


## Nama Proyek

Penyusunan sistem informasi Event Organizer untuk Kapi berbasis CLI


### Deskripsi Singkat

Dengan dibuatnya usaha baru di bidang jasa dan layanan event organizer milik Kapi, dibutuhkan sebuah sistem informasi yang dapat membantu asisten-asisten Kapi dalam mengelola data klien, mencatat kebutuhan acara, memilih vendor, serta menghitung perkiraan total anggaran untuk setiap event.


# Aturan Kerja

### Pembagian Tugas
Berikut keahlian masing-masing anggota tim

**Maria Gabriela Liunardi:**
* Business analyst 
* Project manager 
* Risk Manager
* Full stack developer 3
* Database designer 1
* Database developer 2
* Technical writer

**Tya Kanaya:**
* System architect 
* Product owner 
* Full stack developer 1 
* UI/UX designer 
* Database designer 2 
* Quality assurance engineer 
* Technical writer 

**Serafina Livia Wardhana:**
* Tech lead 
* Scrum master 
* Full stack developer 2 
* Performance engineer 
* Database developer 1 
* Requirement engineer

Tugas-tugas dan jadwal pengerjaan dilihat melalui dokumen perencanaan proyek berikut:
https://docs.google.com/document/d/11L1wusnYkidiuLdbF4HsNNt395FY6GrOHKME7JGDMOA/edit?pli=1\&tab=t.0


### Petunjuk pengerjaan

**Link Repository** yang digunakan adalah sebagai berikut:
https://github.com/MariaGabrielaLiunardi/Event-Organizer-Kapi.git

**Kanban Board** dapat diakses melalui link:
https://trello.com/b/X1xzDzpd/event-organizer-kapi

**Langkah pengerjaan:**
1. Pindah task yang sedang dikerjakan pada kanban board ke kolom “Dikerjakan”
2. Push setiap hasil pengerjaan task ke branch masing-masing kemudian buat pull request ke branch sprint. Pengerjaan akan diulas kembali oleh PM sebelum dilakukan merge ke branch sprint
3. Untuk testing, pull program dari branch sprint, lalu ulangi langkah 1-2 setelah memperbaiki bug. Pindah  task yang sedang dikerjakan pada kanban board ke kolom “Testing”
4. Pada akhir sprint (saat launching) PM melakukan merge ke branch main.
5. Setiap task yang selesai dikerjakan dipindah ke kolom “Done” pada kanban board


### Saluran Komunikasi
Komunikasi dilakukan melalui LINE untuk chat dan Discord untuk voice chat



# Ruang Lingkup Proyek
Ruang lingkup proyek ini mencakup perancangan, pengembangan, pengujian, dan implementasi sistem informasi event organizer Kapi menggunakan pendekatan agile. Pekerjaan dibagi dalam beberapa tahap dengan keluaran (increment) yang bisa langsung digunakan dan ditinjau oleh user secara bertahap. 

1. Setiap tahap meliputi: 
    a. Pemilihan fitur yang akan dikerjakan. 
    b. Pengembangan modul sesuai prioritas.
    c. Testing (unit testing, quality control, dan UAT). 
    d. Feedback dari pemilik usaha dan asisten.
2. Modul-modul utama akan dikembangkan dalam tahapan berikut: 
    a. Tahap 1: Modul manajemen asisten.
    b. Tahap 2: Modul manajemen vendor dan kategori vendor. 
    c. Tahap 3: Modul manajemen klien. 
    d. Tahap 4: Modul manajemen event dan jenis event. 
    e. Tahap 5: Modul laporan terkait vendor, event, dan budgeting. 
3. Data yang dikelola:
    a. Data asisten. 
    b. Data vendor dan jenis vendor. 
    c. Data klien.
    d. Data event dan jenis event. 
4. Merealisasikan desain basis data serta sistem berbasis CLI ke dalam bentuk program.
5. Pelatihan penggunaan aplikasi bagi pemilik usaha dan asisten. 
6. Menyusun jadwal kerja pada tiap tahapan. 
7. Batasan sistem: 
    a. Sistem tidak menangani pembayaran kepada vendor maupun event organizer. 
    b. Sistem hanya mencatat data, menyajikan laporan, dan membantu budgeting.

# Language and Environtment
Java version 21
SQL Server version 17

Struktur repo
* main
* sprint_manpro
* sprint_1
* sprint_2
* sprint_3
* sprint_4
* sprint_5
* gaby
* tea
* livia

Struktur folder
* README.md
* documentation
* project


# Manual Penggunaan Sistem 
Pertama kali sistem dijalankan: 
1. Buka terminal di directory sistem. 
2. Masukkan “python InitializeDatabase.py” untuk membuat tabel di database. 

Menjalankan dan masuk ke sistem: 
Pemilik (Kapi): 
1. Buka terminal di directory sistem. 
2. Masukkan “python MainMenu.py” untuk menjalankan aplikasi.
3. Masukkan username dan password pemilik. 

Asisten: 
1. Buka terminal di directory sistem. 
2. Masukkan “python MainMenu.py” untuk menjalankan aplikasi.
3. Masukkan username dan password asisten. 

Keluar dari sistem: Masukkan “0” dari awal menu untuk keluar dari sistem. 

Fitur bagi pemilik (Kapi): 
Kelola asisten 
Lihat data asisten:
1. Masukkan “1” untuk memilih menu “Kelola asisten”. 
2. Masukkan “1” untuk memilih menu “Lihat data asisten”. Semua data asisten akan muncul. 
3. Masukkan “1” untuk memilih menu “Lihat data asisten spesifik”. 
4. Masukkan ID asisten.  

Edit data asisten: 
1. Dari lihat data asisten spesifik, masukkan “1” untuk memilih menu “Edit data asisten”. 
2. Masukkan nama, alamat, telepon, dan email baru dari asisten. 

Hapus data asisten: 
1. Dari lihat data asisten spesifik, masukkan “2” untuk memilih menu “Hapus data asisten”. 
2. Masukkan “1” untuk mengkonfirmasi penghapusan asisten, masukkan “2” untuk membatalkan. 

Tambah asisten: Masukkan username, password, nama, alamat, no telepon, dan email asisten. 

Kelola data vendor 
Lihat data vendor:
1. Masukkan “2” untuk memilih menu “Kelola vendor”. 
2. Masukkan “1” untuk memilih menu “Lihat data vendor”. Semua data vendor akan muncul. 
3. Masukkan “1” untuk memilih menu “Lihat vendor spesifik”. 
4. Masukkan ID vendor.  

Edit data vendor:
1. Dari lihat data vendor spesifik, masukkan “1” untuk memilih menu “Edit data vendor”. 
2. Masukkan nama, pemilik, alamat, telepon, email, harga min, harga max, dan jenis vendor baru. 

Hapus data vendor: 
1. Dari lihat data vendor spesifik, masukkan “2” untuk memilih menu “Hapus data vendor”. 
2. Masukkan “1” untuk mengkonfirmasi penghapusan vendor, masukkan “2” untuk membatalkan. 

Tambah vendor: Masukkan nama, nama pemilik, alamat, no telepon, email, harga min, harga max, dan jenis vendor. 

Kelola data jenis vendor 
1. Lihat jenis vendor: 
2. Masukkan “3” untuk memilih menu “Kelola data jenis vendor”. 
3. Masukkan “1” untuk memilih menu “Lihat jenis vendor”. 

Edit jenis vendor: 
1. Dari lihat jenis vendor, masukkan “1” untuk memilih menu “Edit jenis vendor”. 
2. Masukkan ID dan jenis baru vendor. 

Tambah jenis vendor:
1. Dari kelola data jenis vendor, masukkan “2” untuk memilih menu “Tambah jenis vendor”. 
2. Masukkan jenis vendor baru. 

Lihat laporan kerjasama dengan vendor 
1. Lihat semua laporan kerjasama: 
2. Masukkan “4” untuk memilih menu “Lihat laporan kerja sama dengan vendor”. 
3. Masukkan “1” untuk memilih menu “Lihat semua laporan kerjasama”. 
4. Masukkan “1” untuk memilih menu “Lihat laporan kerjasama spesifik”. 

Lihat frekuensi kerjasama semua vendor: 
1. Dari lihat laporan kerjasama dengan vendor, masukkan “2” untuk memilih menu “Lihat frekuensi kerjasama semua vendor”. 
2. Masukkan “1” untuk memilih menu “Lihat frekuensi kerjasama vendor spesifik”. 
3. Masukkan ID vendor. 

Lihat laporan event 
Lihat event terdekat: 
1. Masukkan “1” untuk memilih menu “Lihat laporan event”. 
2. Masukkan “1” untuk memilih menu “Lihat event terdekat”. 

Lihat event yang telah selesai: dari lihat laporan event, masukkan “2” untuk memilih menu “lihat event yang telah selesai. 

Lihat event yang dibatalkan: dari lihat laporan event, masukkan “3” untuk memilih menu “lihat event yang dibatalkan”. 

Laporan berdasarkan jenis event: 
1. Dari lihat laporan event, masukkan “4” untuk memilih menu “laporan berdasarkan jenis event”. 
2. Masukkan ID jenis event. 

Fitur bagi asisten: 
Keloa data klien
Lihat data klien:
1. Masukkan “1” untuk memilih menu “Kelola data klien”. 
2. Masukkan “1” untuk memilih menu “Lihat data klien”. Semua data klien akan muncul. 
3. Masukkan “1” untuk memilih menu “Lihat data klien spesifik”. 
4. Masukkan ID klien.  

Edit data klien: 
1. Dari lihat data klien spesifik, masukkan “1” untuk memilih menu “Edit data klien”. 
2. Masukkan nama, alamat, telepon, dan email baru dari klien. 

Hapus data klien: 
1. Dari lihat data klien spesifik, masukkan “2” untuk memilih menu “Hapus data klien”. 
2. Masukkan “1” untuk mengkonfirmasi penghapusan klien, masukkan “2” untuk membatalkan. 
3. Tambah klien: Masukkan username, password, nama, alamat, no telepon, email, dan tanggal registrasi. 

Kelola data event 
Lihat data event:
1. Masukkan “1” untuk memilih menu “Kelola data event”. 
2. Masukkan “1” untuk memilih menu “Lihat data event”. Semua data event akan muncul. 
3. Masukkan “1” untuk memilih menu “Lihat data event spesifik”. 
4. Masukkan ID event.  

Lihat rincian budgeting: dari lihat data event spesifik, masukkan “1” untuk melihat rincian budgeting. 

Lihat total harga deadling: dari lihat data event spesifik, masukkan “1” untuk melihat total harga dealing .

Tambah harga dealing: 
1. Dari lihat data event spesifik, masukkan “2” untuk tambah harga dealing. 
2. Masukkan ID vendor. 
3. Masukkan harga dealing. 

Edit harga dealing: 
1. Dari lihat data event spesifik, masukkan “3” untuk edit harga dealing. 
2. Masukkan ID vendor. 
3. Masukkan harga dealing.
   
Edit event: 
1. Dari lihat data event spesifik, masukkan “2” untuk memilih menu “Edit data event”. 
2. Masukkan nama, tanggal, jumlah undangan, lokasi, dan total budget. 

Hapus event: 
1. Dari lihat data event spesifik, masukkan “3” untuk memilih menu “Hapus data event”. 
2. Masukkan “1” untuk mengkonfirmasi penghapusan event, masukkan “2” untuk membatalkan. 
3. Tambah event: nama, tanggal event, jumlah undangan, lokasi, status event, total budget, ID klien, dan ID jenis event. 

Laporan event 
Lihat event yang telah selesai: 
1. Masukkan “1” untuk memilih menu “Lihat laporan event”. 
2. Dari lihat laporan event, masukkan “2” untuk memilih menu “lihat event yang telah selesai. 

Lihat event yang dibatalkan: dari lihat laporan event, masukkan “2” untuk memilih menu “lihat event yang sedang berlangsung”. 

Laporan berdasarkan jenis event: 
1. Dari lihat laporan event, masukkan “3” untuk memilih menu “laporan berdasarkan jenis event”. 
2. Masukkan ID jenis event. 

Lihat data vendor 
Lihat semua vendor:
1. Masukkan “4” untuk memilih menu “Lihat data vendor”. 
2. Masukkan “1” untuk memilih menu “Lihat semua vendor”. 

Lihat data vendor berdasarkan jenisnya:
1. Dari lihat data vendor, masukkan “2” untuk memilih menu “Lihat vendor berdasarkan jenisnya”. 
2. Masukkan ID jenis vendor.



