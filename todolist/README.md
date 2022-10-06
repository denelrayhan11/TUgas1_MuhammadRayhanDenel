# Nama    : Muhammad Rayhan Denel
##  NPM     : 2106752161
##  Tugas-4 PBP

## 1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
### Penjelasan
CSRF merupakan singkatan dari Cross Site Request Forgery, dan dikatakan terjadi ketika situs Web jahat menipu pengguna untuk secara tidak sengaja dan tanpa sadar memuat URL dari situs yang sebelumnya telah diautentikasi, sehingga mengeksploitasi status mereka dan juga menempatkan data dalam risiko. Terdapat dua kemungkinan yang terjadi yaitu yang pertama adalah jika tidak menggunakan CSRF token namun form dapat dibuat dan dapat digunakan, maka data yang diisi pada form tersebut rentan tergadap situs web jahat dan menjadi tidak aman, kemungkinan yang kedua adalah jika tidak menggunakan CSRF token maka form yang dibuat tidak dapat digunakan dan tidak dapat di muat di web tersebut.

## 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
### Penjelasan
Kita dapat membuat form secara manual tanpa menggunakan form.as_table dengan beberapa langkah yaitu seperti membuat table pada html yang ingin ada formnya, lalu membuat beberapa hal yang dibutuhkan pada form tersebut dengan cara membuat dulu judul untuk data yang dibutuhkan, selanjutnya membuat tipe data yang dibutuhkan pada form tersebut, jika kita menginginkan sebuah teks untuk dimasukkan, maka kita bisa menginisiasi type menjadi text, dengan nama sesuai, lalu kita dapat meletakkan watermark pada textfield tersebut dengan menggunakan placeholder dan menempatkan sesuai dengan class form-control, jika pada form kita menginginkan suatu tombol maka kita bisa menginisiasi class button, lalu memilih typenya, dan memilih aksi yang dilakukan pada tombol tersebut.

## 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
### Penjelasan
tahap pertama yaitu menampilkan form secara default saat pertama kali diminta oleh user, pada form tersebut biasanya berisi laman kosong, dan jika user menginput data baru pada form tersebut atau mengubah nilai yang sudah ada pada form tersebut. Formulir ini disebut sebagai tidak terikat pada saat ini, karena tidak terkait dengan data yang dimasukkan pengguna (meskipun mungkin memiliki nilai awal). Tahap selanjutnya menerima data dari user dan mengikatnya pada form. Selanjutnya data akan dibersihkan dan memvalidasi data tersbut. Selanjutnya Jika ada data yang tidak valid, tampilkan kembali formulir, kali ini dengan nilai yang diisi pengguna dan pesan kesalahan untuk bidang masalah. Namun ika semua data valid, lakukan tindakan yang diperlukan (seperti menyimpan data, mengirim email, mengembalikan hasil penelusuran, mengunggah file, dan sebagainya). Terakhir mengarahkan pengguna ke halaman lain.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
### Penjelasan
Hal yang pertama dilakukan yaitu membuat app baru pada cmd yaitu todolist, lalu mendaftarkannya pada settings.py yang ada pada project django. Selanjutnya membuat models yang dibutuhkan pada aplikasi todolist yang nantinya akan ditampilkan pada views. Models juga membutuhkan field field yang sesuai. Selanjutnya pada views membuat fungsi-fungsi yang dibutuhkan, pada tugas ini memiliki fungsi untuk register, login, logout, dan mengisi data task. Pada fungsi register yaitu memuat sebuah form untuk user membuat dan mendaftarkan akun yang baru dibuat. Pada fungsi login memuat sebuah form yang terhubung dengan form register sehingga untuk menginput data pada form harus bersesuaian dengan data yang terdapat pada form register. Pada fungsi logout akan mengeluarkan data akun yang telah login. dan pada fungsi Create-task akan membuat sebuah form yang berfungsi untuk meminta data dari pengguna sebagai form database yang ada pada web tersebut. terdapat juga fungsi show todolist yaitu fungsi yang menampilkan data yang terdapat pada database setelah diisi pada create-task. pada sebelum create task dan show todolist dibutuhkan login reuired yaitu agar pengguna diminta untuk selalu login sebelum mengakses semua data yang ada pada web tersebut. Pada setiap fungsi tersebut akan mengarahkan ke halaman sesuai dengan fungsinya. Pada urls semuanya disesuaikan dengan urlnya dan halaman yang diarahkannya. Membuat semua halaman html sesuai yang dibutuhkan, create-task.html, login.html, register.html, todolist.html. Semua html tersebut menjadi wadah untuk semua form yang ada pada views.py.

## akun herroku 1 : uname : CSUI2021, password : bakung2021
## akun herroku 2 : uname : BAKUNG2021, password : CSUI2021

# Penjelasan Tugas 5
## 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Untuk Inline CSS karena dia menggunakan atribut <style> agar memberikan sebuah style kepada tag HTML tertentu, kekurangannya adalah jika ingin memberikan perubahan yang merata atau besar, maka inline CSS harus diterapkan pada setiap elemen yang ingin diubah. Namun kelebihannya, karena perubahan yang terjadi hanya di element tertentu, maka dapat digunakan untuk menguji atau melihat perubahan, berguna untuk perbaikan cepat, dan ukuran request HTTPnya lebih kecil.
Untuk internal CSS, biasa diletakkan di bagian <head> pada sebuah halaman HTML. Ini merupakan better practice dari inline CSS karena dapat merubah sekelompok element sekaligus, berbeda dengan inline yang harus diterapkan pada setiap element masing-masing. Opsi ini ideal untuk web yang hanya mempunyai 1 halaman HTML karena perubahan hanya terjadi di 1 halaman. Namun kekurangannya jika web mempunyai beberapa halaman dan kita ingin membuat perubahan pada semua halaman, maka kurang efisien karena jika kita ingin memakai CSS yang sama, maka perlu meng-upload file terlebih dahulu pada setiap halaman.
Untuk external CSS, opsi ini dikenal menjadi opsi yang paling nyaman untuk digunakan. Sama seperti internal, biasa diletakkan di bagian <head> halaman. Kelebihan dari external CSS adalah file CSS yang sama dapat digunakan di halaman-halaman lain, setelah itu kecepatan loading juga lebih cepat, dan ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapih. kekurangannya mungkin cukup sedikit dibandingkan yang lain, salah satunya adalah halaman belum tampil secaraa sempurna hingga file CSS selesai dipanggil.

## 2. Jelaskan tag HTML5 yang kamu ketahui.
terdapat <font> untuk menentukan font, warna, dan ukuran dari sebuah text. Ada <div> untuk membuat bagian-bagian pada halaman. <h1>-<h6> untuk mendefinisikan sebuah header dengan ukuran dari besar sampai kecil. <link>

## 3. Jelaskan tag HTML5 yang kamu ketahui.
class yang akan memilih class element yang akan memilih element

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
class yang akan memilih class element yang akan memilih element

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Saya menggunakan fitur-fitur bootstrap untuk membuat aplikasi saya, seperti cards, button, dan warna-warnanya. Dan juga style css