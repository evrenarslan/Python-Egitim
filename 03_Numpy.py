import numpy as np 

Data=[[1,2,3],[4,5,6],[7,8,9]] # Burada standart bir array yarattık.

print(Data)
# Burada yaratılan array'i numpy array haline getireceğim.

np_data=np.array(Data)

print(np_data)

# Array içerisindeki belili bir indeksteki değeri çağırmak 

print(np_data[0]) # Sıfır indeksteki değeri getirdik. 0 numaralı indeks içindeki değer de array olduğu için bu şekilde bir değer döndü

print(np_data[0][0]) # Sıfır indeksli  array içerisindeki 0 indeksli değer gelir.

print(np_data[0,0]) # Bu notasyon ile de aynı değeri getiririz.

print(np_data[1,2])


# ARANGE fonksiyonu = Verilen değerler arasında belirli bir kurala göre otomatik  array yaratır. 

sayilar_birer=np.arange(0,1000) # Birer atlayarak array yaratır
sayilar_besli=np.arange(0,1000,5) # 5'erli bir array yaratır

print(sayilar_besli)

# ZERO fonksiyonu= Sıfırlardan oluşan array yada matris (ki array'da bir matristir.) oluşturmak için kullanılır.

sifir_array=np.zeros(100) # 100 tane sıfırdan oluşan array
sifir_matris=np.zeros((100,100)) # sıfırlardan oluşan 100x100 matris oluşturdu

print(sifir_matris)

# ONES fonksiyonu = Birlerden oluşan bir matris yaratmak için kullanılır

birler_array=np.ones(100)
birler_matris=np.ones((20,5))

print(birler_matris)

# EYE fonksiyonu = Birim matris üretmek için kullanılır. Birim matrisler matris çarpımlarında etkisiz elemandır.

A=np.array([1,2]),[3,4]
birim_matris=np.eye(2) # 2x2 birim matris yaratır.

print(birim_matris)

print(np.matmul(A,birim_matris))

# linspace fonksiyonu = Bu fonksiyon  bir array yaratmak için kullanılır. linspace(start,stop,num=50,endpoint=True,restep=False,dtype=None,axis=0)
# Başlangıç ve bitiş değerleri verilen sayılar arasında 3. parametre olarak adette elemanlı bir array yaratır.

np.linspace(0,100) # # 0'dan başlayıp 100'de biten 50 elemanlı bir array
np.linspace(0,100,5) # 0'dan başlayıp 100'de biten 5 elemanlı bir array
np.linspace(0,100,5,False) # 0'dan başlayıp 80'de biten (100 dahil olmadı - 4. parametre False) 5 elemanlı arrray
np.linspace(0,100,5,False,True) # 0'dan başlayıp 80'de biten (100 dahil olmadı - 4. parametre False) 5 elemanlı arrray. En son eklenen parametre ile elemanların kaçar kaçar arttıklarınıda yazdı



#Random = Rastgele sayılar üretmek için kullanılan fonksiyondur.

# numpy.random.randint => rastgele integer sayılar üretmek için kulanılır.
np.random.randint(10) # 0 ile 10 arasında 10'dan küçük sayılar arasından rastgele bir integer sayı döner.
np.random.randint(0,10)  # 0 ile 10 arasında 10'dan küçük sayılar arasından rastgele bir integer sayı döner.
np.random.randint(0,10,5) # 0 ile 10 arasında 10'dan küçük sayılar arasından rastgele  5 tane integer sayı döner.
np.random.randint(0,10,(2,4)) # 0 ile 10 arasında 10'dan küçük sayılar arasından rastgele 2x4 tane integer sayıdan oluşan bir matris döner.

# numpy.random.rand => Sıfır ile 1 arasında float sayılar üretmek için kullanılır. Eşit dağılımlı bir array yada matris oluşturur.
np.random.rand(5) #  5 adet sayı içeren bir array üretir.
np.random.rand(5,2) # 5x2 rastgele sayılardan oluşan bir matris oluşturur. 

#numpy.random.randn => Normal (Gaussian) dağılımlı rastgele sayı yada sayı dizileri oluşturur. Oluşturulan sayı dizisinin ortalaması 0 sapması 1 olur.

np.random.randn() # Rastgele - yada + bir float sayı üretir
np.random.randn(3) # Rastgele - yada + 3 float sayı üretir
np.random.randn(3,2) # Rastgele - yada + 3x2 float bir matris üretir

# RESHAPE 

