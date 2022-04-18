from tkinter import *
 
window = Tk()
window.title("GUI Kalkulator")
window.geometry('250x150')
 
label = Label(window, text="==KALKULATOR==")
label.grid(column=0) 

label1 = Label(window, text="Nilai 1 : ",anchor="e",width=20)
label1.grid(column=0, row=1)
 
nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=1)
 
 
label2 = Label(window, text="Nilai 2 : ",anchor="e",width=20)
label2.grid(column=0, row=2)
 
nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=2)
 
label3 = Label(window, text="Hasil : ",anchor="e",width=20)
label3.grid(column=0, row=3)
 
hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=3)
 
def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))
 
def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))
 
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
 
def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))
 
 
tombol = Button(window, text="( + )", command=tambah)
tombol.grid(column=0, row=4)
 
tombol = Button(window, text="( - )", command=kurang)
tombol.grid(column=0, row=5)
 
tombol = Button(window, text="( x )", command=kali)
tombol.grid(column=1, row=4)
 
tombol = Button(window, text="( / )", command=bagi)
tombol.grid(column=1, row=5)


 
window.mainloop()