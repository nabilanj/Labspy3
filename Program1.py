PT = 100000000
sum = 0
x = 0

laba =[int(0), int(0), int(PT)* .1, int(PT)* .1, int(PT)* .5, int(PT)* .5, int(PT)* .5, int(PT)* .2]
print ("Modal Awal PT : ", PT)
for y in laba :
    sum = sum + y
    x+= 1
    print("Laba Bulan Ke- ", x,"Sebesar : ", y)
print ("Total Laba PT adalah : ", sum)

