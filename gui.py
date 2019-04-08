from tkinter import *
import matplotlib.pyplot as plt
import datetime

master = Tk()
hr1 = IntVar()  # Deklariranje varijabli za buduce koristenje
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


def calc(it):  # preko "varijabla.get()"  se dobivaju vrijednosti za tu varijablu
    global hr1, eng1, lat1, glaz1, lik1, pov1, geo1, mat1, fiz1, bio1, inf1, tzk1, vj1, kem1, et1, tal1, soc1, log1, izbor2
    zbroj = hr1.get() + eng1.get() + lat1.get() + glaz1.get() + lik1.get() + pov1.get() + geo1.get() + mat1.get() + fiz1.get() + bio1.get() + inf1.get() + tzk1.get() + vj1.get() + kem1.get() + et1.get() + tal1.get() + soc1.get() + log1.get()
    global prosjek
    p = 0
    broj = [hr1.get(), eng1.get(), lat1.get(), glaz1.get(), lik1.get(), pov1.get(), geo1.get(), mat1.get(), fiz1.get(),
            bio1.get(), inf1.get(), tzk1.get(), vj1.get(), kem1.get(), et1.get(), tal1.get(), soc1.get(), log1.get()]
    for i in broj:
        if i != 0:
            p += 1
    try:
        prosjek1 = str(round(int(zbroj) / (int(p)), 3))
    except ZeroDivisionError:
        prosjek1 = ' '
    boja = ""
    if p == 0:
        boja = "#ffffff"
        prosjek2 = Label(master, text="         Prosjek: " + prosjek1 + "         ", bg=boja).place(x=620, y=340)
    else:
        if (zbroj / p) >= (4.5):  # mijenjanje boja pozadine Labela "prosjek" ovisno o ocjeni
            boja = "#3bef9b"
        elif (zbroj / p) <= 4.5 and (zbroj / p) > 3.5:
            boja = "#3befdc"
        elif (zbroj / p) <= 3.5 and (zbroj / p) > 2.5:
            boja = "#efe03b"
        elif (zbroj / p) <= 2.5 and (zbroj / p) > 1.5:
            boja = "#ce9339"
        else:
            boja = "#ff0000"

    prosjek2 = Label(master, text="         Prosjek: " + prosjek1 + "         ", bg=boja).place(x=620, y=340)


def graf():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    broj = [hr1.get(), eng1.get(), lat1.get(), glaz1.get(), lik1.get(), pov1.get(), geo1.get(), mat1.get(), fiz1.get(),
            bio1.get(), inf1.get(), tzk1.get(), vj1.get(), kem1.get(), et1.get(), tal1.get(), soc1.get(), log1.get()]
    for i in broj:
        if i == 5:
            a += 1
    for i in broj:
        if i == 4:
            b += 1
    for i in broj:
        if i == 3:
            c += 1
    for i in broj:
        if i == 2:
            d += 1
    for i in broj:
        if i == 1:
            e += 1

    labels = ['Odlične ocjene', 'Vrlo Dobre ocjene', 'Dobre ocjene ', 'Dovoljne ocjene', 'Nedovoljne ocjene']
    sizes = [a, b, c, d, e]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
    u = 0
    if a == 0:
        del labels[0]  # ako npr ocjena 5 ne postoji mice se iz liste kako ne bi utjecala na graf
        del sizes[0]
        del colors[0]
        u += 1
    if b == 0:
        del labels[1 - u]
        del sizes[1 - u]
        del colors[1 - u]
        u += 1
    if c == 0:
        del labels[2 - u]
        del sizes[2 - u]
        del colors[2 - u]
        u += 1
    if d == 0:
        del labels[3 - u]
        del sizes[3 - u]
        del colors[3 - u]
        u += 1
    if e == 0:
        del labels[4 - u]
        del sizes[4 - u]
        del colors[4 - u]
        u += 1
        # opcije za graf
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


def save():  # sve isto kao i graf() samo sto ga ne prikazuje vec sprema u istu mapu u kojoj se kod nalazi
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    broj = [hr1.get(), eng1.get(), lat1.get(), glaz1.get(), lik1.get(), pov1.get(), geo1.get(), mat1.get(), fiz1.get(),
            bio1.get(), inf1.get(), tzk1.get(), vj1.get(), kem1.get(), et1.get(), tal1.get(), soc1.get(), log1.get()]
    for i in broj:
        if i == 5:  # broji koliko je ukupno ocjena kako bi se mogao izracunati prosjek
            a += 1
    for i in broj:
        if i == 4:
            b += 1
    for i in broj:
        if i == 3:
            c += 1
    for i in broj:
        if i == 2:
            d += 1
    for i in broj:
        if i == 1:
            e += 1

    labels = ['Odlične ocjene', 'Vrlo dobre ocjene', 'Dobre ocjene ', 'Dovoljne ocjene', 'Nedovoljne ocjene']
    sizes = [a, b, c, d, e]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
    u = 0
    if a == 0:
        del labels[0]  # u slucaju da jedna ili vise ocjena ne postoje ovako se micu iz liste kako  ne bi
        del sizes[0]  # utjecele na kod
        del colors[0]
        u += 1
    if b == 0:
        del labels[1 - u]
        del sizes[1 - u]
        del colors[1 - u]
        u += 1
    if c == 0:
        del labels[2 - u]
        del sizes[2 - u]
        del colors[2 - u]
        u += 1
    if d == 0:
        del labels[3 - u]
        del sizes[3 - u]
        del colors[3 - u]
        u += 1
    if e == 0:
        del labels[4 - u]
        del sizes[4 - u]
        del colors[4 - u]

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    ime = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")  # za ime spremljene datoteke koristi datum i vrijeme
    plt.savefig(ime)  # kako bi se izbjeglo brisanje i zamjenjivanje slika


master.title("Prosjek")
backg = PhotoImage(file="backgg.gif")
master.config(width=800, height=400)  # kod za dizajn grafickog sucelja
backg2 = Label(master, text="", image=backg, bg="white").place(x=0, y=0, relwidth=1, relheight=1)
hr = Scale(master, from_=0, to=5, bg="white", orient=HORIZONTAL, variable=hr1, command=calc).place(x=200, y=0)
hr2 = Label(master, text="Hrvatski jezik", bg="white").place(x=0, y=20)
eng = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=eng1, command=calc, bg="white").place(x=200, y=40)
eng2 = Label(master, text="Engleski jezik", bg="white").place(x=0, y=60)
lat = Scale(master, from_=0, to=5, orient=HORIZONTAL, variable=lat1, command=calc, bg="white").place(x=200, y=80)
lat2 = Label(master, text="Latinski jezik", bg="white").place(x=0, y=100)
glaz = Scale(master, from_=0, to=5, orient=HORIZONTAL, bg="white", variable=glaz1, command=calc).place(x=200, y=120)
glaz2 = Label(master, text="Glazbena umjetnost", bg="white").place(x=0, y=140)
lik = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=lik1, command=calc).place(x=200, y=160)
lik2 = Label(master, bg="white", text="Likovna umjetnost").place(x=0, y=180)
pov = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=pov1, command=calc).place(x=200, y=200)
pov2 = Label(master, bg="white", text="Povijest").place(x=0, y=220)
geo = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=geo1, command=calc).place(x=200, y=240)
geo2 = Label(master, bg="white", text="Geografija").place(x=0, y=260)
mat = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=mat1, command=calc).place(x=200, y=280)
mat2 = Label(master, bg="white", text="Matematika").place(x=0, y=300)
fiz = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=fiz1, command=calc).place(x=200, y=320)
fiz2 = Label(master, bg="white", text="Fizika").place(x=0, y=340)
bio = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=bio1, command=calc).place(x=500, y=0)
bio2 = Label(master, bg="white", text="Biologija").place(x=300, y=20)
inf = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=inf1, command=calc).place(x=500, y=40)
inf2 = Label(master, bg="white", text="Informatika").place(x=300, y=60)
tzk = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=tzk1, command=calc).place(x=500, y=80)
tzk2 = Label(master, bg="white", text="Tjelesna i zdravstvena kultura").place(x=300, y=100)
vj = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=vj1, command=calc).place(x=500, y=120)
vj2 = Label(master, bg="white", text="Vjeronauk").place(x=300, y=140)
kem = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=kem1, command=calc).place(x=500, y=160)
kem2 = Label(master, bg="white", text="Kemija").place(x=300, y=180)
et = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=et1, command=calc).place(x=500, y=320)
et2 = Label(master, bg="white", text="Etika").place(x=300, y=220)
tal = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=tal1, command=calc).place(x=500, y=200)
tal2 = Label(master, bg="white", text="Talijanski jezik").place(x=300, y=260)
soc = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=soc1, command=calc).place(x=500, y=240)
soc2 = Label(master, bg="white", text="Sociologija").place(x=300, y=300)
log = Scale(master, bg="white", from_=0, to=5, orient=HORIZONTAL, variable=log1, command=calc).place(x=500, y=280)
log2 = Label(master, bg="white", text="Logika").place(x=300, y=340)
graff = PhotoImage(file="icon.png")
savee = PhotoImage(file="save.png")
label22 = Label(master, text="         Prikaži graf ocjena", bg="white").place(x=600, y=20)
graf1 = Button(master, image=graff, command=graf).place(x=675, y=50)
label23 = Label(master, text="         Spremi graf ocjena", bg="white").place(x=600, y=120)

save2 = Button(master, image=savee, command=save, bg="white").place(x=675, y=160)
mainloop()
