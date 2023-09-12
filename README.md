## Link adaptable ##
    https://stock-master.adaptable.app/
## 1.Cara membuat sebuah proyek Django baru yaitu ##
    Langkah 1: Membuat Direktori dan Mengaktifkan Virtual Environment
    # Buat direktori baru dan masuk ke dalamnya
    mkdir StockMaster
    cd StockMaster

    # Buat virtual environment dan aktifkan
    python -m venv env
    source env/bin/activate (di Unix/Mac)
    env\Scripts\activate (di Windows)

    Langkah 2: Menyiapkan Dependencies dan Membuat Proyek Django
    # Pasang dependencies
    pip install django gunicorn whitenoise psycopg2-binary requests urllib3

    # Buat proyek Django
    django-admin startproject StockMaster .

    # Tambahkan ALLOWED_HOSTS di settings.py

    Langkah 3: Menjalankan Server
    # Jalankan server Django
    python manage.py runserver

    Langkah 4: Menghentikan Server dan Menonaktifkan Virtual Environment
    # Untuk menghentikan server, tekan Ctrl+C
    # Nonaktifkan virtual environment
    deactivate

    Langkah 5: Mengunggah Proyek ke Repositori GitHub
    # Inisiasi direktori sebagai repositori Git
    git init

    # Tambahkan semua berkas ke repositori
    git add .

    # Buat berkas .gitignore
    # Isi .gitignore dengan aturan yang diperlukan

    # Lakukan commit awal
    git commit -m "Inisialisasi proyek Django"

    # Tambahkan repositori GitHub sebagai remote
    git remote add origin <URL repositori GitHub Anda>

    # Push proyek ke GitHub
    git push -u origin main

## 2.Membuat aplikasi dengan nama main pada proyek tersebut. ##
    Langkah 1: Buat Aplikasi Main
    # Membuat aplikasi baru bernama "main"
    python manage.py startapp main

    Langkah 2: Mendaftarkan Aplikasi ke dalam Proyek
    Buka berkas settings.py yang terletak di dalam direktori proyek "shopping_list" Anda. Temukan variabel INSTALLED_APPS dan tambahkan nama aplikasi "main" ke dalam daftar aplikasi yang ada.
    INSTALLED_APPS = [
        # ...
        'main',
        # ...
    ]

## 3.Melakukan routing pada proyek agar dapat menjalankan aplikasi main. ##
    Langkah 1: Buka berkas urls.py dalam direktori proyek "shopping_list" (bukan yang ada di dalam aplikasi "main").

    Langkah 2: Impor fungsi include dari django.urls.
    from django.urls import path, include

    Langkah 3: Tambahkan rute URL berikut ke dalam variabel urlpatterns untuk mengarahkan ke tampilan "main" yang akan didefinisikan dalam berkas urls.py aplikasi "main".
    urlpatterns = [
        # ...
        path('main/', include('main.urls')),
        # ...
    ]

    Langkah 4: Jalankan proyek Django dengan perintah:
    python manage.py runserver

    Langkah 5: Buka http://localhost:8000/main/ di peramban web Anda untuk melihat halaman yang sudah Anda buat.

## 4.Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib ##
    Langkah 1: Mengubah Berkas models.py dalam Aplikasi "main"

    Buka berkas models.py dalam direktori aplikasi "main".
    Tambahkan atau ubah model Anda seperti yang diinginkan. Misalnya:
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        date_added = models.DateField(auto_now_add=True)
        price = models.IntegerField()
        description = models.TextField()
        amount = models.IntegerField()

    Langkah 2: Membuat dan Mengaplikasikan Migrasi Model

    Untuk membuat migrasi model, jalankan perintah:
    python manage.py makemigrations

    Untuk menerapkan migrasi ke basis data lokal, jalankan perintah:
    python manage.py migrate

## 5.Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas ##
    Langkah 1: Mengintegrasikan Komponen MVT
    Buka berkas views.py dalam direktori aplikasi "main".
    Impor modul yang diperlukan dengan menambahkan baris berikut di bagian atas berkas:
    from django.shortcuts import render

    Tambahkan fungsi show_main di bawah impor:
    def show_main(request):
        context = {
            'name': 'Joseph Bintang Ardhirespati',
            'class': 'PBP D'
        }
        return render(request, "main.html", context)

## 6.Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. ##
    Langkah 1: Mengonfigurasi Routing URL Aplikasi "main"

    Buat berkas urls.py dalam direktori "main" jika belum ada.
    Isi berkas urls.py dengan kode berikut:
    from django.urls import path
    from .views import show_main

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]

    Penjelasan Kode dalam urls.py pada Aplikasi "main":

    Berkas urls.py pada aplikasi "main" bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi "main".
    Impor path dari django.urls untuk mendefinisikan pola URL.
    Gunakan fungsi show_main dari modul .views (karena kita berada dalam direktori yang sama) sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
    Nama app_name dapat ditambahkan jika Anda ingin memberikan nama unik pada pola URL dalam aplikasi, tetapi dalam kasus ini, kami tidak menggunakannya.

## 7.Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. ##
    1.Buatlah akun Adaptable.io menggunakan akun GitHub yang digunakan untuk membuat proyek shopping_list.
    2.Jika sudah login, silakan tekan tombol New App. Pilih Connect an Existing Repository.
    3.Hubungkan Adaptable.io dengan GitHub dan pilih All Repositories pada proses instalasi.
    4.Pilihlah repositori proyek shopping_list sebagai basis aplikasi yang akan di-deploy. Pilih branch yang ingin dijadikan sebagai deployment branch.
    5.Pilihlah Python App Template sebagai template deployment.
    6.Pilih PostgreSQL sebagai tipe basis data yang akan digunakan.
    7.Sesuaikan versi Python dengan spesifikasi aplikasimu. Untuk mengeceknya, nyalakan virtual environment dan jalankan perintah python --version.
    8.Pada bagian Start Command masukkan perintah python manage.py migrate && gunicorn shopping_list.wsgi.
    9.Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu.
    10.Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.

## 8.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. ##
![Alt text](fota/fotoo.png)

    # Request dari Klien ke Aplikasi Django:
    Klien (pengguna web) mengirim permintaan HTTP ke aplikasi Django melalui peramban web mereka.
    Permintaan ini biasanya berupa URL yang diketikkan oleh pengguna atau tindakan yang dilakukan di dalam aplikasi, seperti mengklik tautan atau mengirim formulir.
    # urls.py (Routing URL):
    Ketika permintaan tiba di server Django, berkas urls.py digunakan untuk mencocokkan URL yang diterima dengan pola URL yang telah didefinisikan di dalamnya.
    Pola URL digunakan untuk menentukan tindakan selanjutnya, yaitu fungsi tampilan mana yang harus menangani permintaan tersebut.
    # views.py (Fungsi Tampilan):
    Setelah pola URL cocok dengan URL yang diterima, fungsi tampilan yang sesuai di dalam berkas views.py akan dipanggil.
    Fungsi tampilan ini mengambil permintaan HTTP sebagai argumen dan dapat berinteraksi dengan model untuk mengambil atau memanipulasi data yang diperlukan.
    Fungsi tampilan kemudian mempersiapkan data yang akan ditampilkan di halaman web.
    # models.py (Model Basis Data):
    Fungsi tampilan dapat berinteraksi dengan model yang didefinisikan di dalam berkas models.py untuk mengakses atau memodifikasi data dalam basis data.
    Model ini mencerminkan struktur data dalam basis data dan memungkinkan penggunaan ORM (Object-Relational Mapping) untuk berinteraksi dengan basis data tanpa menulis SQL secara langsung.
    # Berkas HTML (Tampilan):
    Data yang telah dipersiapkan oleh fungsi tampilan akan diteruskan ke berkas HTML yang sesuai untuk merender halaman web.
    Berkas HTML mengandung kode HTML, serta template tag Django yang digunakan untuk mengambil dan menampilkan data yang diterima dari fungsi tampilan.
    Hasil akhirnya adalah halaman web yang dihasilkan yang siap untuk dikirimkan kembali ke klien.
    # Respon Kepada Klien:
    Setelah berkas HTML merender halaman, respon HTTP yang berisi halaman tersebut dikirimkan kembali kepada klien melalui jaringan.
    Klien akan menerima respon ini dan akan melihat halaman web yang telah dihasilkan oleh aplikasi Django.

## 9.mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? ##
    # Isolasi Proyek: Virtual environment memungkinkan Anda membuat lingkungan kerja terisolasi untuk setiap proyek Python yang Anda kerjakan. Ini berarti bahwa semua dependensi proyek, termasuk versi spesifik dari pustaka dan paket Python, diisolasi dari proyek-proyek lain yang ada di komputer Anda. Dengan begitu, Anda dapat menghindari konflik antara versi pustaka dan mengisolasi setiap proyek dengan baik.
    # Menghindari Konflik Dependensi: Saat Anda bekerja pada berbagai proyek Python, beberapa proyek mungkin memerlukan versi pustaka yang berbeda. Virtual environment memungkinkan Anda untuk menginstal versi pustaka yang berbeda dalam setiap lingkungan proyek tanpa konflik.
    # Memudahkan Pemeliharaan: Dengan menggunakan virtual environment, Anda dapat mengelola dependensi proyek dengan lebih baik. Anda dapat membuat daftar dependensi (biasanya disimpan dalam berkas requirements.txt) yang mencantumkan semua pustaka yang dibutuhkan untuk proyek Anda. Ini mempermudah pemasangan ulang dependensi proyek di lingkungan lain atau bagi rekan pengembang yang bekerja pada proyek yang sama.
    # Keamanan: Virtual environment membantu menghindari perubahan tidak disengaja atau terlalu banyak akses ke sistem inti. Ini berarti jika ada kesalahan dalam proyek atau jika ada modifikasi yang tidak diinginkan, dampaknya akan dibatasi pada lingkungan virtual dan tidak akan memengaruhi instalasi Python sistem Anda.

    # Iya, Anda masih bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi sangat disarankan untuk menggunakan virtual environment.

## 10.Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. ##
    MVC, MVT, dan MVVM adalah tiga pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi untuk mengatur cara data, logika, dan tampilan diatur dan berinteraksi. Meskipun semuanya berbagi tujuan umum untuk memisahkan komponen-komponen utama aplikasi, mereka memiliki filosofi dan pengaturan yang berbeda. Berikut adalah penjelasan singkat tentang masing-masing dari mereka dan perbedaan antara ketiganya:

    # MVC (Model-View-Controller):
    -Model: Model merepresentasikan data dan bisnis logic aplikasi. Ini bertanggung jawab untuk mengelola, memproses, dan menyimpan data. Model tidak harus tahu tentang tampilan atau penggunaan akhir dari data ini.
    -View: View mengatur tampilan yang diberikan kepada pengguna. Ini bertanggung jawab untuk menampilkan data dari Model dalam format yang sesuai untuk tampilan. View tidak boleh memiliki logika bisnis.
    -Controller: Controller bertindak sebagai perantara antara Model dan View. Ini menerima input dari pengguna, memprosesnya, dan mengarahkan tindakan apa yang harus diambil berdasarkan input tersebut. Controller juga mengupdate Model atau View sesuai kebutuhan.
    -Perbedaan Utama: MVC adalah pola arsitektur yang sering digunakan dalam pengembangan aplikasi web tradisional, di mana View bertindak sebagai tampilan HTML yang disajikan kepada pengguna. Controller mengelola logika aplikasi dan menghubungkan Model dengan View. Model, View, dan Controller adalah tiga komponen utama yang terpisah secara tegas.

    # MVT (Model-View-Template):
    -Model: Model dalam MVT mirip dengan Model dalam MVC. Ini merepresentasikan data dan bisnis logic aplikasi. Model tidak tahu tentang tampilan.
    -View: View dalam MVT bertanggung jawab untuk mengatur tampilan, sama seperti dalam MVC. Namun, dalam konteks Django (sebuah kerangka kerja Python), View mengambil peran yang lebih besar daripada dalam MVC. View dalam Django adalah komponen yang mengelola logika aplikasi dan menentukan bagaimana data yang diterima dari Model akan ditampilkan dalam Template.
    -Template: Template dalam MVT adalah komponen yang memungkinkan Anda untuk mengatur tampilan HTML secara terpisah dari kode Python dalam View. Template adalah yang menentukan bagaimana data dari View akan ditampilkan kepada pengguna.
    -Perbedaan Utama: MVT adalah varian dari MVC yang digunakan dalam Django. Perbedaan utama adalah peran yang lebih kuat yang dimiliki oleh Template dalam Django untuk mengatur tampilan HTML.

    # MVVM (Model-View-ViewModel):
    -Model: Model dalam MVVM adalah komponen yang sama dengan dalam MVC dan MVT. Ini bertanggung jawab untuk data dan bisnis logic aplikasi.
    -View: View dalam MVVM mirip dengan View dalam MVC dan MVT. Ini bertanggung jawab untuk mengatur tampilan dan menampilkan data kepada pengguna.
    -ViewModel: ViewModel adalah komponen yang unik untuk MVVM. Ini berperan sebagai perantara antara Model dan View. ViewModel mengubah data dari Model ke format yang lebih cocok untuk tampilan dan menyediakannya ke View. ViewModel juga mengelola tindakan dan peristiwa yang terjadi di View.
    -Perbedaan Utama: MVVM adalah pola arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis klien (seperti aplikasi web berbasis JavaScript atau aplikasi seluler). ViewModel adalah komponen yang memungkinkan pengikatan data dua arah antara Model dan View. Ini membantu memisahkan logika aplikasi dari tampilan, mirip dengan MVC dan MVT, tetapi dengan pendekatan yang lebih berfokus pada tampilan responsif.