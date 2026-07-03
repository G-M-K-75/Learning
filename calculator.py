from tkinter import *

global scvalue


def click(event):
    text = event.widget.cget("text")
    print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        scvalue.set(value)
    elif text =="c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("280x450")
root.title("GMK Calculator")
root.configure(bg = "powderblue")
root.wm_iconbitmap(r"E:\EDUCATION\ML Practice\Learning\GMK.ico")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable = scvalue, font = "arialblack 20 bold", bg = "black", fg = "lightgrey")
screen.pack(fill= X, ipadx=7,pady =6, padx = 12)


f = Frame(root, bg = "powderblue")
B = Button(f, text = "c",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "/",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "%",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "*",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "powderblue")
B = Button(f, text = "1",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue")
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "2",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "3",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 11, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "=",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 8, side = LEFT)
B.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "powderblue")
B = Button(f, text = "4",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue")
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "5",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "6",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "+",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 11, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "powderblue")
B = Button(f, text = "7",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue")
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "8",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "9",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "-",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "powderblue")
B = Button(f, text = "0",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "00",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = "000",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
B = Button(f, text = ".",font ="arialblack 20 bold", bg = "lightgrey", fg = "darkblue",width = 2,height = 1)
B.pack(padx = 12, pady = 12, side = LEFT)
B.bind("<Button-1>", click)
f.pack()
root.mainloop()