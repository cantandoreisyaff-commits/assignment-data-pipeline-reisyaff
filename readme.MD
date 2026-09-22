Deskripsi Dataset  : Data ini berisi informasi tentang  spesifikasi mobil dari karakteristik suatu mobil sampai harga jualnya
Sumber Data : file "automobileEDA_dirty_training.csv" yang terletak di '.../data/raw/'
Struktur folder : 

Assigment Data Cleansing/
├── data/
│   ├── raw/
│   │   └── automobileEDA_dirty_training.csv
│   └── processed/
│       └── automobileEDA_processed.csv
├── src/
│   └── pipeline.py
├── documentation/
│   └── data-flow-diagram.png
├── README.md
└── requirements.txt

Cara Menginstall Independency 
Ada dua cara:
1. Install satu satu di terminal dengan menulis :
- pip install pandas 
- pip install numpy 
- pip install matplotlib 
- pip install seaborn
2. Buat file txt requirement yang isinya: 
"pandas
numpy
seaborn
matplotlib"
Dan run di terinal dengan mengetik : pip install -r requirements.txt (Jika nama filenyarequirements.txt )

Penjelasan Simple ETL:

    [Extract]                  [Transform]                       [Load]
Read CSV Raw  --> Cleaning & Encoding Transformation  -->  Export Clean CSV
(data/raw/)             (Pipeline Functions)             (data/processed/)

Lokasi Processed Dataset:
data/processed/automobileEDA_processed.csv

Ukuran Awal Dataset

------Duplicate-----

Total baris yang terduplikasi : 4

------Missing Data-----
transaction_date    2
make                2
num-of-doors        2
stroke              4
horsepower          3
price               3
dtype: int64
Jumlah Baris :205
Jumlah Kolom :30

-----Categorical Column-----
['transaction_date',
 'make',
 'aspiration',
 'num-of-doors',
 'body-style',
 'drive-wheels',
 'engine-location',
 'engine-type',
 'num-of-cylinders',
 'fuel-system',
 'horsepower-binned',
 'symboling',
 'diesel',
 'gas']

-----Numerical Column-----
['normalized-losses',
 'wheel-base',
 'length',
 'width',
 'height',
 'curb-weight',
 'engine-size',
 'bore',
 'stroke',
 'compression-ratio',
 'horsepower',
 'peak-rpm',
 'city-mpg',
 'highway-mpg',
 'price',
 'city-L/100km']


Data Cleansing - Categorical

1. Mengisi data yang nul menggunakan .fillna 
dari data:
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   transaction_date   203 non-null    str    
 1   symboling          205 non-null    int64  
 2   normalized-losses  205 non-null    int64  
 3   make               203 non-null    str    
 4   aspiration         205 non-null    str    
 5   num-of-doors       203 non-null    str    
 6   body-style         205 non-null    str    
 7   drive-wheels       205 non-null    str    
 8   engine-location    205 non-null    str    
 9   wheel-base         205 non-null    float64
 10  length             205 non-null    float64
 11  width              205 non-null    float64
 12  height             205 non-null    float64
 13  curb-weight        205 non-null    int64  
 14  engine-type        205 non-null    str    
 15  num-of-cylinders   205 non-null    str    
 16  engine-size        205 non-null    int64  
 17  fuel-system        205 non-null    str    
 18  bore               205 non-null    float64
 19  stroke             201 non-null    float64
 20  compression-ratio  205 non-null    float64
 21  horsepower         202 non-null    float64
 22  peak-rpm           205 non-null    float64
 23  city-mpg           205 non-null    int64  
 24  highway-mpg        205 non-null    int64  
 25  price              202 non-null    float64
 26  city-L/100km       205 non-null    float64
 27  horsepower-binned  204 non-null    str    
 28  diesel             205 non-null    int64  
 29  gas                205 non-null    int64  

 Ke:
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   transaction_date   205 non-null    str    
 1   symboling          205 non-null    int64  
 2   normalized-losses  205 non-null    int64  
 3   make               205 non-null    str    
 4   aspiration         205 non-null    str    
 5   num-of-doors       205 non-null    str    
 6   body-style         205 non-null    str    
 7   drive-wheels       205 non-null    str    
 8   engine-location    205 non-null    str    
 9   wheel-base         205 non-null    float64
 10  length             205 non-null    float64
 11  width              205 non-null    float64
 12  height             205 non-null    float64
 13  curb-weight        205 non-null    int64  
 14  engine-type        205 non-null    str    
 15  num-of-cylinders   205 non-null    str    
 16  engine-size        205 non-null    int64  
 17  fuel-system        205 non-null    str    
 18  bore               205 non-null    float64
 19  stroke             201 non-null    float64
 20  compression-ratio  205 non-null    float64
 21  horsepower         202 non-null    float64
 22  peak-rpm           205 non-null    float64
 23  city-mpg           205 non-null    int64  
 24  highway-mpg        205 non-null    int64  
 25  price              202 non-null    float64
 26  city-L/100km       205 non-null    float64
 27  horsepower-binned  205 non-null    str    
 28  diesel             205 non-null    int64  
 29  gas                205 non-null    int64 

2. Menghapuskan data duplicate menggunakan .drop_duplicates()
dari:
Total baris yang terduplikasi : 4
ke:
Jumlah data terduplikasi : 0


3. ada data string yang penulisannnya berbeda sehingga bisa mempengaruhi pengkategorian dari suatu data:
- disini aku menggunakan lower untuk mengecilkan semua tulisan data 
- dan aku menggunakan strip untuk menghilangkan spasi yang tidak dibutuhkan 
ALFA-ROMERO	---> alfa-romero

4. Ada penulisan tanggal dan tahun yang tidak singkron juga yang harus disingkronkan:
- Aku menggunakan library pandasm untuk menyamakan penulisan date di data pd.to_datetime
02/01/2025	---> 2025-01-02	
04-jan-2025	 ---> 2025-01-04	

Data Cleansing - Numerical
1. Melihat penyebaran datanya menggunakan visualisasi dengan marplotlib
2. mengidentifikasi mana penyebaran yang normal dan penyebaran yang skew kanan atau skew kiri 
3. 
 data_raw['stroke'] = data_raw['stroke'].fillna(data_raw['stroke'].mean())
data_raw['horsepower'] = data_raw['horsepower'].fillna(data_raw['horsepower'].median())
data_raw['price'] = data_raw['price'].fillna(data_raw['price'].median())

menggunakan ini karena "stroke" penyebarannnya normal, jadi pengisian data nullnya memakai mean
sedangkan "horsepower" memiliki penyebaran data skew kanan dan "price" memiliki penyebaran data skew kanan juga sehingga mengharuskan untuk menggunakan median untuk mengisi colomn nullnya

Data Transformation 

Nama kolom yang ditransformasi : 
- symboling
- diesel
- gas
Kolom ini dipilih karena data typenya masih int tujuannnya agar bisa dirubah ke int

 #   Column                  Non-Null Count  Dtype         
---  ------                  --------------  -----         
 0   transaction_date        201 non-null    datetime64[us]
 1   symboling               201 non-null    str           
 2   normalized-losses       201 non-null    float64       
 3   make                    201 non-null    float64       
 4   aspiration              201 non-null    int64         
 5   num-of-doors            201 non-null    str           
 6   engine-location         201 non-null    int64         
 7   wheel-base              201 non-null    float64       
 8   length                  201 non-null    float64       
 9   width                   201 non-null    float64       
 10  height                  201 non-null    float64       
 11  curb-weight             201 non-null    float64       
 12  engine-type             201 non-null    float64       
 13  num-of-cylinders        201 non-null    str           
 14  engine-size             201 non-null    float64       
 15  fuel-system             201 non-null    float64       
 16  bore                    201 non-null    float64       
 17  stroke                  201 non-null    float64       
 18  compression-ratio       201 non-null    float64       
 19  horsepower              201 non-null    float64       
 20  peak-rpm                201 non-null    float64       
 21  city-mpg                201 non-null    float64       
 22  highway-mpg             201 non-null    float64       
 23  price                   201 non-null    float64       
 24  city-L/100km            201 non-null    float64       
 25  horsepower-binned       201 non-null    int64         
 26  diesel                  201 non-null    str           
 27  gas                     201 non-null    str           
 28  body-style_convertible  201 non-null    bool          
 29  body-style_hardtop      201 non-null    bool          
 30  body-style_hatchback    201 non-null    bool          
 31  body-style_sedan        201 non-null    bool          
 32  body-style_wagon        201 non-null    bool          
 33  drive-wheels_4wd        201 non-null    bool          
 34  drive-wheels_awd        201 non-null    bool          
 35  drive-wheels_fwd        201 non-null    bool          
 36  drive-wheels_rwd        201 non-null    bool

                I
                I
                I
                V
#   Column                  Non-Null Count  Dtype         
---  ------                  --------------  -----         
 0   transaction_date        201 non-null    datetime64[us]
 1   symboling               201 non-null    int64         
 2   normalized-losses       201 non-null    float64       
 3   make                    201 non-null    float64       
 4   aspiration              201 non-null    int64         
 5   num-of-doors            201 non-null    str           
 6   engine-location         201 non-null    int64         
 7   wheel-base              201 non-null    float64       
 8   length                  201 non-null    float64       
 9   width                   201 non-null    float64       
 10  height                  201 non-null    float64       
 11  curb-weight             201 non-null    float64       
 12  engine-type             201 non-null    float64       
 13  num-of-cylinders        201 non-null    str           
 14  engine-size             201 non-null    float64       
 15  fuel-system             201 non-null    float64       
 16  bore                    201 non-null    float64       
 17  stroke                  201 non-null    float64       
 18  compression-ratio       201 non-null    float64       
 19  horsepower              201 non-null    float64       
 20  peak-rpm                201 non-null    float64       
 21  city-mpg                201 non-null    float64       
 22  highway-mpg             201 non-null    float64       
 23  price                   201 non-null    float64       
 24  city-L/100km            201 non-null    float64       
 25  horsepower-binned       201 non-null    int64         
 26  diesel                  201 non-null    int64         
 27  gas                     201 non-null    int64         
 28  body-style_convertible  201 non-null    bool          
 29  body-style_hardtop      201 non-null    bool          
 30  body-style_hatchback    201 non-null    bool          
 31  body-style_sedan        201 non-null    bool          
 32  body-style_wagon        201 non-null    bool          
 33  drive-wheels_4wd        201 non-null    bool          
 34  drive-wheels_awd        201 non-null    bool          
 35  drive-wheels_fwd        201 non-null    bool          
 36  drive-wheels_rwd        201 non-null    bool 



