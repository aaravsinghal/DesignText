import random
from tkinter import *
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)
fonsizlis=[]
for i in range(101):
    fonsizlis.append(i)
fonsizlis=fonsizlis[::-1]
colorlist="green blue red orange white violet yellow black".split()
colorlist2="Green,Blue,Red,Orange,White,Violet,Yellow,Random".split(",")
colorlist3="Green,Blue,Red,Orange,White,Violet,Yellow,Black".split(",")
root=Tk()
root.state("zoomed")
inpval=StringVar()
inpval2=inpval.get()
inpfr=Frame(root)
Label(inpfr, text="Enter text  ", font="jhn 30 bold").grid(row=0,column=0)
inpu=Entry(inpfr, textvariable=inpval, font="gfgggv 30 bold", relief=SUNKEN, borderwidth=5)
inpu.grid(row=0,column=1)
Label(inpfr, text="                                                            ").grid(row=0,column=2)
inpfr.pack()
lett=Frame(root, relief=SUNKEN)
def write():
    global lett
    lett.destroy()
    lett=None
    lett=Frame(root)
    global inpval2
    inpval2=inpval.get()
    count=0
    if fontstval.get()!="Normal" and colval.get()!="Random":
        if fontstval.get()=="Italic":
            for i in list(inpval2):
                Label(lett, text=i, fg=colval.get(), font="{} {} {}".format(fontval.get(),fontsival.get(),(fontstval.get()).lower()), bg=bgcval.get(), relief=RAISED, padx=30).grid(row=0, column=count)
                count+=1
        else:
            for i in list(inpval2):
                Label(lett, text=i, fg=colval.get(), font="{} {} {}".format(fontval.get(),fontsival.get(),(fontstval.get()).lower()), bg=bgcval.get(), relief=RAISED).grid(row=0, column=count)
                count+=1
    elif colval.get()!="Random":
        for i in list(inpval2):
            Label(lett, text=i, fg=colval.get(), font="{} {}".format(fontval.get(),fontsival.get()), bg=bgcval.get(), relief=RAISED).grid(row=0, column=count)
            count+=1
    elif fontstval.get()=="Normal":
        for i in list(inpval2):
            tr=colorlist[random.randint(0,len(colorlist)-1)]
            if tr=="".join(bgcval.get().lower().split()):
                write()
                return
            Label(lett, text=i, fg=tr, font="{} {} {}".format(fontval.get(),fontsival.get(),(fontstval.get()).lower()), bg=bgcval.get(), relief=RAISED).grid(row=0, column=count)
            count+=1
    else:
        for i in list(inpval2):
            tr=colorlist[random.randint(0,len(colorlist)-1)]
            if tr=="".join(bgcval.get().lower().split()):
                write()
                return
            Label(lett, text=i, fg=tr, font="{} {}".format(fontval.get(),fontsival.get()), bg=bgcval.get(), relief=RAISED).grid(row=0, column=count)
            count+=1
    lett.pack()
lett.pack()
Button(root, text="Design", command=write, font="hnn 15 bold",borderwidth=5).pack(pady=20)
fontval=StringVar()
fontandsize=Frame(root)
fontfr=Frame(fontandsize)
Label(fontfr, text="            Font: ", font="consolas").grid(column=0, row=0)
font=Spinbox(fontfr, values=["Forte", "Consolas", "Normal", "Algerian"], textvariable=fontval)
font.grid(row=0, column=1)
Label(fontfr, text="                                      ").grid(row=0, column=3)
fontsival=StringVar()
fontsifr=Frame(fontandsize)
Label(fontsifr, text="       Font Size: ", font="consolas").grid(column=0, row=0)
fontsi=Spinbox(fontsifr, values=fonsizlis, textvariable=fontsival)
fontsival.set(60)
fontsi.grid(row=0, column=1)
Label(fontsifr, text="                                      ").grid(row=0, column=3)
fontstval=StringVar()
fontstfr=Frame(fontandsize)
Label(fontstfr, text="           Style: ", font="consolas").grid(column=0, row=0)
fontst=Spinbox(fontstfr, values=["Normal", "Bold", "Italic"], textvariable=fontstval)
fontstval.set("Normal")
fontst.grid(row=0, column=1)
Label(fontstfr, text="                                      ").grid(row=0, column=3)
colval=StringVar()
colfr=Frame(fontandsize)
Label(colfr, text="     Text Colour: ", font="consolas").grid(column=0, row=0)
col=Spinbox(colfr, values=colorlist2, textvariable=colval)
colval.set("Random")
col.grid(row=0, column=1)
Label(colfr, text="                                      ").grid(row=0, column=3)
bgcval=StringVar()
bgcfr=Frame(fontandsize)
Label(bgcfr, text="Highlight Colour: ", font="consolas").grid(column=0, row=0)
bgc=Spinbox(bgcfr, values=colorlist3, textvariable=bgcval)
bgcval.set("Black")
bgc.grid(row=0, column=1)
Label(bgcfr, text="                                      ").grid(row=0, column=3)
fontfr.pack()
fontsifr.pack()
fontstfr.pack()
colfr.pack()
bgcfr.pack()
fontandsize.pack(pady=20)
root.mainloop()
