from alive_progress import alive_bar
import time
import random

mylist = [1,2,3,4,5,6,7,8,9,10]
with alive_bar(len(mylist)) as bar:
    for i in mylist:
        bar()
        time.sleep(random.randint(0,5))

print("")
print("--------------------------------------------------------------------------------")
print("")
import time
from progress.bar import IncrementalBar

mylist=[1,2,3,4,5,6]

bar=IncrementalBar('Countdown',max=len(mylist)) # Burada IncremantalBar dışında seçeneklerde mevcut. Library sitesine bakılabilir.

for item in mylist:
    bar.next()
    time.sleep(1)
    
bar.finish()
print("")
print("--------------------------------------------------------------------------------")
print("")
import time
from tqdm import tqdm
mylist = [1,2,3,4,5,6,7,8,9,10]
for i in tqdm(mylist):
    time.sleep(random.randint(0,5))


print("")
print("--------------------------------------------------------------------------------")
print("")