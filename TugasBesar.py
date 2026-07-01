# =================================================================
# PROYEK AKHIR ALGORITMA DAN PEMROGRAMAN - UNIVERSITAS AL AZHAR INDONESIA
# NAMA PROGRAM : IT-INSIGHT MINI QUIZ (DYNAMIC OPTIONS & RANDOMIZED EDITION)
# STRUKTUR DATA: DICTIONARY (O(1) ACCESS), LIST OF DICT (RIWAYAT), SET (KATEGORI)
# ALGORITMA: BUBBLE SORT (SORTING), TOTAL SKOR (REKURSI), OPTION SHUFFLING
# =================================================================

import sys
import random  # Mengimport modul random untuk pengacakan soal dan opsi

# 1. STRUKTUR DATA UTAMA: NESTED DICTIONARY (DATABASE SOAL)
# Catatan: Prefix pilihan (A, B, C, D) dihapus dari data mentah agar bisa diacak secara dinamis.
BANK_SOAL = {
    "General IT Knowledge": {
        "Level 1": [
            {"pertanyaan": "Siapakah pencipta awal sistem operasi Linux?", "pilihan": ["Bill Gates", "Linus Torvalds", "Steve Jobs", "Dennis Ritchie"], "jawaban": "Linus Torvalds"},
            {"pertanyaan": "Wi-Fi mengirimkan data tanpa kabel menggunakan gelombang...", "pilihan": ["Serat Optik", "Gelombang Radio", "Sinar Inframerah", "Sinar Laser"], "jawaban": "Gelombang Radio"},
            {"pertanyaan": "Siapakah penemu bahasa pemrograman Python?", "pilihan": ["James Gosling", "Guido van Rossum", "Bjarne Stroustrup", "Tim Berners-Lee"], "jawaban": "Guido van Rossum"},
            {"pertanyaan": "Perangkat keras mana yang bertugas sebagai alat input data?", "pilihan": ["Monitor", "Keyboard", "Printer", "Speaker"], "jawaban": "Keyboard"},
            {"pertanyaan": "Apakah kepanjangan dari istilah WWW?", "pilihan": ["World Wide Web", "World Whole Web", "Wide World Web", "Web World Wide"], "jawaban": "World Wide Web"},
            {"pertanyaan": "Siapakah penemu komputer pertama 'Analytical Engine'?", "pilihan": ["Alan Turing", "Charles Babbage", "Ada Lovelace", "John von Neumann"], "jawaban": "Charles Babbage"},
            {"pertanyaan": "Perusahaan manakah yang mengembangkan OS Windows?", "pilihan": ["Apple", "Microsoft", "Google", "IBM"], "jawaban": "Microsoft"},
            {"pertanyaan": "Manakah komponen yang merupakan otak utama komputer?", "pilihan": ["RAM", "CPU", "Harddisk", "GPU"], "jawaban": "CPU"},
            {"pertanyaan": "Bluetooth bekerja menggunakan koneksi nirkabel jarak...", "pilihan": ["Jauh", "Pendek", "Antariksa", "Global"], "jawaban": "Pendek"},
            {"pertanyaan": "Apakah fungsi utama dari perangkat keras bernama Monitor?", "pilihan": ["Menyimpan Data", "Menampilkan Visual", "Memproses Logika", "Mencetak Teks"], "jawaban": "Menampilkan Visual"}
        ],
        "Level 2": [
            {"pertanyaan": "Memori super cepat yang menjembatani CPU dan RAM adalah...", "pilihan": ["SSD", "Cache Memory", "ROM", "Flashdisk"], "jawaban": "Cache Memory"},
            {"pertanyaan": "Algoritma page replacement yang menghapus halaman paling lama tidak diakses adalah...", "pilihan": ["FIFO", "LRU (Least Recently Used)", "LFU", "Random"], "jawaban": "LRU (Least Recently Used)"},
            {"pertanyaan": "Algoritma page replacement yang menghapus halaman berdasarkan frekuensi paling sedikit dipakai adalah...", "pilihan": ["FIFO", "LFU (Least Frequently Used)", "LRU", "Optimal"], "jawaban": "LFU (Least Frequently Used)"},
            {"pertanyaan": "Algoritma substitusi halaman memori yang memakai prinsip masuk-pertama keluar-pertama adalah...", "pilihan": ["LRU", "FIFO (First In First Out)", "LFU", "LIFO"], "jawaban": "FIFO (First In First Out)"},
            {"pertanyaan": "Sensor apa pada kacamata VR yang mendeteksi rotasi gerakan kepala?", "pilihan": ["Proximity", "Gyroscope", "Barometer", "Light Sensor"], "jawaban": "Gyroscope"},
            {"pertanyaan": "Penyimpanan volatile yang datanya hilang saat komputer dimatikan adalah...", "pilihan": ["Harddisk", "RAM", "SSD", "Flashdisk"], "jawaban": "RAM"},
            {"pertanyaan": "Tempat penyimpanan data jangka panjang non-volatile berbasis piringan magnetik disebut...", "pilihan": ["SSD", "HDD", "RAM", "Cache"], "jawaban": "HDD"},
            {"pertanyaan": "Penyimpanan modern kecepatan tinggi tanpa piringan bergerak adalah...", "pilihan": ["HDD", "SSD", "Disket", "Pita Magnetik"], "jawaban": "SSD"},
            {"pertanyaan": "Perangkat jaringan yang bertugas menghubungkan dua subnet berbeda adalah...", "pilihan": ["Switch", "Router", "Hub", "Repeater"], "jawaban": "Router"},
            {"pertanyaan": "Perangkat pintar yang menyalurkan data hanya ke MAC Address tujuan dalam satu LAN adalah...", "pilihan": ["Hub", "Switch", "Repeater", "Bridge"], "jawaban": "Switch"},
            {"pertanyaan": "Berapa jumlah total lapisan (layer) pada OSI Reference Model?", "pilihan": ["5 Layer", "7 Layer", "4 Layer", "9 Layer"], "jawaban": "7 Layer"},
            {"pertanyaan": "Protokol yang memberikan IP Address secara otomatis ke perangkat klien adalah...", "pilihan": ["DNS", "DHCP", "FTP", "HTTP"], "jawaban": "DHCP"},
            {"pertanyaan": "Sistem yang menerjemahkan nama domain situs menjadi alamat IP adalah...", "pilihan": ["DHCP", "DNS", "FTP", "SMTP"], "jawaban": "DNS"},
            {"pertanyaan": "Sistem pertahanan penapis lalu lintas jaringan yang mencegah akses ilegal adalah...", "pilihan": ["Router", "Firewall", "Switch", "Gateway"], "jawaban": "Firewall"},
            {"pertanyaan": "Alamat logika 32-bit yang digunakan untuk identifikasi perangkat IPv4 disebut...", "pilihan": ["MAC Address", "IP Address", "Subnet Mask", "DNS Tag"], "jawaban": "IP Address"}
        ],
        "Level 3": [
            {"pertanyaan": "Siklus paling awal CPU mengambil instruksi dari memori utama disebut...", "pilihan": ["Decode", "Fetch", "Execute", "Store"], "jawaban": "Fetch"},
            {"pertanyaan": "Siklus CPU menerjemahkan kode instruksi binari menjadi perintah sirkuit dinamakan...", "pilihan": ["Fetch", "Decode", "Execute", "Writeback"], "jawaban": "Decode"},
            {"pertanyaan": "Siklus CPU menjalankan perintah operasi setelah diterjemahkan disebut...", "pilihan": ["Fetch", "Execute", "Decode", "Interrupt"], "jawaban": "Execute"},
            {"pertanyaan": "Profesi IT yang fokus merancang model AI dan Machine Learning adalah...", "pilihan": ["Web Developer", "Data Scientist", "Network Engineer", "QA Analyst"], "jawaban": "Data Scientist"},
            {"pertanyaan": "Profesi IT yang bertugas membangun infrastruktur server dan otomasi deployment cloud adalah...", "pilihan": ["Frontend", "DevOps Engineer", "UI/UX Designer", "Data Entry"], "jawaban": "DevOps Engineer"},
            {"pertanyaan": "Siapakah yang bertugas menguji celah keamanan sistem secara legal (ethical hacker)?", "pilihan": ["DBA", "Penetration Tester", "Business Analyst", "System Analyst"], "jawaban": "Penetration Tester"},
            {"pertanyaan": "Profesi IT yang bertanggung jawab merancang tampilan antarmuka visual aplikasi adalah...", "pilihan": ["Backend", "UI/UX Designer", "Data Engineer", "Product Owner"], "jawaban": "UI/UX Designer"},
            {"pertanyaan": "Spesialis IT yang bertugas mengelola, mengoptimalkan, dan mengamankan pangkalan data adalah...", "pilihan": ["Fullstack", "Database Administrator (DBA)", "SEO", "IT Support"], "jawaban": "Database Administrator (DBA)"},
            {"pertanyaan": "Insinyur yang menguasai pengerjaan sisi klien (frontend) dan sisi server (backend) dinamakan...", "pilihan": ["Frontend dev", "Fullstack Developer", "Backend dev", "Scrum Master"], "jawaban": "Fullstack Developer"},
            {"pertanyaan": "Komponen CPU yang berfungsi melakukan perhitungan matematika dan perbandingan logika adalah...", "pilihan": ["Control Unit", "Arithmetic Logic Unit (ALU)", "Register", "Cache"], "jawaban": "Arithmetic Logic Unit (ALU)"},
            {"pertanyaan": "Komponen CPU yang bertugas mengatur jalannya sirkuit dan sinkronisasi kendali aliran data adalah...", "pilihan": ["ALU", "Control Unit (CU)", "SSD", "CMOS"], "jawaban": "Control Unit (CU)"},
            {"pertanyaan": "Lokasi penyimpanan internal kecil di dalam CPU dengan kecepatan akses terendah/tercepat adalah...", "pilihan": ["RAM", "Register", "Cache L3", "Virtual Memory"], "jawaban": "Register"},
            {"pertanyaan": "Layanan cloud di mana pengguna menyewa infrastruktur komputasi murni virtual (seperti VPS) adalah...", "pilihan": ["SaaS", "IaaS (Infrastructure as a Service)", "PaaS", "FaaS"], "jawaban": "IaaS (Infrastructure as a Service)"},
            {"pertanyaan": "Layanan cloud seperti Google Workspace di mana pengguna langsung memakai software jadi adalah...", "pilihan": ["IaaS", "SaaS (Software as a Service)", "PaaS", "DaaS"], "jawaban": "SaaS (Software as a Service)"},
            {"pertanyaan": "Platform awan penyedia lingkungan run-time siap pakai tanpa pusing kelola OS server adalah...", "pilihan": ["IaaS", "PaaS (Platform as a Service)", "SaaS", "BaaS"], "jawaban": "PaaS (Platform as a Service)"},
            {"pertanyaan": "Protokol transfer enkripsi aman berbasis SSL/TLS untuk menjelajah web adalah...", "pilihan": ["HTTP", "HTTPS", "FTP", "SSH"], "jawaban": "HTTPS"},
            {"pertanyaan": "Kombinasi firmware dasar yang menyimpan konfigurasi hardware boot komputer awal adalah...", "pilihan": ["Kernel", "BIOS / UEFI", "Drivers", "Bootloader"], "jawaban": "BIOS / UEFI"},
            {"pertanyaan": "Komponen inti sistem operasi yang menjembatani software aplikasi dan hardware fisik adalah...", "pilihan": ["GUI Shell", "Kernel", "Compiler", "File Explorer"], "jawaban": "Kernel"},
            {"pertanyaan": "Standar pengalamatan fisik permanen yang unik dari pabrik pada kartu jaringan (NIC) disebut...", "pilihan": ["IP Address", "MAC Address", "Ports Number", "Subnet ID"], "jawaban": "MAC Address"},
            {"pertanyaan": "Satuan unit data digital terkecil dalam sistem komputasi bernilai 0 atau 1 dinamakan...", "pilihan": ["Byte", "Bit", "Kilobyte", "Word"], "jawaban": "Bit"}
        ]
    },
    "Tebak Code Python": {
        "Level 1": [
            {"pertanyaan": "Berapakah output dari:\nx = 5\nx += 3\nprint(x)", "pilihan": ["5", "8", "3", "Error"], "jawaban": "8"},
            {"pertanyaan": "Berapakah hasil dari operasi modulus berikut:\nprint(10 % 3)", "pilihan": ["3", "1", "0", "3.33"], "jawaban": "1"},
            {"pertanyaan": "Apakah output dari:\na = 10\nif a > 15:\n    print('X')\nelse:\n    print('Y')", "pilihan": ["X", "Y", "XY", "None"], "jawaban": "Y"},
            {"pertanyaan": "Berapa kali perulangan ini mencetak kata 'IT'?\nfor i in range(3):\n    print('IT')", "pilihan": ["2 kali", "3 kali", "4 kali", "0 kali"], "jawaban": "3 kali"},
            {"pertanyaan": "Apakah tipe data dari variabel berikut:\nnilai = 4.5", "pilihan": ["int", "float", "str", "bool"], "jawaban": "float"},
            {"pertanyaan": "Berapakah output dari logika boolean berikut:\nprint(True and False)", "pilihan": ["True", "False", "None", "Error"], "jawaban": "False"},
            {"pertanyaan": "Perhatikan loop berikut:\nc = 0\nwhile c < 2:\n    c += 1\nprint(c)", "pilihan": ["0", "2", "1", "3"], "jawaban": "2"},
            {"pertanyaan": "Apakah hasil dari pengbagungan string berikut:\nprint('Kuis' + 'IT')", "pilihan": ["Kuis shadow", "KuisIT", "Kuis+IT", "Error"], "jawaban": "KuisIT"},
            {"pertanyaan": "Perhatikan kondisi berikut:\nx = 5\nif x > 2 and x < 10:\n    print('A')\nelse:\n    print('B')", "pilihan": ["B", "A", "AB", "None"], "jawaban": "A"},
            {"pertanyaan": "Keyword apa yang dipakai untuk menghentikan loop secara paksa?", "pilihan": ["continue", "break", "pass", "exit"], "jawaban": "break"}
        ],
        "Level 2": [
            {"pertanyaan": "Apakah output dari:\ndef sapa(nama):\n    return 'Halo ' + nama\nprint(sapa('Budi'))", "pilihan": ["Halo nama", "Halo Budi", "Budi", "Error"], "jawaban": "Halo Budi"},
            {"pertanyaan": "Method string apa untuk mengubah teks menjadi huruf kapital semua?", "pilihan": ["lower()", "upper()", "strip()", "split()"], "jawaban": "upper()"},
            {"pertanyaan": "Berapakah output dari panjang list berikut:\ndata = [10, 20, 30]\nprint(len(data))", "pilihan": ["10", "3", "20", "1"], "jawaban": "3"},
            {"pertanyaan": "Bagaimanakah cara mengambil angka 99 dari list: angka = [11, 99, 45]?", "pilihan": ["angka[0]", "angka[1]", "angka[2]", "angka[-3]"], "jawaban": "angka[1]"},
            {"pertanyaan": "Method list apa yang dipakai untuk menambah elemen baru di bagian akhir?", "pilihan": ["pop()", "append()", "remove()", "insert()"], "jawaban": "append()"},
            {"pertanyaan": "Berapakah output dari:\nuser = {'id': 12, 'nama': 'Ali'}\nprint(user['nama'])", "pilihan": ["id", "Ali", "12", "nama"], "jawaban": "Ali"},
            {"pertanyaan": "Manakah dari tipe data koleksi berikut yang bersifat immutable (tidak bisa diubah)?", "pilihan": ["List", "Tuple", "Dictionary", "Set"], "jawaban": "Tuple"},
            {"pertanyaan": "Berapakah nilai keluaran dari metode string berikut:\nteks = '  python  '\nprint(teks.strip())", "pilihan": ["'  python'", "'python'", "'python  '", "'py thon'"], "jawaban": "'python'"},
            {"pertanyaan": "Apakah output dari slice list berikut:\nkata = ['P', 'Y', 'T', 'H', 'O', 'N']\nprint(kata[0:2])", "pilihan": ["['P']", "['P', 'Y']", "['P', 'Y', 'T']", "['Y', 'T']"], "jawaban": "['P', 'Y']"},
            {"pertanyaan": "Apakah hasil dari eksekusi fungsi tanpa return statement ini:\ndef tes():\n    x = 5\nprint(tes())", "pilihan": ["5", "None", "Error", "0"], "jawaban": "None"},
            {"pertanyaan": "Berapakah output dari:\nlogs = [200, 404, 200, 500]\nprint(logs.count(200))", "pilihan": ["1", "2", "3", "4"], "jawaban": "2"},
            {"pertanyaan": "Keyword apakah yang digunakan untuk mendefinisikan fungsi di Python?", "pilihan": ["function", "def", "func", "define"], "jawaban": "def"},
            {"pertanyaan": "Bagaimana cara mengubah isi dictionary agar usia menjadi 20: profil = {'usia': 19}?", "pilihan": ["profil.add('usia', 20)", "profil['usia'] = 20", "profil[0] = 20", "profil.update(20)"], "jawaban": "profil['usia'] = 20"},
            {"pertanyaan": "Apakah output dari kodingan berikut:\nitems = [1, 2, 3]\nitems.pop()\nprint(items)", "pilihan": ["[1]", "[1, 2]", "[2, 3]", "[]"], "jawaban": "[1, 2]"},
            {"pertanyaan": "Berapakah hasil dari perkalian list berikut:\nprint([0] * 3)", "pilihan": ["[0]", "[0, 0, 0]", "0", "Error"], "jawaban": "[0, 0, 0]"}
        ],
        "Level 3": [
            {"pertanyaan": "Berapakah hasil pemanggilan fungsi rekursif faktorial(3) ini:\ndef faktorial(n):\n    if n <= 1: return 1\n    return n * faktorial(n-1)", "pilihan": ["3", "6", "1", "9"], "jawaban": "6"},
            {"pertanyaan": "Kompleksitas Big-O dari pencarian elemen dengan mencocokkan key pada Dictionary adalah...", "pilihan": ["O(N)", "O(1)", "O(log N)", "O(N^2)"], "jawaban": "O(1)"},
            {"pertanyaan": "Kompleksitas Big-O dari pencarian linear sekuensial menelusuri List satu demi satu adalah...", "pilihan": ["O(1)", "O(N)", "O(N log N)", "O(2^N)"], "jawaban": "O(N)"},
            {"pertanyaan": "Berapakah hasil konversi kode ASCII karakter berikut:\nprint(chr(ord('A') + 1))", "pilihan": ["A", "B", "66", "Error"], "jawaban": "B"},
            {"pertanyaan": "Manakah tipe data koleksi Python yang secara otomatis membuang elemen duplikat?", "pilihan": ["List", "Set", "Tuple", "Dictionary"], "jawaban": "Set"},
            {"pertanyaan": "Apakah hasil operasi irisan set berikut:\na = {1, 2, 3}; b = {2, 3, 4}\nprint(a & b)", "pilihan": ["{1, 4}", "{2, 3}", "{1, 2, 3, 4}", "set()"], "jawaban": "{2, 3}"},
            {"pertanyaan": "Berapakah output dari fungsi rekursif berikut:\ndef jumlah(n):\n    if n == 1: return 1\n    return n + jumlah(n-1)\nprint(jumlah(4))", "pilihan": ["4", "10", "6", "8"], "jawaban": "10"},
            {"pertanyaan": "Apakah output dari pengurutan berikut:\na = [3, 1, 2]\na.sort()\nprint(a)", "pilihan": ["[3, 2, 1]", "[1, 2, 3]", "[3, 1, 2]", "None"], "jawaban": "[1, 2, 3]"},
            {"pertanyaan": "Manakah algoritma sorting yang menggunakan metode Divide and Conquer secara rekursif?", "pilihan": ["Bubble Sort", "Merge Sort", "Insertion Sort", "Selection Sort"], "jawaban": "Merge Sort"},
            {"pertanyaan": "Struktur data Nested Dictionary menjamin pencarian kunci kuis berada pada performa...", "pilihan": ["Linear", "Konstan / O(1)", "Kuadratik", "Eksponensial"], "jawaban": "Konstan / O(1)"},
            {"pertanyaan": "Apa yang terjadi jika fungsi rekursif tidak memiliki base case?", "pilihan": ["Selesai Normal", "Stack Overflow / RecursionError", "Nilai Nol", "Runtime Ok"], "jawaban": "Stack Overflow / RecursionError"},
            {"pertanyaan": "Apakah hasil operasi gabungan set berikut:\ns1 = {1}; s2 = {2}\nprint(s1.union(s2))", "pilihan": ["{1}", "{1, 2}", "{3}", "set()"], "jawaban": "{1, 2}"},
            {"pertanyaan": "Berapakah output fungsi berikut:\nprint(chr(65))", "pilihan": ["65", "A", "B", "Error"], "jawaban": "A"},
            {"pertanyaan": "Berapakah hasil fungsi berikut:\nprint(ord('B'))", "pilihan": ["65", "66", "A", "2"], "jawaban": "66"},
            {"pertanyaan": "Manakah kompleksitas Big-O yang paling tidak efisien untuk data skala masif?", "pilihan": ["O(1)", "O(N^2)", "O(log N)", "O(N)"], "jawaban": "O(N^2)"},
            {"pertanyaan": "Istilah pemanfaatan AI untuk membantu menulis draf baris kode kodingan disebut...", "pilihan": ["Cyber Security", "AI-Augmented Programming", "Cloud Storage", "IoT"], "jawaban": "AI-Augmented Programming"},
            {"pertanyaan": "Algoritma sorting yang bekerja dengan cara menukar elemen berdekatan secara berulang adalah...", "pilihan": ["Quick Sort", "Bubble Sort", "Merge Sort", "Radix Sort"], "jawaban": "Bubble Sort"},
            {"pertanyaan": "Apakah output dari:\nprint([x for x in range(3) if x % 2 == 0])", "pilihan": ["[1]", "[0, 2]", "[0, 1, 2]", "[]"], "jawaban": "[0, 2]"},
            {"pertanyaan": "Berapakah panjang elemen dari objek set berikut: s = {1, 2, 2, 3}?", "pilihan": ["4", "3", "2", "1"], "jawaban": "3"},
            {"pertanyaan": "Konsep memecahan masalah besar menjadi sub-masalah kecil yang serupa dinamakan...", "pilihan": ["Enkapsulasi", "Dekomposisi / Rekursi", "Inheritansi", "Polimorfisme"], "jawaban": "Dekomposisi / Rekursi"}
        ]
    }
}

KATEGORI_SET = set(BANK_SOAL.keys())

# DATABASE RIWAYAT LEADERBOARD GLOBAL
RIWAYAT_SKOR = [
    {"nama": "Ahmad_UAI", "kategori": "General IT Knowledge", "level": 3, "skor": 85},
    {"nama": "Siti_Informatika", "kategori": "Tebak Code Python", "level": 1, "skor": 90}
]

def tampilkan_menu_utama():
    print("\n" + "="*50)
    print("           IT-INSIGHT MINI QUIZ")
    print("     Mata Kuliah: Fondasi Pemrograman")
    print("="*50)
    print("[1] MULAI KUIS")
    print("[2] LIHAT LEADERBOARD & STATISTIK")
    print("[3] KELUAR APLIKASI")
    print("="*50)

    while True:
        pilihan = input("Pilih menu (1/2/3): ").strip()
        if pilihan in ["1", "2", "3"]:
            return pilihan
        print("[Peringatan] Pilihan tidak valid!")

def hitung_total_skor_rekursif(daftar_riwayat, indeks=0):
    if indeks >= len(daftar_riwayat):
        return 0
    return daftar_riwayat[indeks]["skor"] + hitung_total_skor_rekursif(daftar_riwayat, indeks + 1)

def tampilkan_leaderboard():
    print("\n" + "="*60)
    print("         PAPAN PERINGKAT UTAMA (LEADERBOARD)")
    print("="*60)
    
    if not RIWAYAT_SKOR:
        print("Belum ada riwayat pengerjaan kuis.")
        print("="*60)
        return

    data_sort = list(RIWAYAT_SKOR)
    n = len(data_sort)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_sort[j]["skor"] < data_sort[j+1]["skor"]:
                data_sort[j], data_sort[j+1] = data_sort[j+1], data_sort[j]
                
    print(f"{'Rank':<6} | {'Nama Pemain':<16} | {'Kategori':<22} | {'Lvl':<4} | {'Skor':<5}")
    print("-"*65)
    for rank, data in enumerate(data_sort, 1):
        print(f"#{rank:<5} | {data['nama']:<16} | {data['kategori']:<22} | Lvl {data['level']:<1} | {data['skor']:<5}")
    print("-"*65)
    
    total_akumulasi = hitung_total_skor_rekursif(RIWAYAT_SKOR)
    print(f"Total Akumulasi Nilai Semua Pemain (Fungsi Rekursi): {total_akumulasi} Poin")
    print("="*60)

# REVIEW JAWABAN PEMAIN
def review_jawaban_pemain(daftar_soal, urutan_pilihan_diacak, jawaban_user):
    print("\n" + "-"*20 + " REVIEW EVALUASI JAWABAN " + "-"*20)
    for idx, soal in enumerate(daftar_soal):
        print(f"\nSoal {idx+1}: {soal['pertanyaan']}")
        
        jawab_huruf = jawaban_user[idx]
        pilihan_soal_ini = urutan_pilihan_diacak[idx]
        
        # Mapping huruf A/B/C/D kembali ke teks asli untuk di-review
        label_map = {"A": 0, "B": 1, "C": 2, "D": 3}
        if jawab_huruf in label_map:
            teks_jawab_user = pilihan_soal_ini[label_map[jawab_huruf]]
        else:
            teks_jawab_user = "Dilewati (Belum Dijawab)"
            
        print(f"  Pilihan Anda : {jawab_huruf} ({teks_jawab_user})")
        print(f"  Kunci Jawaban: {soal['jawaban']}")
        
        if teks_jawab_user == soal['jawaban']:
            print("  Status       : ✅ BENAR")
        else:
            print("  Status       : ❌ SALAH")
    print("-" * 65)

def jalankan_gameplay(nama_user, kategori, level_target):
    if level_target == 1:
        nyawa = 4
    elif level_target == 2:
        nyawa = 3
    else:
        nyawa = 1

    kunci_level = f"Level {level_target}"
    master_soal = BANK_SOAL[kategori][kunci_level]
    total_soal = len(master_soal)

    # Mengacak urutan kemunculan soal
    daftar_soal = random.sample(master_soal, total_soal)

    # LOGIKA BARU: Mengacak urutan opsi pilihan (A, B, C, D) secara dinamis untuk setiap soal
    urutan_pilihan_diacak = []
    for soal in daftar_soal:
        opsi_copy = list(soal["pilihan"])
        random.shuffle(opsi_copy)  # Mengocok isi pilihan secara random
        urutan_pilihan_diacak.append(opsi_copy)

    sudah_dijawab = [False] * total_soal
    jawaban_user = [None] * total_soal

    idx = 0
    lulus = True

    print("\n" + "="*50)
    print(f"KATEGORI : {kategori.upper()}")
    print(f"TINGKATAN: LEVEL {level_target} | TOTAL SOAL: {total_soal}")
    print("="*50)
    print("Ketik 'S' untuk Surrend, 'N' untuk Next, 'P' untuk Previous")
    print("-"*50)

    while idx < total_soal:
        soal = daftar_soal[idx]
        pilihan_sekarang = urutan_pilihan_diacak[idx]
        
        print(f"\n[Soal {idx+1} dari {total_soal}]  |  Sisa Nyawa: {'❤️' * nyawa if nyawa > 0 else 'Mati'}")
        print(soal["pertanyaan"])
        
        # Tampilkan pilihan yang sudah diacak dengan label abjad dinamis
        labels = ["A", "B", "C", "D"]
        for i, opsi in enumerate(pilihan_sekarang):
            print(f"{labels[i]}. {opsi}")

        opsi_valid = ["A", "B", "C", "D", "S"]
        nav_info = "Jawaban (A/B/C/D)"

        if idx > 0:
            opsi_valid.append("P")
            nav_info += ", P (Prev)"
        if idx < total_soal - 1:
            opsi_valid.append("N")
            nav_info += ", N (Next)"

        while True:
            jawaban = input(f"Masukkan {nav_info} atau S (Surrend): ").strip().upper()
            if jawaban in opsi_valid:
                break
            print("[Peringatan] Input salah! Harap perhatikan menu navigasi yang tersedia.")

        if jawaban == "S":
            print("\n" + "~"*50)
            print("Next time di siapkan lebih matang lagi ya")
            print("~"*50)
            return "SURREND"

        elif jawaban == "P":
            idx -= 1
            continue

        elif jawaban == "N":
            idx += 1
            continue

        else:
            jawaban_user[idx] = jawaban
            
            # Ambil nilai teks asli berdasarkan indeks abjad yang ditekan user
            label_map = {"A": 0, "B": 1, "C": 2, "D": 3}
            teks_pilihan_user = pilihan_sekarang[label_map[jawaban]]
            
            if not sudah_dijawab[idx]:
                sudah_dijawab[idx] = True
                
                # Menguji teks jawaban, bukan lagi sekadar huruf "B" kaku
                if teks_pilihan_user == soal["jawaban"]:
                    print("\n>> Jawaban anda benar! <<")
                else:
                    nyawa -= 1
                    print("\n>> Jawaban anda salah! <<")
                    print(f"Jawaban benar : {soal['jawaban']}")

                    if nyawa <= 0:
                        lulus = False
                        break
            else:
                print("\n[Info] Anda sudah mengubah/mengisi soal ini sebelumnya.")
                if teks_pilihan_user == soal["jawaban"]:
                    print("Status data: Benar.")
                else:
                    print("Status data: Salah.")
                    print(f"Jawaban benar : {soal['jawaban']}")
            
            idx += 1

    # PROSES KALKULASI SKOR AKHIR LEVEL
    jawaban_benar_count = 0
    for i in range(total_soal):
        label_map = {"A": 0, "B": 1, "C": 2, "D": 3}
        user_ans_letter = jawaban_user[i]
        if user_ans_letter in label_map:
            if urutan_pilihan_diacak[i][label_map[user_ans_letter]] == daftar_soal[i]["jawaban"]:
                jawaban_benar_count += 1

    skor_akhir = int((jawaban_benar_count / total_soal) * 100) if total_soal > 0 else 0
    RIWAYAT_SKOR.append({"nama": nama_user, "kategori": kategori, "level": level_target, "skor": skor_akhir})

    print("\n" + "="*45)
    print("             HASIL EVALUASI")
    print("="*45)
    print(f"Skor Akhir Level Ini : {skor_akhir} Poin")
    print(f"Total Jawaban Benar  : {jawaban_benar_count} dari {total_soal} Soal")
    print("-"*45)

    if level_target == 1:
        if not lulus or nyawa <= 0:
            print("Mohon maaf anda belum bisa lanjut ke level berikutnya")
            print("tingkat pemahaman anda c, lebih semangat lagi ya, jangan menyerah :")
        elif nyawa == 4:
            print("Selamat nyawa anda utuh")
            print("tingkat pemahaman anda A, Selamat anda mendapat nilai terbaik.")
        elif nyawa == 3:
            print("Anda bisa lanjut ke level berikutnya")
            print("tingkat pemahaman anda A-, Sudah bagus tapi masih bisa ditingkatkan, semangat ya")
        elif nyawa >= 2:
            print("Anda bisa lanjut ke level berikutnya")
            print("tingkat pemahaman anda B, lebih ditingkatkan lagi ya, semangatt")

    elif level_target == 2:
        if not lulus:
            print("Mohon maaf anda belum bisa lanjut ke level berikutnya")
            print("tingkat pemahaman anda c. Tetap semangat, jangan menyerah!")
        elif nyawa == 3:
            print("Anda bisa lanjut ke level berikutnya")
            print("tingkat pemahaman anda A. Luar biasa, pertahankan!")
        else:
            print("Anda bisa lanjut ke level berikutnya")
            print("tingkat pemahaman anda B. Sudah cukup baik!")

    elif level_target == 3:
        if lulus:
            print("STATUS: LULUS EVALUASI AKHIR")
            print("Selamat! Anda telah menyelesaikan seluruh tingkatan materi.")
        else:
            print("STATUS: TIDAK LULUS")
            print("Mohon maaf, Anda belum berhasil melewati level penutup.")

    print("="*45)
    
    opsi_review = input("Apakah anda ingin melihat review jawaban level ini? (Y/T): ").strip().upper()
    if opsi_review == "Y":
        review_jawaban_pemain(daftar_soal, urutan_pilihan_diacak, jawaban_user)
        
    return "LULUS" if lulus else "GAGAL"

def navigasi_setelah_kuis(status_hasil, level_aktif):
    if level_aktif == 3 and status_hasil == "LULUS":
        print("\n[1] Kembali ke Halaman Utama")
        while True:
            opsi = input("Pilih tindakan (1): ").strip()
            if opsi == "1": return "HOME"
            print("Input tidak valid!")

    if status_hasil == "LULUS":
        print("\n[1] Lanjut ke Level Berikutnya")
        print("[2] Kembali ke Halaman Utama")
        while True:
            opsi = input("Pilih tindakan (1/2): ").strip()
            if opsi == "1": return "LANJUT"
            if opsi == "2": return "HOME"
            print("Input tidak valid!")
    else:
        print("\n[1] Ulang Level Ini")
        print("[2] Kembali ke Halaman Utama")
        while True:
            opsi = input("Pilih tindakan (1/2): ").strip()
            if opsi == "1": return "ULANG"
            if opsi == "2": return "HOME"
            print("Input tidak valid!")

def main():
    while True:
        menu_pilihan = tampilkan_menu_utama()
        if menu_pilihan == "3":
            print("\nTerima kasih telah menggunakan sistem kuis. Sampai jumpa!")
            sys.exit()
        elif menu_pilihan == "2":
            tampilkan_leaderboard()
            input("\nTekan Enter untuk kembali ke Menu Utama...")
            continue

        print("\n--- REGISTRASI PESERTA ---")
        nama = input("Masukkan Nama Pelajar IT: ").strip()
        if not nama:
            nama = "Pelajar_Anonymous"

        print("\n--- PILIH KATEGORI KUIS ---")
        list_kategori = list(KATEGORI_SET)
        for idx, kat in enumerate(list_kategori, 1):
            print(f"[{idx}] {kat}")

        while True:
            try:
                pilih_kat = int(input("Pilih nomor kategori: "))
                if 1 <= pilih_kat <= len(list_kategori):
                    kategori_pilihan = list_kategori[pilih_kat - 1]
                    break
            except ValueError:
                pass
            print("Pilihan kategori tidak tersedia!")

        level_sekarang = 1
        while level_sekarang <= 3:
            hasil = jalankan_gameplay(nama, kategori_pilihan, level_sekarang)

            if hasil == "SURREND":
                break

            tindakan = navigasi_setelah_kuis(hasil, level_sekarang)

            if tindakan == "HOME":
                break
            elif tindakan == "LANJUT":
                level_sekarang += 1
            elif tindakan == "ULANG":
                continue

if __name__ == "__main__":
    main()