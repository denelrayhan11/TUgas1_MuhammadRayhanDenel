# Muhammad Rayhan Denel
# 2106752161

# Penjelasan Tugas 6
## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

Jawab:

Perbedaan utama antara asyncrhonus programming dengan synchronus programming terletak pada metodenya.

Asychronus programming berarti program dapat menjalankan beberapa task / tugas secara bersamaan. Ketika sebuah function asyncrhonus dipanggil, baris code selanjutnya tetap dapat dijalankan tanpa perlu menunggu function tersebut selesai dijalankan (concurrent).
Synchronus programming berarti program menjalankan tugas / task secara berurutan. Ketika sebuah task/function dijalankan, instruksi untuk menjalankan task lainnya diblokir. Sedemikian sehingga harus menunggu task/function tersebut selesai terlebih dahulu baru bisa menjalankan task/function berikutnya (sequential).

# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini

Jawab:

Paradigma Event-Driven Programming merupakan suatu momen dimana program dieksekusi berdasarkan event yang terjadi. Paradigma ini sangat bergantung pada event, sehingga flow dari program dapat dijalankan seperti konsep asynchronus programming yang tidak sequential. Salah satu contoh penerapannya pada tugas kali ini adalah ketika button add pada add task diklik, program akan selalu menjalankan suatu fungsi untuk membuat task baru ketika terdapat event yaitu click document.getElementById("addtaskbutton").onclick = addTodolistModal

# Jelaskan penerapan asynchronous programming pada AJAX

Jawab:

Penerapan asynchronus programming pada AJAX contohnya ketika sebuah event terjadi maka event tersebut akan menjalankan suatu fungsionalitas AJAX. Pada tugas 6 ini, penerapannya terjadi ketika user melakukan klik button add pada form untuk membuat task baru, makan AJAX POST akan dilakukan dan mengirim data ke server. Kemudian, setelah server berhasil mengolah data tersebut, callback function akan dijalankan sehingga dapat menangkap data dan mengirimkannya ke server tanpa harus melakukan reload pada website. Hal tersebut tentu akan membuat user experience dari website jauh lebih baik.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

Jawab:

AJAX GET

- Menambahkan 2 function yaitu todolist_ajax dan get_todolist_json pada views.py yang berfungsi untuk mengambil data task dalam bentuk JSON yang sesuai dengan user yang login saat itu. Function tersebut akan merev Selanjutnya menambahkan routing path pada urls.py agar views dapat terhubung. Ketika website berhasil di load, AJAX GET akan otomatis terpanggil dan mendapatkan task dalma bentuk JSON kemudian memasukkannya ke dalam masing-masing cards.

AJAX POST

- Membuat button add task yang sebelumnya redirect ke todolist/create_task, berubah menjadi memunculkan modal. Dalam implementasinya, menambahkan function add pada views.py dan routing pada urls.py agar dapat terhubung. Pada function ini diterapkan pula asynchronus programming sedemikian sehingga task yang ditambahkan akan otomatis terupdate tanpa perlu melakukan relaod pada website.