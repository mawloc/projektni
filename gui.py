from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt
master = Tk()
l = Label(master, text="")
hr1 = IntVar()
eng1 = IntVar()
lat1 = IntVar()
glaz1 = IntVar()
lik1 = IntVar()
pov1 = IntVar()
geo1 = IntVar()
mat1 = IntVar()
fiz1 = IntVar()
bio1 = IntVar()
inf1 = IntVar()
tzk1 = IntVar()
vj1 = IntVar()
kem1 = IntVar()
et1 = IntVar()
tal1 = IntVar()
soc1 = IntVar()
log1 = IntVar()
izbor2 = IntVar()
global prosjek
prosjek = 0

def calc(it):
    global hr1, eng1, lat1, glaz1, lik1, pov1, geo1, mat1, fiz1, bio1, inf1, tzk1, vj1, kem1, et1, tal1, soc1, log1, izbor2
    zbroj = hr1.get() + eng1.get() + lat1.get() + glaz1.get() + lik1.get() + pov1.get() + geo1.get() + mat1.get() + fiz1.get() + bio1.get() + inf1.get() + tzk1.get() + vj1.get() + kem1.get() + et1.get() + tal1.get() + soc1.get() + log1.get()
    global prosjek
    prosjek1 = str(round(zbroj / (14 + izbor2.get()),2))
    prosjek2 = Label(master, text="Prosjek:"+prosjek1).place(x=600, y=300)

def graf():
    # Data to plot
    a=0
    b=0
    c=0
    d=0
    e=0
    broj = [hr1.get(),eng1.get(),lat1.get(),glaz1.get(),lik1.get(),pov1.get(),geo1.get(),mat1.get(),fiz1.get(),bio1.get(),inf1.get(),tzk1.get(),vj1.get(),kem1.get(),et1.get(),tal1.get(),soc1.get(),log1.get()]
    for i in broj:
        if i == 5:
            a+=1
    for i in broj:
        if i == 4:
            b+=1
    for i in broj:
        if i == 3:
            c+=1
    for i in broj:
        if i == 2:
            d+=1
    for i in broj:
        if i == 1:
            e+=1
    labels = 'Odlične ocjene', 'Vrlo dobre ocjene', 'Dobre ocjene ', 'Dovoljne ocjene', 'Nedovoljne ocjene'
    sizes = [a, b, c, d,e]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']

    # Plot
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

master.config(width=800, height=400)
hr = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=hr1, command=calc).place(x=200, y=0)
hr2 = Label(master, text="Hrvatski jezik").place(x=0, y=20)
eng = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=eng1, command=calc).place(x=200, y=40)
eng2 = Label(master, text="Engleski jezik").place(x=0, y=60)
lat = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=lat1, command=calc).place(x=200, y=80)
lat2 = Label(master, text="Latinski jezik").place(x=0, y=100)
glaz = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=glaz1, command=calc).place(x=200, y=120)
glaz2 = Label(master, text="Glazbena umjetnost").place(x=0, y=140)
lik = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=lik1, command=calc).place(x=200, y=160)
lik2 = Label(master, text="Likovna umjetnost").place(x=0, y=180)
pov = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=pov1, command=calc).place(x=200, y=200)
pov2 = Label(master, text="Povijest").place(x=0, y=220)
geo = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=geo1, command=calc).place(x=200, y=240)
geo2 = Label(master, text="Geografija").place(x=0, y=260)
mat = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=mat1, command=calc).place(x=200, y=280)
mat2 = Label(master, text="Matematika").place(x=0, y=300)
fiz = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=fiz1, command=calc).place(x=200, y=320)
fiz2 = Label(master, text="Fizika").place(x=0, y=340)
bio = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=bio1, command=calc).place(x=500, y=0)
bio2 = Label(master, text="Biologija").place(x=300, y=20)
inf = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=inf1, command=calc).place(x=500, y=40)
inf2 = Label(master, text="Informatika").place(x=300, y=60)
tzk = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=tzk1, command=calc).place(x=500, y=80)
tzk2 = Label(master, text="Tjelesna i zdravstvena kultura").place(x=300, y=100)
vj = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=vj1, command=calc).place(x=500, y=120)
vj2 = Label(master, text="Vjeronauk").place(x=300, y=140)
kem = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=kem1, command=calc).place(x=500, y=160)
kem2 = Label(master, text="Kemija").place(x=300, y=180)
et = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=et1, command=calc).place(x=500, y=320)
et2 = Label(master, text="Etika").place(x=300, y=220)
tal = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=tal1, command=calc).place(x=500, y=200)
tal2 = Label(master, text="Talijanski jezik").place(x=300, y=260)
soc = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=soc1, command=calc).place(x=500, y=240)
soc2 = Label(master, text="Sociologija").place(x=300, y=300)
log = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=log1, command=calc).place(x=500, y=280)
log2 = Label(master, text="Logika").place(x=300, y=340)
izbor1 = Checkbutton(master, text="Talijanski jezik", variable=izbor2).place(x=600, y=0)
graf1 = Button(master,text="Graf ocjena",command=graf).place(x=600,y=40)


mainloop()

