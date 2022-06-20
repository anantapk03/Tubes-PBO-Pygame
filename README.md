# Game Development Life Cycle (GDLC) 
#### Pemrograman Berorientas Objek 
```
Dibuat oleh :
ANANTA PADMA KUSUMA (2105031) - D4 RPL 1B
CEPRI DAMIRI (2105036) - D4 RPL 1B 
```

## Initiation Game 

#### 1. Story
```
  1.1 Plot
      Misi penyelamatan galaksi dari ancaman meteorit. 
      
  1.2 Character
      Spaceship
      
  1.3 Setting
      Galaksi ruang angkasa 
      
  1.4 Theme
      Space and Laga
   
  1.5 Mechanic
      Run and shoot dari meteorit. 
```

#### 3. Aesthetic
```
   Suasana yang dibuat menegangkan.
```
#### 4. Technology
```
   Desktop game
```
## Pre - Production Game
#### Game Design Document


#### 1. High Concept
 ```
 ini adalah game yang dimana kita sebagai player
 yang bertugas untuk menyelamatkan galaksi dari 
 ancaman meteorit dengan cara menghindar dan menembak
 meteor hingga hancur (meledak)
```
#### 2. Unique Value
```
 game ini membutuhkan kecepatan dan kelihaian tangan karena harus
 menghindar serta menembak meteorit yang arah geraknya tidak bisa ditebak.
 ```
#### 3. Genre
```
 game ini bergenre space dan laga.
```
#### 4. Target Audience
```
 Game ini dapat dimainkan dari kalangan anak-anak hingga orang dewasa.
``` 
#### 5. Story
```
  ancaman meteorit telah menghantui galaksi saat ini sehingga 
 sebagai bentuk antisipasi agar dampak meteorit tidak menghantam
 dan merusak galaksi maka dikirimkan pesawat yang dapat dikendalikan
 untuk menghancurkan meteorit(dalam kurun waktu tertentu) dengan arah 
 gerak meteor yang tidak dapat ditebak.

```
#### 6. Gameplay
```
  pemain diminta mengendalikan pesawat untuk menembak meteorit yang
 jatuh dan menghindar. Meteorit berjatuhan secara tidak beraturah (random) sehingga 
 player perlu mengatur keterampilan menghindar dan kemampuan 
 menembak secara tepat agar meteorit tidak mengenai space ship yang ia kendalikan serta tidak merusak galaksi.
```

## Production Game 
### Analisis Class Diagram yang Dibutuhkan

![ClassDiagram_Game](https://raw.githubusercontent.com/anantapk03/Tubes-PBO-Pygame/main/ClassDiagram_Game.png "Gambar Class Diagram Game")

```
1. Kelas Menu nantinya akan bertugas menampilkan tampilan awal dan menampilkan tampilan ketika player kehabisan 
   nyawa. Maka dari itu kelas Menu akan menyimpan informasi dari kelas Nyawa. 

2. Kelas Nyawa akan memiliki tugas menampilkan dan mengkalkulasi nyawa dari player. kelas ini akan menyimpan informasi 
   dari kelas ShieldBar yang mana nantinya akan ada tiga kesempatan nyawa dan setiap nyawa memiliki shield bar yang 
   full jika player tidak mengalami tabrakan dengan Meteor. 

3. Kelas Shield Bar nantinya akan meyimpan informasi dari player yang memiliki hubungan asosiasi dengan kelas Meteor. 
   Satu-satunya penentu mengapa shield bar berkurang adalah ketika objek Player dan Meteor bertabrakan sehingg player 
   nantinya akan meledak. 

4. Kelas Player pada kelas ini akan memiliki tugas seperti player yang bisa bergerak ke kanan dan ke kiri, lalu menembak 
   yang mana hal tersebut bisa terjadi karena kelas ini menyimpan informasi dari kelas Peluru. nantinya tembakan akan ditujukan 
   oleh meteor yang mana ketika peluru dan meteor berbenturan maka akan terjadi ledakan yang mengakibatkan score yang dimiliki player 
   bertambah.

5. Kelas Meteor merupakan musuh dari Player. Meteor dapat meledak karena menerima peluru yang ditembakan oleh Player. 
   Kelas ini juga menyimpan informasi dari player. Player dan Meteor ketika bertabrakan maka akan terjadi ledakan sehingga 
   dua kelas tersebut memiliki hubungan composition dengan kelas Ledakan. 
   
6. Kelas Ledakan akan memiliki hubungan dengan kelas meteor dan Player yaitu hubungan Composition. Karena kelas Player dan Meteor yang 
   dapat memungkinkan terjadinya ledakan. Player dapat membuat Meteor meledak karena player menyimpan peluru. sedangkan Player dapat meledak 
   karena terjadinya tabrakan antara Meteor dan Player. 

7. Kelas Peluru memiliki hubungan Agregation dengan kelas Player. Player akan menyimpan informasi dari kelas Peluru yang mana nantinya Peluru
   dapat digunakan oleh Player. 
   
```

### Asset Game 

```
1. 
```
