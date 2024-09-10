# 1.Pengimplementasian checklist secara step by step
  
  - Membuat direktori baru dengan nama “Covela” dan mengaktifkan virtual environment
  - Membuat proyek Django bernama “Covela” dengan perintah startproject
  - Membuat aplikasi baru dengan nama main dengan perintah startapp lalu mendaftarkan aplikasi main ke dalam proyek
  - Membuat direktori baru bernama templates didalam direktori aplikasi main
  - Membuat berkas baru bernama “main.html” untuk menunjukkan tampilan dasar HTML
  - Membuat model pada aplikasi main yang memiliki atribut name dengan tipe CharField, price dengan tipe IntegerField, description dengan tipe TextField dan quantity dengan tipe     IntegerField.
  - Membuat serta mengaplikasikan migrasi model dengan perintah makemigrations dan migrate
  - Menambahkan fungsi “show_main” yang berisi nama aplikasi, nama dan kelas saya untuk dikembalikan ke template HTML
  - Memodifikasi template “main.html” agar dapat menampilkan data yang telah diambil dari model
  - Mengonfigurasi Routing URL aplikasi main dengan membuat berkas urls.py didalam direktori main serta menambahkan kode yang diperlukan kedalam “urls.py”
  - Mengonfigurasi Routing URL Proyek dengan membuka file “urls.py” yang terletak di direktori proyek “Covela” lalu menambahkan rute URL untuk mengarahkan ke tampilan main
  - Melakukan deployment ke PWS



# 2.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan Tugas 2 PBP](https://github.com/user-attachments/assets/b5cbe845-b142-4fbd-a0e2-485146ca7a27)

"urls.py" berperan sebagai pemetaan URL. Setiap kali pengguna mengakses URL tertentu, Django mencocokkannya dengan pola URL yang terdaftar di sini, dan meneruskan request ke view yang sesuai. Lalu "views.py" bertindak sebagai penghubung antara URL dan data. View mengambil data dari models.py, memprosesnya, dan mengirimkan data tersebut ke template untuk dirender sebagai HTML. "models.py" berisi representasi objek dari data yang disimpan di database. Setiap model menggambarkan tabel dalam database, dan digunakan untuk mengambil atau menyimpan data yang akan ditampilkan di view. Kemudian, berkas HTML akan berfungsi untuk menampilkan data dalam bentuk yang dapat dibaca oleh pengguna. berkas ini menerima data dari views.py dan menyajikannya dalam HTML yang dapat diakses oleh pengguna melalui browser.



# 3.Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah control version system yang digunakan dalam pengembangan perangkat lunak untuk melacak perubahan kode, mendukung kolaborasi tim, dan mengelola versi proyek. Fungsinya meliputi pelacakan perubahan, pengelolaan cabang (branching), penyelesaian konflik, serta memungkinkan backup kode dan transparansi dalam pengembangan. 

# 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django dapat memberikan kemudahan bagi penggunanya karena memiliki dokumentasi yang lengkap dan jelas serta menyediakan struktur proyek yang rapi dan terorganisir. Meskipun mudah digunakan, Django sangatlah scalable.  Hal tersebut karena memungkinkan pengembang untuk memulai dengan proyek kecil dan kemudian berkembang menjadi proyek besar tanpa perlu berpindah ke framework-framework yang lainnya sehingga cocok untuk jangka panjang.

# 5.Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek Python dan tabel di database. Dengan ORM, pengembang dapat mengelola database menggunakan kode Python tanpa perlu menulis query SQL, sehingga memudahkan manipulasi data
