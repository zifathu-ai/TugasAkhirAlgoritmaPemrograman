# **IT-Insight Mini Quiz**

### **1. Identitas & Latar Belakang Proyek**

* **Proyek:** **IT-Insight Mini Quiz**, aplikasi kuis berbasis *Command Line Interface* (CLI) untuk evaluasi mandiri pelajar IT.


* **Latar Belakang Masalah:**
* **The Theory-Practice Gap:** Kesenjangan antara hafalan teori dasar IT dengan kemampuan implementasi logika pemrograman secara praktis.
* **Kurangnya Media Evaluasi:** Ketiadaan media latihan mandiri dengan tekanan terkontrol (*low-stakes self-assessment*) sebelum ujian resmi.



### **2. Solusi & Tujuan Proyek**

* **Penyelesaian Masalah:** Proyek ini menyediakan media latihan interaktif yang mensimulasikan tekanan akademik melalui mekanika sistem nyawa dan umpan balik instan.
* **Tujuan Proyek:**
* Membangun media latihan mandiri yang terstruktur untuk mengukur kesiapan akademik.
* Mengimplementasikan konsep fondasi pemrograman Python dalam sistem yang terintegrasi.


* **Target Pengguna:** Pelajar IT tingkat pemula dan institusi pendidikan yang membutuhkan alat ukur pemahaman kurikulum.

### **3. Cakupan Materi (Kurikulum)**

Proyek ini memetakan 13 Bab kurikulum fondasi pemrograman ke dalam 2 kategori kuis:

* **Bab 1–4:** *Computational Thinking*, variabel, seleksi percabangan, dan perulangan.
* **Bab 5–8:** Fungsi, *string*, *list*, *tuple*, dan *dictionary* dasar.
* **Bab 9–13:** *Set*, *searching* & *sorting*, rekursi lanjut, *Big-O notation*, dan *AI-augmented programming*.

### **4. Konsep & Alur Sistem**

* **Konsep:** Menggunakan *gamification* (sistem nyawa dan *leaderboard*) untuk meningkatkan keterlibatan pengguna dalam lingkungan CLI yang simpel namun menantang.
* **Alur:** Pengguna melakukan registrasi, memilih kategori, melewati 3 level kesulitan dengan mekanika nyawa yang berbeda, lalu hasil akhirnya diproses ke *leaderboard*.

### **5. Fitur Sistem**

* **Fitur Wajib:**
* **Bank Soal:** Basis data soal multi-level menggunakan *nested dictionary*.
* **Quiz Random:** Pengacakan soal dan opsi jawaban (A, B, C, D) secara dinamis.
* **Scoring:** Perhitungan skor akhir berbasis persentase jawaban benar.
* **Leaderboard:** Menampilkan peringkat berdasarkan skor tertinggi.
* **Review Jawaban:** Evaluasi pasca-kuis untuk mencocokkan jawaban pemain dengan kunci jawaban.


* **Fitur Tambahan:**
* **Sistem Nyawa:** Simulasi tekanan dengan pembatasan kesalahan (L1: 4, L2: 3, L3: 1 nyawa).
* **Total Skor Rekursi:** Fungsi rekursif untuk mengakumulasi total poin seluruh pemain.
* **Fitur Surrender:** Opsi untuk mengakhiri kuis secara paksa saat pengguna merasa kewalahan.



### **6. Algoritma yang Digunakan**

* **Bubble Sort:** Digunakan untuk mengurutkan data skor secara menurun (*descending*) pada *leaderboard*.
* **Fungsi Rekursif:** Digunakan dalam modul perhitungan total akumulasi nilai seluruh pemain.
* **Manipulasi ASCII & Pengacakan:** Menggunakan `random.shuffle()` untuk pengacakan opsi dan manipulasi data melalui fungsi `ord()` dan `chr()`.

### **7. Rencana Pengembangan**

Proyek ini mengikuti metodologi **SDLC Waterfall** dalam 5 fase:

* **Requirement Analysis & Design:** Identifikasi kebutuhan dan perancangan arsitektur sistem.
* **Implementation:** Penulisan kode Python untuk semua fitur.
* **Testing & Verification:** Pengujian fungsional modul (Black-box testing).
* **Deployment & Maintenance:** Publikasi di GitHub dan pemeliharaan bug.
* **Timeline:** Pengembangan direncanakan berlangsung selama 4 minggu mulai dari analisis desain hingga finalisasi dokumentasi.

## Identitas

* **Muhammad Raafi Putra Arya**
* **Raya Aulia Abdillah**
* **Zhilal Fathurrahman**
* **Panca PAmungkas**

**Mata Kuliah**: Praktikum Fondasi Pemrograman - Media Evaluasi Mandiri Pelajar IT 


* **Dosen**: Tri Aji Nugroho, S.T., M.T.
* **Semester**: Genap 2025/2026
