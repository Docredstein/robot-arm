import tkinter
import tkinter.filedialog
import tkinter.messagebox
import serial 
import serial.tools.list_ports
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
debug = open("debug.txt","a")
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
    port = port.rstrip("\n")
    #speed.replace("\n","")
    #NServo.replace("\n","")
print(f"{port}\n{speed}")
try :
    con = serial.Serial(port, speed)
except :
    print("connection error")

class Pos() :
        def __init__(self,n,x,y) :
            self.n = n
            self.x = x
            self.y = y
            self.pos = 0
            self.bt = tkinter.Button(master, command=self.press, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text=f"pos {n}")
            self.bt.place(relx=x,rely=y,anchor=tkinter.W)
        def press(self) :
            if self.pos == 0 :
                out = []
                out.append(a.get())
                out.append(b.get())
                out.append(c.get())
                out.append(d.get())
                out.append(e.get())
                out.append(f.get())
                self.pos = out
                print(self.pos)
            else :
                print(self.pos)
                setSlider(self.pos)
                SendCom(self.pos)

        def clear(self) :
            self.pos = 0




master = tkinter.Tk()
master.title('Contrôle bras SI 2020')
master.iconbitmap(rf"{dir_path}\icons.ico")
master.geometry("800x800")
master.configure(background=r'#0f0b0d')
def start() :
    inp = tkinter.Toplevel()
    inp.title("Settings")
    inp.geometry("230x250")
    inp.configure(background=r'#0f0b0d')
    prec = tkinter.Button(inp,fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="charger les anciens par.")
    prec.place(relx=0.375,rely=0.9,anchor=tkinter.W)
    liste = tkinter.Listbox(inp,fg =fg, background=bg,relief=tkinter.RIDGE,height=3)
    x = 0
    portCom = ListPortCom()
    print(portCom)
    for i in portCom :
        liste.insert(x,i)
        x=x+1
    liste.yview()
    liste.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)
    saveBB = tkinter.Button(inp,fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="enregistrer")
    saveBB.place(relx=0.075,rely=0.9,anchor=tkinter.W)
    debounceEntry = tkinter.Entry (inp,highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE, text="temps",foreground=fg) 
    debounceEntry.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    bauds= tkinter.Entry (inp,highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE, text="bauds",foreground=fg) 
    bauds.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
    baudsLabel = tkinter.Label(inp,text = "bauds :", fg =fg, highlightbackground=highlightbackground,background=background,relief=tkinter.FLAT,activebackground=highlightbackground)
    baudsLabel.place(relx=0.1,rely=0.6,anchor=tkinter.CENTER)
    debounceLabel = tkinter.Label(inp,text = "délai :", fg =fg, highlightbackground=highlightbackground,background=background,relief=tkinter.FLAT,activebackground=highlightbackground)
    debounceLabel.place(relx=0.1,rely=0.5,anchor=tkinter.CENTER)
    msLabel = tkinter.Label(inp,text = "ms", fg =fg, highlightbackground=highlightbackground,background=background,relief=tkinter.FLAT,activebackground=highlightbackground)
    msLabel.place(relx=0.85,rely=0.5,anchor=tkinter.CENTER)
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
def trjPlay() :
    global trj 

    perf = time.time()
    if len(trj) !=0 :
        try :
            if len(trj[0]) !=0 :
                for i in range(len(trj)) :
                    print(trj[i])
                    if trj[i] == trj[0] or trj[i][6]==0:
                        print(trj[i])
                        setSlider(trj[i])
                        print(f"étape {i} : {trj[i]}")
                        stripSend(trj[i])
                    else :
                        
                        current = [0,0,0,0,0,0,0]
                        exectime=0
                        a = lambda x,y : round((((trj[i][y]-trj[i-1][y])/trj[i][6])*x)+trj[i-1][y])
                        for x in range(1,round((trj[i][6]+1)/10)) :
                            if (0.01-exectime) >0 :
                                sleep(0.01-exectime)
                            timen = time.time()
                            for j in range(6) : 
                                
                                current[j] = a(x,j)
                                #print("---------------")
                            current[6]=x
                            #print(current)
                            '''for w in current :
                                debug.write(f'{w};')
                            debug.write('\n')'''
                            setSlider(current)
                            stripSend(current)
                            exectime=time.time()-timen

                        

        except TypeError :
            '''setSlider(trj)
            SendCom(i)'''
            pass
    else :
        #print('trajectoire vide')
        tkinter.messagebox.showerror(title="erreur",message="trajectoire vide")
    print(time.time()-perf)
    print(f'{(((time.time()-perf-15)/15)*100)} %')
    print(exectime)          
def posClear():
    pos1.clear()
    pos2.clear()
    pos3.clear()
    pos4.clear()
    pos5.clear()
    pos6.clear()
    pos7.clear()
    pos8.clear()
    pos9.clear()
def ListPortCom():
    ports = serial.tools.list_ports.comports()
    out=[]
    for port, desc, hwid in sorted(ports):
        out.append(port)
    return out
def stripSend(list)  :
    out = []
    for i in range(len(list)) :
        if i<5 : 
            out.append(i)
        else :
            pass
    SendCom(out)
def trjRec():
    global trj
    with open("out.trj","a") as file:
        file.write("-------------\n")
        for x in trj :
            for y in x :
                file.write(f"{y};")
            file.write("\n")
def trjUnload() :
    global trj
    trj = []
    print(trj)
def trjLoad():
    path = tkinter.filedialog.askopenfilename()
    global trj
    print(path)
    trj = []
    mid = []
    nbr = ""
    if path != "" :
        with open(path,"r") as file :
            line = file.readlines()
            for i in line :
                for j in i :
                    if j == ";" :
                        nbr = int(nbr)
                        mid.append(nbr)
                        nbr = ""
                    elif j == "-" :
                        pass
                    else : 
                        nbr = nbr +j
                if mid != [] :
                    trj.append(mid)
                mid = []
            print(trj)
    else : 
        print("opération annulée")

    pass
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
def setSlider(list) :
    a.set(list[0])
    b.set(list[1])
    c.set(list[2])
    d.set(list[3])
    e.set(list[4])
    f.set(list[5])


a = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground, command = test)
a.pack()
a.place(relx=0.5, rely=4/30, anchor=tkinter.CENTER)
t1 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 1")
t1.pack()
t1.place(relx=0.02,rely=4/30,anchor=tkinter.W)
b = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
b.pack()
b.place(relx=0.5, rely=9/30, anchor=tkinter.CENTER)
t2 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 2")
t2.pack()
t2.place(relx=0.02,rely=9/30,anchor=tkinter.W)
c = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
c.pack()
c.place(relx=0.5, rely=14/30, anchor=tkinter.CENTER)
t3 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 3")
t3.pack()
t3.place(relx=0.02,rely=14/30,anchor=tkinter.W)
d = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
d.pack()
d.place(relx=0.5, rely=19/30, anchor=tkinter.CENTER)
t4 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 4")
t4.pack()
t4.place(relx=0.02,rely=19/30,anchor=tkinter.W)
e = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg,highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
e.pack()
e.place(relx=0.5, rely=23.5/30, anchor=tkinter.CENTER)

t5 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 5")
t5.pack()
t5.place(relx=0.02,rely=23.5/30,anchor=tkinter.W)

f = tkinter.Scale(master, from_=0, to=180,tickinterval=20, length=600, orient="horizontal",background=bg,highlightthickness=2,fg=fg, highlightbackground=highlightbackground,relief=tkinter.RIDGE,activebackground=highlightbackground,command = test)
f.pack()
f.place(relx=0.5, rely=28/30, anchor=tkinter.CENTER)

t6 = tkinter.Label(master,fg=fg,background=background, text = "Servo n° 6")
t6.pack()
t6.place(relx=0.02,rely=28/30,anchor=tkinter.W)

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

trjLoBt = tkinter.Button(master, command=trjLoad, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="charger une trajectoire"  )
trjLoBt.place(relx=0.64,rely=0.06,anchor=tkinter.W)

trjUnlBt = tkinter.Button(master, command=trjUnload, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="décharger une trajectoire"  )
trjUnlBt.place(relx=0.805,rely=0.06,anchor=tkinter.W)
#trjUnlBt =Bt("décharger la trajectoire",0.76,0.06,tkinter.W,trjUnload())

posClBt = tkinter.Button(master, command=posClear, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="RàZ pos")
posClBt.place(relx=0.46,rely=0.06,anchor=tkinter.W)

BtSetting = tkinter.Button(master, command=start, fg =fg, highlightbackground=highlightbackground,background=bg,relief=tkinter.RIDGE,activebackground=highlightbackground, text="paramètre")
BtSetting.place(relx=0.545,rely=0.06,anchor=tkinter.W)
pos1 = Pos(1,0.01,0.06)
pos2 = Pos(2,0.06,0.06)
pos3 = Pos(3,0.11,0.06)
pos4 = Pos(4,0.16,0.06)
pos5 = Pos(5,0.21,0.06)
pos6 = Pos(6,0.26,0.06)
pos7 = Pos(7,0.31,0.06)
pos8 = Pos(8,0.36,0.06)
pos9 = Pos(9,0.41,0.06)





tkinter.mainloop()
SendCom(endPos) 