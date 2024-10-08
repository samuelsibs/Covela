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


# TUGAS 4 - README

# 1) Apa perbedaan antara HttpResponseRedirect() dan redirect()?
HttpResponseRedirect() hanya menerima URL secara manual untuk redirect, sedangkan redirect() lebih fleksibel karena bisa menerima URL, nama view, atau objek model, sehingga lebih mudah digunakan

# 2) Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model Product dengan User di Django dilakukan dengan menggunakan field ForeignKey pada model Product, yang mengacu pada model User dari “django.contrib.auth.models”. Hal ini menciptakan relasi antara produk dan pengguna, di mana setiap produk akan terasosiasi dengan satu pengguna, sedangkan satu pengguna bisa memiliki banyak produk. Dalam implementasinya, ketika pengguna yang sedang login membuat produk baru, field user pada Product diisi dengan request.user, yang mewakili pengguna yang sedang terotorisasi. Untuk menyimpan produk, Django menggunakan 'commit=False' saat menyimpan form agar dapat mengisi field user terlebih dahulu sebelum menyimpan data ke database. Selain itu, ketika menampilkan produk, kita dapat memfilter produk berdasarkan user yang sedang login dengan memanfaatkan query 'Product.objects.filter(user=request.user)'. Dengan cara ini, setiap pengguna hanya akan melihat produk yang mereka buat, memastikan bahwa data yang ditampilkan sesuai dengan kepemilikan pengguna yang sedang terotentikasi.

# 3) Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses untuk memverifikasi identitas pengguna, biasanya melalui pemeriksaan kredensial seperti username dan password. Contohnya, saat pengguna login ke aplikasi, sistem melakukan authentication untuk memastikan bahwa informasi yang dimasukkan benar. Sedangkan Authorization adalah proses yang menentukan hak akses pengguna setelah mereka berhasil diautentikasi, menentukan apa yang dapat dilakukan pengguna dalam sistem, seperti mengakses halaman tertentu atau mengedit data. Dalam implementasinya di Django, saat pengguna login, sistem menggunakan metode “authenticate()” untuk memverifikasi kredensial, dan jika valid, pengguna tersebut akan diautentikasi menggunakan fungsi “login()”. Setelah itu, akses pengguna dapat dibatasi dengan menggunakan decorator seperti “@login_required”, memastikan bahwa hanya pengguna yang terautentikasi yang dapat mengakses view tertentu. 

# 4) Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan session dan cookies. Ketika pengguna berhasil login, Django membuat session yang menyimpan informasi seperti ID pengguna, dan mengaitkannya dengan cookie di browser pengguna yang berisi ID session. Ini memungkinkan pengguna untuk tetap login tanpa harus mengisi kredensial setiap kali mereka mengakses aplikasi. Selain itu, cookies juga digunakan untuk menyimpan preferensi pengguna, melacak aktivitas, dan Cookies juga bisa digunakan untuk analitik, membantu pengembang memahami perilaku pengguna di situs mereka. Namun, tidak semua cookies aman digunakan. Cookies dapat menjadi target serangan seperti pencurian session (session hijacking) atau serangan cross-site scripting (XSS). 

# STEP BY STEP !!!
- Mengimport UserCreationForm dan messages pada berkas views.py 
- Menambahkan fungsi register ke dalam views.py yang fungsinya untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di submit dari form
- Membuat berkas HTML baru dengan nama “register.html”  dan mengimplementasi kode yang dibutuhkan.
- import fungsi register yang telah dibuat kedalam urls.py serta tambahkan pathnya ke variable urlpatterns
- Pada views.py, telah ditambahkan import authenticate,login dan AuthenticationForm yang digunakan untuk melakukan autentikasi dan login
- Mengimplementasikan fungsi login_user ke views.py yang mempunyai fungsi untuk mengautentikasi pengguna yang ingin login. Lalu, mengimport fungsinya kedalam berkas urls.py dan menambahkan pathnya di variable urlpatterns
- Membuat berkas HTML baru dengan nama “login.html” di direktori main/templates dan mengimplementasi kode yang dibutuhkan
- Untuk membuat fungsi Logout, kita mengimport “from django.contrib.auth import logout” ke dalam views.py
- Untuk melakukan mekanisme logout, kita menambahkan fungsi logout_user di berkas yang sama lalu mengimport fungsi tersebut kedalam urls.py dan menambahkan pathnya
- Menambahkan tombol Logout pada berkas main.html
- Untuk merestriksi akses halaman main, maka kita menambahkan import login_required pada views.py
- Diatas fungsi show_main, tambahkan @login_required(login_url='/login') agar halaman main hanya bisa diakses oleh pengguna yang sudah login.
- Agar bisa menggunakan data dari cookies, kita menambahkan import HttpResponseRedirect, reverse, dan datetime pada views.py
- Dalam fungsi login_user, kita akan menambahkan fitur yang menyimpan cookie bernama last_login, yang mencatat waktu terakhir pengguna melakukan login.
- Di fungsi show_main juga ditambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context. 
- Menyesuaikan fungsi logout_user agar ketika pengguna logout, data cookie dapat terhapus.
- Untuk menampilkan data sesi terakhir login pengguna, maka pada main.html kita menambahkan potongan kode “<h5>Sesi terakhir login: {{ last_login }}</h5>”
- Langkah terakhir yang dilakukan adalah menghubungkan model Product dengan User. Tambahkan potongan kode berikut “from django.contrib.auth.models import User” pada models.py
- Pada model Product yang telah dibuat, tambahkan variabel user untuk dapat menghubungkan satu Product entry dengan satu user.
- Mengubah kode pada fungsi create_product_entry yang ada di views.py, salah satunya dengan menambahkan parameter commit=False untuk mencegah Django menyimpan objek yang dibuat dari form langsung ke database. 
- Mengubah value dari “product_entries” dan menambahkan ‘name’ di variable context pada fungsi show_main.
- Dalam mempersiapkan aplikasi web untuk environment production maka kita menambahkan import os pada settings.py yang ada di subdirektori Covela, Kemudian ganti variabel DEBUG dari berkas settings.py
- Deploy ke PWS!!!
- Pada web Covela, klik register untuk menambahkan akun ( untuk ketentuan tugas maka perlu dibuat 2 akun). Selanjutnya tambahkan tiga Product pada web tersebut.
- SELESAII!!!!

# TUGAS 5 - README

# 1) Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS selector pada elemen HTML ditentukan oleh beberapa faktor. Prioritas tertinggi diberikan kepada inline styles yang ditulis langsung dalam elemen HTML menggunakan atribut style, sehingga akan mengesampingkan aturan CSS lainnya. Setelah itu, prioritas ditentukan oleh spesifisitas selector, dengan urutan spesifisitas tertinggi adalah selector ID (#id), diikuti oleh class selector, pseudo-class, dan attribute selector (.class, :hover, [type="text"]), kemudian tag/type selector dan pseudo-element (div, p, ::before). Jika beberapa selector memiliki tingkat spesifisitas yang sama, maka urutan deklarasi akan menentukan prioritasnya, di mana aturan yang ditulis terakhir dalam CSS akan diterapkan. Terakhir, deklarasi dengan !important akan mengesampingkan semua aturan lainnya, termasuk inline styles, ID, dan selector lainnya. 

# 2) Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design menjadi penting karena memungkinkan tampilan dan pengalaman pengguna yang konsisten dan optimal di berbagai perangkat dengan ukuran layar yang berbeda, seperti smartphone, tablet, dan desktop. 
Contoh aplikasi yang telah menerapkan responsive design adalah Shopee. Antarmuka Shopee dapat menyesuaikan dengan baik pada perangkat apapun, sehingga pengguna dapat menikmati pengalaman yang lancar di layar apapun.
Untuk contoh yang belum menerapkan responsive design adalah Pacil Web Service, karena hanya dirancang untuk tampilan laptop dan belum dapat menyesuaikan pada tampilan mobile.

# 3) Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin adalah ruang kosong di luar border yang memisahkan elemen dari elemen lainnya; contohnya, margin: 20px artinya menambahkan jarak 20px di semua sisi elemen. 
- Border adalah garis pembatas yang mengelilingi elemen dan padding, yang bisa diatur ketebalan, warna, dan jenis garisnya, seperti border: 2px solid black. 
- Padding adalah ruang di dalam border yang memisahkan konten dari border elemen; contohnya, padding: 15px artinya menambahkan ruang 15px di dalam elemen. 

#  4) Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox (Flexible Box Layout) dirancang untuk tata letak satu dimensi, yaitu mengatur elemen dalam satu baris atau kolom, dan memberikan fleksibilitas untuk menyesuaikan ukuran serta posisi item dalam container, berguna untuk membuat tata letak seperti navbar, footer, atau card alignment. 
Sedangkan,Grid Layout adalah metode tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom, menawarkan kontrol lebih atas tata letak yang kompleks seperti halaman web yang memiliki header, sidebar, dan konten utama yang terstruktur. Keduanya digunakan untuk membuat desain yang responsif dan rapi, namun flexbox lebih cocok untuk tata letak linier, sedangkan grid lebih kuat untuk tata letak yang memiliki struktur dua dimensi.

# STEP BY STEP !
- Untuk membuat fitur edit product, kita menambahkan fungsi baru bernama “edit_product” pada views.py. Lalu, mengimpor dan menambahkan path urlnya ke urls.py
- Membuat berkas HTML baru yang bernama “edit_products.html” di subdirektori main/templates dan mengimplementasi kode yang dibutuhkan
- Membuat tombol edit pada “main.html” yang terhubung oleh fungsi edit_products sehingga pengguna bisa mengedit input product mereka
- Untuk membuat fitur hapus product, kita menambahkan fungsi baru bernama “delete_product” pada views.py.Pada fungsi ini, kita memanfaatkan method delete() untuk menghapus data produk. Lalu, mengimpor dan menambahkan path urlnya ke urls.py
- Membuat tombol hapus di main.html
- Untuk melakukan designnya, kita perlu menambahkan Tailwind ke aplikasinya dengan cara menambahkan script CDN tailwind dibagian head.
- Untuk menambahkan Navigation Bar,  kita perlu membuat HTML baru dengan nama “navbar.html” di folder templates yang di root directory. Implementasikan kodenya dengan design yang diinginkan. Kemudian, kita perlu menautkan navbarnya ke dalam main.html, create_mood_entry.html, dan edit_mood.html dengan menggunakan tags include
- Mengonfigurasi Static Files pada Aplikasi dengan menambahkan middleware WhiteNoise pada settings.py dan juga mengonfigurasikan variabel  STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL 
- Untuk menambahkan styles pada aplikasi, kita membuat direktori baru yaitu /static/css dan membuat file global.css didalamnya
- Menambahkan custom styling ke global.css
- Menghubungkan global.css dan script Tailwind ke base.html agar bisa digunakan dalam template Django.
- Styling halaman login,register, tambah produk, edit product dan home sesuai dengan design yang diinginkan
- Untuk styling data produknya, kita membuat file html baru bernama “card_products.html” di direktori main/templates dan implementasi design card produknya sesuai yang diinginkan. Buat juga 2 button untuk mengedit dan menghapus produknya di setiap card product.
- Untuk mengatur tampilan kalau tidak ada data produk yang diterima, maka dibuat gambar “x-button” sebagai simbol tidak ada data produk yang dapat ditampilkan. Gambar tersebut kita masukkan kedalam folder “image” yang terdapat di direktori static/image
- Gunakan card_info.html, card_products.html dan x-button.png ke template main.html.
