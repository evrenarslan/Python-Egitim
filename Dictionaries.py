# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Dictionary kullanmanın neden gerekli olduğunu anlamak için bir örnek yapalım. Birbiri ile uyumlu iki adet listemiz olsun
#Bunlardan almanyanın başkentini bulalım.

indeks_ger=countries.index("germany") # germany için index değerini buluyorum

print(capitals[indeks_ger]) # bulduğum indexli başkent değerini yazdırıyorum.

# böyle bir değeri bir dictionary içinde daha rahat bulurum

europe={"spain":"madrid","france":"paris","germany":"berlin","norway":"oslo"} # süslü parantez ile dictionary tanımladım.

print(europe)

print(europe.keys()) # Key değerlerini getirir
print(europe.values()) # Value değerlerini getirir

print(europe["germany"]) # Dictionary içindeki bir key için değeri getirir.  Tıpkı liste içerisinden getirir gibi key değeri vererek çağırırız.

# Dictionary operations 

europe["italy"]="Roma" # Dictionary içine Italy diye bir değer ekledim.

print(europe)

europe["Türkiye"]="İstanbul" # Dictionary içine Türkiye ve capital city olarak İstanbul ekledim

print(europe)

europe["Türkiye"]="Ankara" # Yanlış olduğunu anlayıp İstanbul değerini Ankara ile değiştirdim.

print(europe)

print("Türkiye" in europe) # kullanımı ile bir değerin bir dictionary içinde olup olmadığını anlarız. Bize True yada False döner

# Dictionary içindeki bir değeri silmek

europe["Polonya"]="Varşova" # Polonya için dictionary içine ekleme yaptık.

print(europe)

del(europe["Polonya"]) # Polonya dictionary içinden silinir.

print(europe)
