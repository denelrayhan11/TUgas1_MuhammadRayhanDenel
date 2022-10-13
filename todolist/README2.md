# Muhammad Rayhan Denel
# 2106752161
# link heroku
https://tokosipedi.herokuapp.com/todolist/login

# Penjelasan Tugas 6
## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

Jawab:

Perbedaan utama antara asyncrhonus programming dengan synchronus programming terletak pada metodenya.

Asychronus programming berarti program dapat menjalankan beberapa task / tugas secara bersamaan. Ketika sebuah function asyncrhonus dipanggil, baris code selanjutnya tetap dapat dijalankan tanpa perlu menunggu function tersebut selesai dijalankan (concurrent).
Synchronus programming berarti program menjalankan tugas / task secara berurutan. Ketika sebuah task/function dijalankan, instruksi untuk menjalankan task lainnya diblokir. Sedemikian sehingga harus menunggu task/function tersebut selesai terlebih dahulu baru bisa menjalankan task/function berikutnya (sequential).

# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini

Jawab:

paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya. penerapan pada tugas ini yaitu saat pengguna melakukan perintah dengan mengklik tambah task baru, maka pop up task baru langsung keluar saat di klik/saat terjadi event.

# Jelaskan penerapan asynchronous programming pada AJAX

Jawab:

Pada Javascript, Asynchronous JavaScript and XMLHTTP atau biasa disebut AJAX merupakan salah satu konsep yang menerapkan metode asynchronous dalam menjalankan pekerjaannya. Biasa nya AJAX digunakan untuk melakukan permintaan data (request) dan menangani sebuah tanggapan (handling response), baik response dalam bentuk XML, Javascript ataupun JSON dari sebuah Rest API.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

Jawab:

AJAX GET

- Menambahkan 2 function yaitu todolist_ajax dan get_todolist_json pada views.py yang berfungsi untuk mengambil data task dalam bentuk JSON yang sesuai dengan user yang login saat itu. Function tersebut akan merev Selanjutnya menambahkan routing path pada urls.py agar views dapat terhubung. Ketika website berhasil di load, AJAX GET akan otomatis terpanggil dan mendapatkan task dalma bentuk JSON kemudian memasukkannya ke dalam masing-masing cards.

AJAX POST

- Membuat button add task yang sebelumnya redirect ke todolist/create_task, berubah menjadi memunculkan modal. Dalam implementasinya, menambahkan function add pada views.py dan routing pada urls.py agar dapat terhubung. Pada function ini diterapkan pula asynchronus programming sedemikian sehingga task yang ditambahkan akan otomatis terupdate tanpa perlu melakukan relaod pada website.