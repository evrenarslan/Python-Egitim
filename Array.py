
# Listelerde slicing
X=[0,1,2,3,4,5,6,7,8,9,10]
print(X[-4:]) # bir listenin son dört elemanını getirmek için kullanılan slicing yöntemi

print(X[:4]) #baştan 4 elemanını getirir
print(X[:]) # tüm listeyi getirir
print(X[1:]) # birinci elemandan başlayarak tüm listeyi getirir

Y=[["a","b","c"],["d","e","f"],["g","h","i"]] # liste içinde liste yaratılabilir

print(Y[0][1]) # liste içinde listede bir elemanı çağırırken önce ana listedeki eleman çağırılır sonra içindeki listedeki eleman
print(Y[-1][:2]) # ana listenin son elemanı olan listenin ilk iki elemanını çağırır.

# Listelerde değerlerin değiştirilmesi
X=[0,1,2,3,4,5,6,7,8,9,10]
X[1]=100 # Listenin 2. elemanını değerini 100'e ayarladı
X[-1]=200 # Listenin sonuncu elemanını değerini 200'e ayarladı
X[3:6]=[6,7,8] # Listenin 4. elemanından başlayarak 3 elemanının değerini verilen yeni dizi ile değiştirir.

#Listeye yeni değerler + işareti ile eklenebilir

Z=X+[11,12,13,14] # X listesine [11,12,13,14] değerlerini ekleyerek Z diye yeni bir liste yarattım.


# Bir liste içerisindeki değerleri silmek

del(Z[-1]) # del() ile herhangi bir değer silinebilir. 

del(Z[-4:-2]) # burada ilgili listenin sondan dördüncü ve 3. elemanlarını silmesini sağlıyorum. Bunları ayrı ayrı sildirmek istersem indis numaraları değişeceği için hata alır.


# Listeyi kopyalamak

T=Z # ile liste kopyalanabilir. Ama pointer tuttuğu için Z değişir ise  T'de değişir yada tersi

K=Z[:] # ile kopyalanır ise memory içinde yeni bir alanda yeni liste yaratır ve birbirini etkilemez.
