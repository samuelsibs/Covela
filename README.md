# COVELA 
# Link Project : http://samuel-sebastian-covela.pbp.cs.ui.ac.id/

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


# TUGAS 3 - README

# 1) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery sangat penting dalam pengimplementasian sebuah platform karena memungkinkan transfer informasi secara efisien dan real-time antara server dan pengguna. Dengan data delivery yang tepat, platform dapat memastikan bahwa pengguna menerima konten, pembaruan, atau informasi penting lainnya dengan cepat dan akurat. Hal ini tidak hanya meningkatkan pengalaman pengguna, tetapi juga membantu menjaga konsistensi dan integritas data di seluruh sistem. Selain itu, data delivery yang efisien dapat mengoptimalkan penggunaan sumber daya jaringan, memastikan keamanan data, serta memungkinkan platform untuk beradaptasi dengan perubahan kebutuhan pengguna dan kondisi pasar secara dinamis.

# 2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik daripada XML karena lebih ringan, mudah dibaca, dan diproses. JSON memiliki struktur yang lebih ringkas dan simpel dibandingkan XML.Selain itu, JSON secara alami mendukung tipe data yang umumnya digunakan dalam pemrograman seperti angka, string, array, dan objek, sehingga memudahkan integrasi dengan bahasa pemrograman modern.

JSON lebih populer dibandingkan XML karena formatnya yang lebih bersahabat dengan JavaScript dan banyak bahasa pemrograman lainnya, memungkinkan proses parsing dan serialisasi data menjadi lebih cepat dan efisien. JSON juga memiliki sintaks yang lebih sederhana, memudahkan developer untuk membuat, membaca, dan men-debug data. Oleh karena itu, dalam pengembangan aplikasi web dan API modern, JSON sering menjadi pilihan utama dibandingkan XML.

# 3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Dalam Django, method is_valid() digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan dan validasi yang telah ditentukan dalam model atau form tersebut. Ketika form diisi dan dikirimkan melalui request.POST, method ini akan menjalankan serangkaian pemeriksaan, seperti memverifikasi tipe data, memastikan field yang wajib diisi tidak kosong, dan memeriksa batasan lain yang telah didefinisikan dalam kode.

# 4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token itu adalah token yang berfungsi sebagai security yang sudah digenerate secara otomotis oleh Django. Kita membutuhkan csrf_token saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF. CSRF adalah jenis serangan di mana penyerang membuat pengguna yang telah terautentikasi di suatu situs web tanpa sadar melakukan tindakan yang tidak diinginkan, seperti mengubah data, membuat transaksi, atau mengirimkan formulir.
Jika kita tidak menambahkan csrf_token pada form, aplikasi akan rentan terhadap serangan CSRF. Penyerang bisa memanfaatkan kerentanan ini dengan membuat halaman web atau email berbahaya yang, jika dibuka oleh pengguna, secara otomatis akan mengirimkan permintaan ke situs target tanpa sepengetahuan atau persetujuan pengguna. Tanpa perlindungan csrf_token, aplikasi tidak dapat memverifikasi apakah permintaan tersebut berasal dari sumber yang sah, sehingga memungkinkan penyerang untuk mengeksploitasi sesi pengguna yang valid.

# 5) STEP BY STEP !
- Untuk membuat input form agar bisa menambahkan objek model pada app maka kita perlu membuat berkas baru di direktori main dengan nama “forms.py” untuk membuat struktur form yang dapat menerima data baru.
- Isilah kode yang diperlukan didalam “forms.py” tersebut. Saya membuat class bernama ProductForm yang menunjukkan model yang akan digunakan untuk form serta fields yang menunjukkan field dari model product yang akan digunakan untuk form.
- Buka berkas “views.py” yang di direktori main dan tambahkan import class tadi yang telah dibuat dalam “forms.py”. (Tambahkan juga import redirect)
- Dalam “views.py” juga, buat fungsi baru dengan nama create_product_entry yang menerima parameter request yang fungsinya untuk menghasilkan form yang dapat menambahkan data secara otomatis ketika data disubmit dari form.
- Import fungsi yang telah dibuat kedalam “urls.py” yang ada pada direktori main
- Masukkan path URL ke dalam variabel urlpatterns pada urls.py di folder main untuk dapat mengakses fungsi yang telah diimpor pada langkah sebelumnya.
- Buat berkas HTML baru bernama “create_product_entry.html” di direktori main/templates.
- Didalam “create_product_entry.html” itu diimplementasikan kode yang berfungsi untuk menampilkan halaman form yang memungkinkan pengguna menambahkan entri product baru. Form ini menggunakan template inheritance (extends), memiliki perlindungan CSRF, dan menyusun form dalam tabel untuk pengaturan tata letak yang rapi.
- Membuka “main.html” dan menambahkan beberapa kode didalam block content untuk menampilkan data product dalam bentuk tabel dan juga ada tombol “Add Product” yang akan mengarahkan ke halaman form
- Membuka views.py yang ada direktori main dan tambahkan import HttpResponse dan Serializer
- Membuat fungsi baru bernama “show_xml” yang menerima parameter request dan membuat sebuah variabel baru untuk menyimpan hasil query dari seluruh data yang ada pada class Product. Setelah itu,menambahkan return function berupa HttpResponse yang memuat parameter data dari query yang telah diserialisasi ke dalam format XML beserta parameter content_type="application/xml".
- Membuat fungsi baru bernama “show_json” yang menerima parameter request dan membuat sebuah variabel baru untuk menyimpan hasil query dari seluruh data yang ada pada class Product. Setelah itu, menambahkan return function berupa HttpResponse yang memuat parameter data dari query yang telah diserialisasi ke dalam format JSON beserta parameter content_type="application/json".
- Import kedua fungsi tersebut di “urls.py” yang ada di direktori main dan tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang udah diimpor tadi.
- Untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON, maka kita membuat fungsi baru bernama “show_xml_by_id” dan “show_json_by_id”. Setelah itu, buat variable yang bisa menyimpan hasil query dari data dengan id tertentu yang ada pada kelas Product dan tambahkan return function berupa HTTPResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML atau JSON dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON).
- Import fungsi yang telah dibuat ke “urls.py” dan tambahkan path URL ke dalam urlpatterns.
- git add,commit dan push lalu deploy ke pws!!!

### Mengakses 4 URL dengan Postman
![Screenshot (1365)](https://github.com/user-attachments/assets/a49a76da-2df0-4cb1-8b0e-f67834f1febb)

![Screenshot (1366)](https://github.com/user-attachments/assets/b29c7f17-984a-471c-8fa1-1f34a1b75842)

![Screenshot (1367)](https://github.com/user-attachments/assets/cfc58b24-1610-43d6-a338-7ea515f5dec3)

![Screenshot (1368)](https://github.com/user-attachments/assets/160c5dfd-5522-4f53-b4a7-257cf07f1b13)

