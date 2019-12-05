from tkinter import *
from tkinter.simpledialog import *
def ft_color() :
    if ftcolor.get() == 1 :
        la_result.configure(fg="white")
    elif ftcolor.get() == 2 :
        la_result.configure(fg="yellow")
    elif ftcolor.get()==3 :
        la_result.configure(fg="red")

def radio_func() :
    if var_lang.get() == 1 :
        la_result.configure(bg="blue")
    elif var_lang.get() == 2 :
        la_result.configure(bg="black")
    elif var_lang.get() ==3 :
        la_result.configure(bg="yellow")

def inpput() :
    global i
    i=0
    if(i==0) :
        input_str = askstring("String", "문자를 입력하세요")
    la_result.configure(text=input_str)


def func_exit() :
    win.quit()
    win.destroy()



win = Tk()
win.title("String Viewer")
win.geometry("200x140")

#menu
main_menu = Menu(win)
win.config(menu=main_menu)

menu1=Menu(main_menu)
main_menu.add_cascade(label="File",menu=menu1)

menu1.add_command(label="input String",command=inpput)
menu1.add_separator()
menu1.add_command(label="Exit",command=func_exit)



var_lang = IntVar()
ftcolor=IntVar()



bg_name=Label(win,text="<배경색>")
bg_name.grid(row=0,column=0)
ft_name=Label(win,text="<글자색>")
ft_name.grid(row=0,column=1)

#radio button
rb1=Radiobutton(win,text="blue",variable=var_lang,value=1,command=radio_func)
rb1.grid(row=1,column=0)
rb2=Radiobutton(win,text="black",variable=var_lang,value=2,command=radio_func)
rb2.grid(row=2,column=0)
rb3=Radiobutton(win,text="yellow",variable=var_lang,value=3,command=radio_func)
rb3.grid(row=3,column=0)

fc1=Radiobutton(win,text="white",variable=ftcolor,value=1,command=ft_color)
fc1.grid(row=1,column=1)
fc2=Radiobutton(win,text="yellow",variable=ftcolor,value=2,command=ft_color)
fc2.grid(row=2,column=1)
fc3=Radiobutton(win,text="red",variable=ftcolor,value=3,command=ft_color)
fc3.grid(row=3,column=1)

la_result=Label(win)
la_result.grid(row=4, columnspan=2)

win.mainloop()