# Data Crawling
Data Crawling merupakan suatu teknik untuk mengambil data yang ada di website tertentu sesuai dengan keperluan yang akan diteliti. Dalam 
domain Zakat yang diperlukan adalah data - data dari website yang menampilkan informasi seputar Zakat, mulai dari aturan Zakat, definisi, ketentuan Zakat,
dan lain sebagainya. 
Untuk kebutuhan penelitian kali ini, informasi data berupa teks dari website yang memiliki informasi tentang Zakat ditentukan melalui tahapan berikut :
1. Penentuan website yang akan diambil informasinya
2. Identifikasi struktur website
3. Membuat tools Crawler menggunakan Python
4. Implementasi tools Crawler 

# Penentuan website yang akan diambil informasinya
Dalam tahapan ini ditentukan website yang akan diambil informasinya :
1. Bersumber dari website
	1. BAZNAS (https://baznas.go.id/)
	2. Rumah Zakat
	3. LAZ Al-Azhar
2. File digital
	1. Undang-undang Republik Indonesia no.23 tahun 2011 tentang Pengelolaan Zakat
	2. Buku hukum zakat dan wakaf terkait bab Zakat

# Identifikasi struktur website

Dalam mengidentifikasi struktur website yang akan di crawling, Peneliti menggunakan teknik identifikasi secara langsung menggunakan tools yang ada di browser,yaitu tools Inspect Element. 
Misalkan ketika akan mengcrawling data dari website BAZNAS. Disana akan ada tampilan atau page yang berkaitan dengan Zakat. Halaman yang akan diambil datanya yaitu 
https://baznas.go.id/zakat., lalu kita lihat strukturnya dengan menggunakan inspect element (Klik Kanan -> Inspect).

Dari satu page atau halaman akan ada beragam element, dan yang kita lihat adalah class element yang mengandung teks tentang Zakat.
Setelah itu Class element tersebut kita Copy dan kita masukan kedalam Script Crawler yang kita persiapkan menggunakan Python.
Asumsi dalam Crawler ini bahwa teks yang akan diambil mempunyai Class yang sama. Bila pada Page yang lain, Classnya berbeda , maka pada Script Crawler ditambahkan lagi dengan Class yang baru.



# Membuat tools Crawler menggunakan Python
Crawler tools menggunakan pemrograman Python, dimana banyak library yang siap digunakan untuk kebutuhan Crawler. 
Adapun Script Python yang digunakan dalam penelitian ini mengkustom dari Script open source dari Github, yang kemudian dimodifikasi sesuai kebutuhan
Crawler untuk domain Zakat.
Untuk masing - masing website memiliki masing - masing Script Python, karena masing - masing web mempunyai struktur Class yang berbeda - beda.
Untuk Script Python yang digunakan, bisa dilihat pada File :
- zakat_alazhar.py
- zakat_dd.py
- zakat_dir.py
- zakat_rumah.py

# Implementasi tools Crawler
Pada tahap implementasi, Peneliti menjalankan Script Python menggunakan PyCharm, selanjutnya menjalankan Script tersebut dan mengembalikan data 
yang berhasil diCrawler dalam bentuk json.

Secara keseluruha proses Crawling dapat dilihat pada gambar berikut : crawler.png
