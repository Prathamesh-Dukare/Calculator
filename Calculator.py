from tkinter import *
root=Tk()
root.geometry('265x365')
root.title("My Calculator")
root.wm_iconbitmap('calci.ico')
root.configure(background='grey')
def click(event):
    text=event.widget.cget('text')
 
    if(text=="="):
        if(scval.get().isdigit()):
            scval.set(scval.get())
            sc.update()
        elif('%' in scval.get()):
            str=scval.get()
            list=str.split(' ')
            scval.set(f'{float(list[0])/100}')
            sc.update()

        elif('1/x' in scval.get()):
            str=scval.get()
            list=str.split('1/x')
            a=float(list[0])
            scval.set(f'{a**-1}')
            sc.update()
 
        else:
            try:
                scval.set(eval(scval.get()))
                sc.update()
            except (SyntaxError,ZeroDivisionError,NameError):
                scval.set('Error')

    elif(text=='C'):
        scval.set('')
        sc.update()
    else:
        scval.set(scval.get()+text)
        sc.update()

scval=StringVar()
scval.set('')
sc=Entry(root,textvariable=scval,font='lucida 17 bold')
sc.pack(padx=10,pady=10,ipadx=5,ipady=5)

f1=Frame(root,bg='grey')
b=Button(f1,text="7",font='lucida 19 bold',padx=9,pady=4,relief=SUNKEN)
b.grid(row=0,column=0,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="8",font='lucida 19 bold',padx=9,pady=4.4,relief=SUNKEN)
b.grid(row=0,column=1,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="9",font='lucida 19 bold',padx=9,pady=4.2,relief=SUNKEN)
b.grid(row=0,column=2,padx=0,pady=0)
b.bind('<Button-1>',click)

b=Button(f1,text="4",font='lucida 19 bold',padx=8.5,pady=5,relief=SUNKEN)
b.grid(row=1,column=0,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="5",font='lucida 19 bold',padx=9.6,pady=4.4,relief=SUNKEN)
b.grid(row=1,column=1,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="6",font='lucida 19 bold',padx=9.4,pady=5,relief=SUNKEN)
b.grid(row=1,column=2,padx=0,pady=0)
b.bind('<Button-1>',click)

b=Button(f1,text="1",font='lucida 19 bold',padx=9,pady=5,relief=SUNKEN)
b.grid(row=2,column=0,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="2",font='lucida 19 bold',padx=10,pady=5,relief=SUNKEN)
b.grid(row=2,column=1,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="3",font='lucida 19 bold',padx=9.2,pady=5,relief=SUNKEN)
b.grid(row=2,column=2,padx=0,pady=0)
b.bind('<Button-1>',click)

b=Button(f1,text=".",font='lucida 19 bold',padx=12.2,pady=4,relief=SUNKEN)
b.grid(row=3,column=0,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="0",font='lucida 19 bold',padx=9.6,pady=4.4,relief=SUNKEN)
b.grid(row=3,column=1,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="/",font='lucida 19 bold',padx=13,pady=4,relief=SUNKEN)
b.grid(row=3,column=2,padx=0,pady=0)
b.bind('<Button-1>',click)

b=Button(f1,text="+",font='lucida 22 bold',padx=10,pady=0.4,relief=SUNKEN)
b.grid(row=0,column=3,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="-",font='lucida 22 bold',padx=13.4,pady=1.38,relief=SUNKEN)
b.grid(row=1,column=3,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="*",font='lucida 17 bold',padx=14,pady=7,relief=SUNKEN)
b.grid(row=2,column=3,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="=",font='lucida 19 bold',fg='green',padx=13.3,pady=5,relief=SUNKEN)
b.grid(row=3,column=3,padx=0,pady=0)
b.bind('<Button-1>',click)

b=Button(f1,text="^",font='lucida 19 bold',padx=8.2,pady=3.8,relief=SUNKEN)
b.grid(row=5,column=0,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="1/x",font='lucida 17 bold',padx=2.7,pady=7,relief=SUNKEN)
b.grid(row=5,column=1,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text=" %",font='lucida 19 bold',padx=6.6,pady=4.3,relief=SUNKEN)
b.grid(row=5,column=2,padx=0,pady=0)
b.bind('<Button-1>',click)
b=Button(f1,text="C",font='lucida 19 bold',fg='red',padx=12,pady=4,relief=SUNKEN)
b.grid(row=5,column=3,padx=0,pady=0)
b.bind('<Button-1>',click)

f1.pack()
root.mainloop()
 
 