Link HTML = https://tokosipedi.herokuapp.com/mywatchlist/html/
Link JSON = https://tokosipedi.herokuapp.com/mywatchlist/json/
Link XML = https://tokosipedi.herokuapp.com/mywatchlist/xml/

### Jelaskan perbedaan antara JSON, XML, dan HTML!
 ## Json 
 sebuah singkatan dari JavScript Object Notation yaitu sebuah formatan yang digunakan untuk menyimpan, membaca serta menukar informasi dari web server yang akan dibaca atau berguna bagi pengguna dari web tersebut.
 ## XML
 Extensible Markup Language. XML akan menyimpan data dengan format teks yang sederhana sehingga data tersebut akan dimengerti oleh server yang menerima data tanpa perlu perubahan atau modifikasi apapun. XML juga merupakan sebuah bahasa dari pemrograman.
 ## HTML
 Hyper Text Markup Language adalah bahasa markup standar yang biasa digunakan untuk membuat suatu website
 ## perbedaannya
 Yang pertama adalah cara menyimpan elemen,  JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien.Nama dari file JSON akan diakhiri dengan ekstensi .json. Sementara file XML akan diakhiri dengan ekstensi .xml.Untuk penerapannya, JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. Sedangkan XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan. Untuk HTML bersifat case sensitive, berfungsi menampilkan data, tidak terdiri dari data struktural, bersifat statis, harus menggunakan tag tertentu.

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
dalam proses mengembangkan suatu platform kita harus mengirimkan data dari suatu wadah atau stack yang satu lalu dikirim ke stack yang lainnya. formatan pengiriman data tersebut bisa menggunakan xml, json, dan html

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
membuat atau meginisiasi suatu app di file kita dengan "python manage.py startapp 'nama app'" dengan command tersebut kita akan mendapatkan file file yang bisa digunakan untuk mengembangkan app kita dengan menghubungkan antar satu file dengan file yang lain. selanjutnya adalah menambahkan path melalui urls.py pada project_django, yaitu memasukkan mywatchlist pada url_patterns. lalu menambahkan variabel variabel yang akan ada pada models.py beserta fieldnya. selanjutnya akan memuat data pada folder fixtures yang ada pada app mywatchlist. selanjutnya adalah membuat beberapa fungsi pada views.py berkaitan dengan html xml dan json serta melakukan routing menggunakan urls.py pada mywatchlist. terakhir melakukan testing pada 3 fungsi yang berbeda untuk html, xml, dan json. selanjutnya commit dan push
![Gambar]('../../xml_postman.jpg?raw=true')
![Gambar]('../../json_postman.jpg?raw=true')
![Gambar]('../../html_postman.jpg?raw=true')