''' Evren Arslan @earslan 2019.11.29'''

a="Evren"
print(a)
print(a[2])
#a[2]="t" # string değerleri değiştirilemez (immutable)

# Local and Global scope for variable

def a_function():
    test_var="Arslan"
    return(test_var)



##print(test_var) # fonksiyonlarda yaratılan değişkenler localdir.

for i in range(1,11):
    test_scope="Ali Emren Arslan"

print(test_scope) # for döngüsü içinde yaratılan değişken local değildir.


if 1==1:
    test_sc1="if içerisindeki değer"
else:
    test_sc2="else içerisindeki değer"

print(test_sc1) #if içerisindeki değer global blok dışından geliyor
print(test_sc2) # else içindeki değer local blok dışından gelmiyor.

## Global Scope =>
