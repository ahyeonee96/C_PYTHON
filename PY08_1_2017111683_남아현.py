from tkinter import *

def before_func() :
    global i
    if(i==0) :
        i=4
    else :
        i-=1
    image = PhotoImage(file=lst[i])
    la_img.configure(image=image)
    la_img.image=image

def after_func() :
    global i
    if(i==4) :
        i=0
    else :
        i+=1
    image = PhotoImage(file=lst[i])
    la_img.configure(image=image)
    la_img.image=image

def before_func1(event) :
    global i
    if(i==0) :
        i=4
    else :
        i-=1
    image = PhotoImage(file=lst[i])
    la_img.configure(image=image)
    la_img.image=image

def after_func1(event) :
    global i
    if(i==4) :
        i=0
    else :
        i+=1
    image = PhotoImage(file=lst[i])
    la_img.configure(image=image)
    la_img.image=image

win = Tk()
win.title("사진 앨범 보기")

lst=["jeju1.gif","jeju2.gif","jeju3.gif","jeju4.gif","jeju5.gif"]\



btn1 = Button(win,text="<<이전",command=before_func)
btn1.grid(row=0,column=0)

btn2 = Button(win,text="다음>>",command=after_func)
btn2.grid(row=0,column=1)

i=0
image=PhotoImage(file=lst[i])
la_img=Label(win,image=image)
la_img.grid(row=1,columnspan=2)

win.bind("<Key>",before_func1)
win.bind("<Right>",after_func1)
win.mainloop()