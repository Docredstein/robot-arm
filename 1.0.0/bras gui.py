import tkinter
import serial 
from time import sleep
import time
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
endPos = [76, 145, 176, 52, 151, 20]
lastMillis = 0
delay=0
background = "#0f0b0d"
fg = "#ffffff"
highlightbackground = "#bf2431"
bg = "#8C1f28"
trj = []
if input("new setting ? Y/N :").lower() == "y" :
    port = input("port :")
    speed = int(input("débit :"))
    debounce = int(input("délai entre 2 paquet (ms) :"))
    file = open("setting.txt",'w') 
    file.write(f"{speed}\n{port}\n{debounce}")
    file.close()
else :
    file = open("setting.txt", "r") 
    speed = int(file.readline())
    port = file.readline()
    debounce = int(file.readline())
    file.close()
    port.replace("\n","")
    #speed.replace("\n","")
    #NServo.replace("\n","")
print(f"{port}\n{speed}")
try :
    con = serial.Serial(port, speed)
except :
    print("connection error")

master = tkinter.Tk()
master.title('Contrôle bras SI 2020')
master.iconbitmap(rf"{dir_path}\icons.ico")
master.geometry("800x800")
master.configure(background=r'#0f0b0d')

def save() :
    file = open('Saved.txt',"a")
    file.write(f"{test(0)}\n")
    file.close()
def SendCom(list) :
    global lastMillis
    ms = time.time()*1000.0
    if (ms-lastMillis)>debounce :
        print("sending data")
        con.write(bytes([254]))
        print(bytes([254]))
        for i in list :
            con.write(bytes([int(i)]))
            print(bytes([int(i)]))
        con.write(bytes([255]))
        print(bytes([255]))
        lastMillis = time.time()*1000.0
def trjExt() :
    global trj
    out = []
    out.append(a.get())
    out.append(b.get())
    out.append(c.get())
    out.append(d.get())
    out.append(e.get())
    out.append(f.get())
    try :
        out.append(int(delay.get()))
    except :
        out.append(0)
    
    trj.append(out)
    print(trj)
def trjPlay(trj) :
    pass
def trjRec():
    global trj
    with open("out.trj","a") as file:
        file.write("-------------\n")
        for x in trj :
            for y in x :
                file.write(f"{y};")
            file.write("\n")

def test(value):
    #print("test")
    #print(value)
    out = []
    out.append(a.get())
    out.append(b.get())
    out.append(c.get())
    out.append(d.get())
    out.append(e.get())
    out.append(f.get())
    print(out)
    SendCom(out)
    return out
a = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground, command = test)
a.pack()
a.place(relx=0.5, rely=1/12, anchor=tkinter.CENTER)
t1 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 1")
t1.pack()
t1.place(relx=0.02,rely=1/12,anchor=tkinter.W)
b = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
b.pack()
b.place(relx=0.5, rely=3/12, anchor=tkinter.CENTER)
t2 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 2")
t2.pack()
t2.place(relx=0.02,rely=3/12,anchor=tkinter.W)
c = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
c.pack()
c.place(relx=0.5, rely=5/12, anchor=tkinter.CENTER)
t3 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 3")
t3.pack()
t3.place(relx=0.02,rely=5/12,anchor=tkinter.W)
d = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
d.pack()
d.place(relx=0.5, rely=7/12, anchor=tkinter.CENTER)
t4 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 4")
t4.pack()
t4.place(relx=0.02,rely=7/12,anchor=tkinter.W)
e = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
e.pack()
e.place(relx=0.5, rely=9/12, anchor=tkinter.CENTER)

t5 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 5")
t5.pack()
t5.place(relx=0.02,rely=9/12,anchor=tkinter.W)

f = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg, highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
f.pack()
f.place(relx=0.5, rely=11/12, anchor=tkinter.CENTER)

t6 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 6")
t6.pack()
t6.place(relx=0.02,rely=11/12,anchor=tkinter.W)

saveB = tkinter.Button(master, command=save, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="enregistrer la position"  )
saveB.place(relx=0.4,rely=0.02,anchor=tkinter.CENTER)
#saveB.pack()

delay = tkinter.Entry (master,highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE, text="enregistrer la position",foreground=fg) 
delay.place(relx=0.12,rely=0.02,anchor=tkinter.W)

delayLabel = tkinter.Label(master,text = "temporisation :", fg =fg, highlightbackground=highlightbackground,background=background,relief=tkinter.FLAT,activebackground=highlightbackground)
delayLabel.place(relx=0.01,rely=0.02,anchor=tkinter.W)
ms= tkinter.Label(master,text = "ms", fg =fg, highlightbackground=highlightbackground,background=background,relief=tkinter.FLAT,activebackground=highlightbackground)
ms.place(relx=0.27,rely=0.02,anchor=tkinter.W)
trjRecBt = tkinter.Button(master, command=trjRec, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="enregistrer la trajectoire"  )
trjRecBt.place(relx=0.48,rely=0.02,anchor=tkinter.W)

trjExtBt = tkinter.Button(master, command=trjExt, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="ajouter la pos. a la trj."  )
trjExtBt.place(relx=0.65,rely=0.02,anchor=tkinter.W)

trjPlBt = tkinter.Button(master, command=trjPlay, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="faire la trajectoire"  )
trjPlBt.place(relx=0.81,rely=0.02,anchor=tkinter.W)


tkinter.mainloop()
SendCom(endPos) 