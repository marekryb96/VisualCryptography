from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import Image
from PIL import ImageFilter
import cv2
import random
import sys

def button1Action():
    name = text3.get("1.0", "end-1c")
    if name != "":
        filename1 = fd.askopenfilename()
        img = readPhoto1(filename1)
        thresh(img, name)
    else:
        messagebox.showinfo("Zamiana obrazu na czarno biały", "Proszę podać nazwę tworzonego pliku w, którym zostanie zapisany rezultat progowania!")


def button2Action():
    name2 = text2.get("1.0", "end-1c")
    name1 = text1.get("1.0", "end-1c")
    if name1 != "" and name2 != "":
        filename2 = fd.askopenfilename()
        img = readPhoto(filename2)
        makeCrypto(img, name1, name2)
    else:
        messagebox.showinfo("Wczytywanie obrazu do ukrycia", "Proszę podać nazwy dla obu udziałów")


def button4Action():
    global test1
    global filename3
    filename3 = fd.askopenfilename()
    global d1img
    global test1
    d1img = cv2.imread(filename3)
    if filename3 != "":
        messagebox.showinfo("Wczytywanie udziału nr 1", "Pomyślnie wczytano udział nr 1 - " + filename3)
        test1 = 1
    else:
        messagebox.showinfo("Wczytywanie udziału nr 1", "Nie udało się wczytać udziału nr 1!")

def button5Action():
    global filename4
    filename4 = fd.askopenfilename()
    global d2img
    global test2
    d2img = cv2.imread(filename4)
    if filename4 != "":
        messagebox.showinfo("Wczytywanie udziału nr 2", "Pomyślnie wczytano udział nr 2 - " + filename4)
        test2 = 1
    else:
        messagebox.showinfo("Wczytywanie udziału nr 2", "Nie udało się wczytać udziału nr 2!")

def button6Action():
    with open("pomoc.txt", 'r') as myfile1:
        data1 = myfile1.read()
        #data1 = myfile1.readlines().replace('\n', '')
        messagebox.showinfo("Pomoc", str(data1))


def button7Action():
    with open("info.txt", 'r') as myfile2:
        data2 = myfile2.read()
        messagebox.showinfo("Informacje", str(data2))

def button8Action():
    global filename3
    global filename4
    test3 = 0
    if test1 == 1 and test2 == 1:
        result = cv2.addWeighted(d1img, 0.5, d2img, 0.5, 0)
        cv2.imshow("rest", result)
        nameD = text4.get("1.0", "end-1c")
        if nameD == "":
            test3 = 0
        else:
            test3 = 1
        nameD = nameD + ".bmp"
        cv2.imwrite(nameD, result)
    else:
        if test1 == 0 and test2 == 1:
            messagebox.showinfo("Nakładanie udziałow","Nie wczytano udziału nr 1")
        elif test1 == 1 and test2 == 0:
            messagebox.showinfo("Nakładanie udziałow","Nie wczytano udziału nr 2")
        elif test1 == 0 and test2 == 0:
            messagebox.showinfo("Nakładanie udziałow", "Nie wczytano udziałów!")
        if test3 == 0:
            messagebox.showinfo("Nakładanie udziałow","Nie podano nazwy tworzonego pliku w, którym zostanie zapisany rezultat")

def rand():
    return random.randint(1, 6)

def readPhoto1(name):
    img = Image.open(name)
    return img

def readPhoto(name):
    tv = 0
    test = cv2.imread(name, 1)
    value = test[2, 2]
    if value[2] != 255 and value[2] != 0:
        tv = 1

    value = test[5, 5]
    if value[2] != 255 and value[2] != 0:
        tv = 1

    value = test[7, 7]
    if value[2] != 255 and value[2] != 0:
        tv = 1

    if tv == 0:
        img = Image.open(name)
    else:
        messagebox.showinfo("Wczytywanie obrazu ", "Obsługiwane są tylko biało czarne obrazy, proszę użyć innego obrazu lub skorzystać z funkcji progowania dostępnej w aplikacji.")
    return img

def thresh(img, name):
    temp = img.convert("L")
    threshold = 100
    out = temp.point(lambda p: p > threshold and 255)
    name = name + ".bmp"
    out.save(name)

def makeCrypto(img, name1, name2):
    img = img.convert('1')
    part1 = Image.new("1", [dimension * 2 for dimension in img.size])
    part2 = Image.new("1", [dimension * 2 for dimension in img.size])
    
    for x in range(0, img.size[0], 2):
        for y in range(0, img.size[1], 2):
            px = img.getpixel((x, y))
            assert px in (0, 255)
            dec = rand()
            if px == 255:
                if dec == 1:
                    part1.putpixel((x * 2, y * 2), 255)
                    part1.putpixel((x * 2, y * 2 + 1), 255)
                    part1.putpixel((x * 2 + 1, y * 2), 0)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                    part2.putpixel((x * 2, y * 2), 255)
                    part2.putpixel((x * 2, y * 2 + 1), 255)
                    part2.putpixel((x * 2 + 1, y * 2), 0)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 0)
                elif dec == 2:
                    part1.putpixel((x * 2, y * 2), 0)
                    part1.putpixel((x * 2, y * 2 + 1), 0)
                    part1.putpixel((x * 2 + 1, y * 2), 255)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                    part2.putpixel((x * 2, y * 2), 0)
                    part2.putpixel((x * 2, y * 2 + 1), 0)
                    part2.putpixel((x * 2 + 1, y * 2), 255)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 255)
                elif dec == 3:
                    part1.putpixel((x * 2, y * 2), 255)
                    part1.putpixel((x * 2, y * 2 + 1), 0)
                    part1.putpixel((x * 2 + 1, y * 2), 255)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                    part2.putpixel((x * 2, y * 2), 255)
                    part2.putpixel((x * 2, y * 2 + 1), 0)
                    part2.putpixel((x * 2 + 1, y * 2), 255)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 0)
                elif dec == 4:
                    part1.putpixel((x * 2, y * 2), 0)
                    part1.putpixel((x * 2, y * 2 + 1), 255)
                    part1.putpixel((x * 2 + 1, y * 2), 0)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                    part2.putpixel((x * 2, y * 2), 0)
                    part2.putpixel((x * 2, y * 2 + 1), 255)
                    part2.putpixel((x * 2 + 1, y * 2), 0)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 255)
                elif dec == 5:
                    part1.putpixel((x * 2, y * 2), 255)
                    part1.putpixel((x * 2, y * 2 + 1), 0)
                    part1.putpixel((x * 2 + 1, y * 2), 0)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                    part2.putpixel((x * 2, y * 2), 255)
                    part2.putpixel((x * 2, y * 2 + 1), 0)
                    part2.putpixel((x * 2 + 1, y * 2), 0)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 255)
                elif dec == 6:
                    part1.putpixel((x * 2, y * 2), 0)
                    part1.putpixel((x * 2, y * 2 + 1), 255)
                    part1.putpixel((x * 2 + 1, y * 2), 255)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                    part2.putpixel((x * 2, y * 2), 0)
                    part2.putpixel((x * 2, y * 2 + 1), 255)
                    part2.putpixel((x * 2 + 1, y * 2), 255)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 0)
            elif px == 0:
                if dec == 1:
                    part1.putpixel((x * 2, y * 2), 0)
                    part1.putpixel((x * 2, y * 2 + 1), 255)
                    part1.putpixel((x * 2 + 1, y * 2), 255)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                    part2.putpixel((x * 2, y * 2), 255)
                    part2.putpixel((x * 2, y * 2 + 1), 0)
                    part2.putpixel((x * 2 + 1, y * 2), 0)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 255)
                elif dec == 2:
                    part1.putpixel((x * 2, y * 2), 255)
                    part1.putpixel((x * 2, y * 2 + 1), 0)
                    part1.putpixel((x * 2 + 1, y * 2), 0)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                    part2.putpixel((x * 2, y * 2), 0)
                    part2.putpixel((x * 2, y * 2 + 1), 255)
                    part2.putpixel((x * 2 + 1, y * 2), 255)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 0)
                elif dec == 3:
                    part1.putpixel((x * 2, y * 2), 255)
                    part1.putpixel((x * 2, y * 2 + 1), 255)
                    part1.putpixel((x * 2 + 1, y * 2), 0)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                    part2.putpixel((x * 2, y * 2), 0)
                    part2.putpixel((x * 2, y * 2 + 1), 0)
                    part2.putpixel((x * 2 + 1, y * 2), 255)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 255)
                elif dec == 4:
                    part1.putpixel((x * 2, y * 2), 0)
                    part1.putpixel((x * 2, y * 2 + 1), 0)
                    part1.putpixel((x * 2 + 1, y * 2), 255)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                    part2.putpixel((x * 2, y * 2), 255)
                    part2.putpixel((x * 2, y * 2 + 1), 255)
                    part2.putpixel((x * 2 + 1, y * 2), 0)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 0)
                elif dec == 5:
                    part1.putpixel((x * 2, y * 2), 255)
                    part1.putpixel((x * 2, y * 2 + 1), 0)
                    part1.putpixel((x * 2 + 1, y * 2), 255)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                    part2.putpixel((x * 2, y * 2), 0)
                    part2.putpixel((x * 2, y * 2 + 1), 255)
                    part2.putpixel((x * 2 + 1, y * 2), 0)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 255)
                elif dec == 6:
                    part1.putpixel((x * 2, y * 2), 0)
                    part1.putpixel((x * 2, y * 2 + 1), 255)
                    part1.putpixel((x * 2 + 1, y * 2), 0)
                    part1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                    part2.putpixel((x * 2, y * 2), 255)
                    part2.putpixel((x * 2, y * 2 + 1), 0)
                    part2.putpixel((x * 2 + 1, y * 2), 255)
                    part2.putpixel((x * 2 + 1, y * 2 + 1), 0)
    name1 = name1 + '.bmp'
    name2 = name2 + '.bmp'
    part1.save(name1)
    part2.save(name2)

    a = cv2.imread(name1, 0)
    a = cv2.resize(a, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Part1", a)
    b = cv2.imread(name2, 0)
    b = cv2.resize(b, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Part2", b)



root = Tk("aa")
global test1
test1 = 0
global test2
test2 = 0
root.title("VisualCryptography")
label30 = Label(root, text="Obraz do podziału na 2 udziały")
label31 = Label(root, text=" ")
label31 = Label(root, text="Nazwa pliku w, którym zostanie zapisany udział nr 1")
label32 = Label(root, text="Nazwa pliku w, którym zostanie zapisany udział nr 2")
label35 = Label(root, text="Nazwa pliku w, którym zostanie zapisany rezultat progowania")
label34 = Label(root, text="Nazwa pliku w, którym zostanie zapisany rezultat deszyfrowania")
label22 = Label(root, text=" ")
label21 = Label(root, text=" ")
label20 = Label(root, text="Kryptografia wizualna")
label1 = Label(root, text="schemat stopnia (2, 2) z użyciem 4 subpikselowej reprezentacji")
label2 = Label(root, text=" ")
label7 = Label(root, text="PROGOWANIE")
label2 = Label(root, text="zamiana obrazu na czarnobiały")
label4 = Label(root, text="UKRYWANIE")
label5 = Label(root, text=" ")
button1 = Button(root, text="Wczytaj obraz i wykonaj", fg="green", command = lambda: button1Action())
entry1 = Entry(root, width = 950)
v = StringVar()
v.set("a default value")
text1 = Text(root, heigh = 5, width = 30)
button2 = Button(root, text="Wczytaj obraz i wykonaj", fg="blue", command = lambda: button2Action())
label6 = Label(root, text="NAKŁADANIE UDZIAŁÓW")
button4 = Button(root, text="Wczytaj udział 1", fg="brown", command = lambda: button4Action())
button5 = Button(root, text="Wczytaj udział 2", fg="brown", command = lambda: button5Action())
label9 = Label(root, text=" ")
text1 = Text(root, heigh = 1, width = 20)
text2 = Text(root, heigh = 1, width = 20)
text3 = Text(root, heigh = 1, width = 20)
text4 = Text(root, heigh = 1, width = 20)
button6 = Button(root, text="Pomoc", fg="red", command = lambda: button6Action())
button7 = Button(root, text="Info", fg="red", command = lambda: button7Action())
button8 = Button(root, text="Wykonaj", fg="brown", command = lambda: button8Action())



label9.pack(side=BOTTOM)
button8.pack(side=BOTTOM)
button5.pack(side=BOTTOM)
button4.pack(side=BOTTOM)
text4.pack(side=BOTTOM)
label34.pack(side=BOTTOM)
label6.pack(side=BOTTOM)
label21.pack(side=BOTTOM)
button2.pack(side=BOTTOM)
text2.pack(side=BOTTOM)
label32.pack(side=BOTTOM)
text1.pack(side=BOTTOM)
label31.pack(side=BOTTOM)
label30.pack(side=BOTTOM)
label4.pack(side=BOTTOM)
label5.pack(side=BOTTOM)
button1.pack(side=BOTTOM)
text3.pack(side=BOTTOM)
label35.pack(side=BOTTOM)
label2.pack(side=BOTTOM)
label7.pack(side=BOTTOM)
label22.pack(side=BOTTOM)
label1.pack(side=BOTTOM)
label20.pack(side=BOTTOM)

button7.pack(side=LEFT)
button6.pack(side=LEFT)
root.mainloop()