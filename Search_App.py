from tkinter import *
from tkinter import messagebox
import wikipedia
class SearchApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Search APP | Developed by Areeba Munir")
        self.root.geometry("1353x700+0+0")
        self.root.config(bg="black")

        title=Label(self.root,text="Simple Search Application",font=("ariel",35,"bold"),bg="black",fg="gold").place(x=0,y=0,relwidth=1)

        self.lbl_word=Label(self.root,text="Search Word",font=("ariel",30,"bold"),bg="black",fg="green").place(x=10,y=100)
        self.var_search=StringVar()
        txt_word=Entry(self.root,textvariable=self.var_search,font=("times new roman",20)).place(x=300,y=110,width=300)

        btn_search=Button(self.root,text="Search",command=self.searchword,font=("times new roman",20,"bold"),bg="brown",fg="black").place(x=620,y=108,height=40,width=150)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",20,"bold"),bg="blue",fg="black").place(x=790,y=108,height=40,width=150)
        btn_enable=Button(self.root,text="Enable Mood",command=self.enable,font=("times new roman",20,"bold"),bg="purple",fg="black").place(x=950,y=108,height=40,width=200)
        btn_disable=Button(self.root,text="Disable",command=self.disable,font=("times new roman",20,"bold"),bg="pink",fg="black").place(x=1170,y=108,height=40,width=180)


        self.lbl_mode=Label(self.root,font=("times new roman",15),bg="#262626",fg="yellow")
        self.lbl_mode.place(x=20,y=170)
        frame1=Frame(self.root,bd=2,relief=RIDGE)
        frame1.place(x=20,y=195,width=1330,heigh=500)

        scrolly=Scrollbar(frame1,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_area=Text(frame1,font=("times new roman",15),yscrollcommand=scrolly.set)
        self.txt_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_area.yview)

    def enable(self):
        self.txt_area.config(state=NORMAL)
        self.lbl_mode.config(text="MODE: ENABLED")

    def disable(self):
        self.txt_area.config(state=DISABLED)
        self.lbl_mode.config(text="MODE: DISABLED")

    def searchword(self):
        if self.var_search.get()=="":
            messagebox.showerror("Error","Search area should not be empty")
        else:
            fetch_data=wikipedia.summary(self.var_search.get())
            self.txt_area.insert('1.0',fetch_data)

    def clear(self):
        self.var_search.set("")
        self.txt_area.delete('1.0',END)
        self.lbl_mode.config(text="")


root=Tk()
obj=SearchApp(root)
root.mainloop()