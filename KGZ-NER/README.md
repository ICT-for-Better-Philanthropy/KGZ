# KGZ-NER

## Proses akuisisi data

Sumber data yang dijadikan rujukan dalam pengembangan KGZ ini dibagi kedalam 3 (tiga) kelompok yakni:
1. Data yang bersumber dari internet.
   Data yang bersumber dari internet diperoleh melalui teknik crawling, dimana penjelasannnya dapat dilihat pada link berikut: https://github.com/ICT-for-Better-Philanthropy/KGZ-NER/tree/master/data/data_crawling
2. Data yang bersumber berdasarkan regulasi dan panduan zakat dari Kementerian Agama RI dan buku-buku mengenai zakat.
   Data yang berhasil kami kumpulkan adalah sebagai berikut:
   1. Hukum zakat dan wakaf [Buku]
   2. Undang-undang RI nomor 23 tahun 2011 tentang pengelolaan zakat
   3. Standarisasi amil zakat Indonesia [buku]
   4. Panduan organisasi pengelola zakat [buku]
   5. Petunjuk pelaksanaan pengumpulan zakat [buku]
3. Data yang bersumber dari wikipedia.
   Data yang didapat dari wikipedia terkait dengan zakat dengan keyword pencarian adalah zakat.

## Membuat definisi untuk properti model KGZ-NER
Pembuatan model untuk IndonesianNER pada domain Zakat ini menggunakan librari dari StanfordNER. Model yang dibuat berdasarkan masukan dari data training, pada model data training dapat berupa single dokumen atau list dokume yang diatur dalam file properti. Adapun contoh dari isi dari file property adalah sebagai berikut:

```
trainFileList = 1_document.tsv,23_document.tsv
serializeTo = ner-model-id.ser.gz
map = word=0,answer=1

useClassFeature=true
useWord=true
useNGrams=true
noMidNGrams=true
maxNGramLeng=6
usePrev=true
useNext=true
useSequences=true
usePrevSequences=true
maxLeft=1
useTypeSeqs=true
useTypeSeqs2=true
useTypeySequences=true
wordShape=chris2useLC
useDisjunctive=true
``` 

Contoh property diatas mendukung inputan dari multi dokumen training, jika hanya menggunakan satu dokumen training cukup mengganti trainFileList menjadi trainFile.
Sebagai contoh simpan contoh isi property diatas dalam file prop.txt. dan kemudian buatlah model dengan perintah dibawah ini:

## Membangun Model KGZ-NER
Perintah untuk membuat model
```
java -mx600m -cp "*;lib\*" edu.stanford.nlp.ie.crf.CRFClassifier -prop prop.txt
```


## Validasi Model KGZ-NER dengan menggunakan K-Fold Cross Validation
Untuk keperluan evaluasi terhadap model dan memilih model yang terbaik berdasarkan data training dan data testing yang dipersiapkan berdasarkan metode K-Fold Cross Validation, maka dilakukan pengecekan dengan menggunakan perintah sebagai berikut:
```
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model-id.ser.gz -testFile 1_testing.tsv
```