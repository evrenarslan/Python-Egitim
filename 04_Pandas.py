'''
Evren Arslan @earslan 
PANDAS hakkında kısa bilgiler.
'''
#Dictionary yaratmak için üç tana array yaratıyorum.
ulkeler = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
direksiyon=  [True, False, False, False, True, True, True] # Direksiyon sağda yada solda olduğunu tanımlar
araba_sayisi = [809, 731, 588, 18, 200, 70, 45] # Her 1000 kişi başına düşen araba sayısı

import pandas as pd 

araba_dict={'Ülke':ulkeler,'Direksiyon':direksiyon,'Araba_Sayısı':araba_sayisi} # Daha önce tanımlanan arraylar üzerinden dictionary yarattık

araba=pd.DataFrame(araba_dict) # Pandas ile bir dataframe yarattık

print(araba)

# Dataframe içerisindeki index değerini  bir başka array ile değiştireceğim
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

araba.index=row_labels # row_labes değerleri index olarak atandı.

print(araba)

# CSV dosyasıdan dataframe oluşturmak

df_nufus= pd.read_csv('sehir_nufus.csv') # kod ile aynı dizinde olan csv dosyanı okuyarak bie df yaratır.

print(df_nufus)

#Eğer dosya içindeki ilk kolon index kolonu olacak ise
#df_nufus= pd.read_csv('sehir_nufus.csv',index_col=0) # Bu parametre ile ilk kolonun index olmasını sağladık.

# Dataframe içerinden değerleri listelemek.

print(df_nufus["Bolge"]) # Bolge kolonunu bir liste olarak döker
print(type(df_nufus['Bolge'])) # Tek bir köşeli parantez içerisinde getirilen veriler bir array olaak dönerler

print(df_nufus[['Bolge']]) # Burada yine Bolge kolonu gelir ama dataframe olarak gelir
print(type(df_nufus[["Bolge"]])) #  'pandas.core.frame.DataFrame' olarak dönüş yapar.

# Dataframe içerisindeki birden fazla kolonu yada satırı listelemek

print(df_nufus[["Bolge","Sehir"]]) # Bölge ve şehir kolonları dataframe olarak geldi.

print(df_nufus[0:10]) # ilk 10 satırı listeler burada çift tırnak çalışmaz sonucu dataframe olarak verir
print(type(df_nufus[0:10])) # 'pandas.core.frame.DataFrame'

# loc & iloc => loc label tabanlı "kolonların isimlerini verek" iloc ise sayı tabanlı "kolon ve satırların sıra numarasını vererek sorgulama sağlar"
#print(df_nufus.loc["Bolge"])

