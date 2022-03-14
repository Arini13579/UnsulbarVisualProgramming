print ("")
print ("silahkan pilih Operasi Hitung di bawah ini")
print ("---------------")
print ("1.penjumlahan")
print ("2.pengurangan")
print ("3.perkalian")
print ("4.pembagian")
print ("===============")

bilangan = int (input ("Masukkan pilihan bilangan 1/2/3/4   :"))
bil1     = int (input ("Masukkan bilangan pertama           :"))
bil2     = int (input ("Masukkan bilangan kedua             :"))

if (bilangan==1 ):
    print  (bil1," + " ,bil2," = ",(bil1 + bil2))

elif(bilangan==2):
    print  (bil1," - " ,bil2," = ",(bil1 - bil2))
    
elif(bilangan==3):
    print  (bil1," x " ,bil2," = ",(bil1 * bil2))
    
elif(bilangan==4):
    print  (bil1," / " ,bil2," = ",(bil1 / bil2))
    
else:
    print ("tidak ada pilihan")
