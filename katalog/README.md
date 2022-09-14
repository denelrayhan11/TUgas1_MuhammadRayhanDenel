Nama    : Muhammad Rayhan Denel
NPM     : 2106752161
Matkul  : PBP-E

link    : http://tokosipedi.herokuapp.com/katalog/

![Gambar]('../../punya%20denel.png?raw=true')
## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Menggunakan virtual environment agar mengisolasi hasil install kedalam virtual environment bukan ke dalam lokal komputer. dan untuk mengupdate pada web tersebut juga bisa mengunakan virtual environment.
jika tidak menggunakan virtual environment maka hasil install akan disimpan di dalam lokal komputer. namun tetap bisa tetap dibuat. dan untuk mengupdate akan terjadi ketidak sinkronan

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

poin 1 = views.py yaitu mengambil semua data-data yang terdapat pada data base dan dengan menambahkan variabel data penting seperti nama dengan npm, dan variabel tersebut akan disimpan kedalam scope context yang selanjutnya akan dibawa kedalam fungsi render sebagai parameter tambahan.
poin 2 = urls.py pada urls.py saya menambahkan kode path ('katalog/', include('katalog.urls')) yang diletakkan pada file urls.py yang terletak pada folder project_django. hal tersebut dibuat agar mmemberikan route ke '/katalog' dengan katalog/urls.py agar function dapat dijalankan show_katalog yang katalog.views.py
poin 3 = katalog.html untuk mengimplementasikan. program akan menjalankan atau menampilkan di katalog.html lalu saya menambahkan variabel yang telah saya buat yaitu nama dan npm dengan variabel "{{nama}}" dan "{{npm}}".
poin 4 = deploy yaitu untuk mendeploy web yang telah saya buat. saya menghubungkan antara repositori yang terdapat pada github dengan web heroku. dengan cara memasukkan variabel HEROKU_APP_NAME dan HEROKU_API_KEY di github secrets