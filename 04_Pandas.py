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

bisikletler= pd.read_csv('bisikler.csv') # kod ile aynı dizinde olan csv dosyanı okuyarak bie df yaratır.

print(bisikletler)


#Eğer dosya içindeki ilk kolon index kolonu olacak ise
bisikletler= pd.read_csv('bisikler.csv',index_col=0) # BU parametre ile ilk kolonun index olmasını sağladık.




