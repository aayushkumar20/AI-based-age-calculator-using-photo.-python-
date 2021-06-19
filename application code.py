from tkinter import *
from datetime import date

root=Tk()
root.geometry("700*500")
root.title("AI Based age calculator using image by-(aayush)")
#new=Label(root,bg="#D5C6FF")  
photo=PhotoImage(file="********.png")
myimage=Label(image=photo)
myimage.grid(row=0,column=1)

today=str(date.today())   
list_today=today.split("-")  

def calculateAge():
  today=date.today()
  birthDate=date(int(yearEntry.get()),
  int(monthEntry.get()),int(dayEntry.get())
  age=today.year-birthDate.year-((today.month,today.day)<(bithDate.month,BirthDate.day))
  Label(text=f"{nameValue.get()} your age is {age}").grid(row=6,column=1)
                 
  
Label(text="Name".grid(row=1,column=0,padx=90)
Label(text="Year".grid(row=2,column=0)
Label(text="Month".grid(row=3,column=0)
Label(text="Day".grid(row=4,column=0)
nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar() 
nameEntry=Entry(root,textvariable=nameValue)
yearEntry=Entry(root,textvariable=yearValue)
monthEntry=Entry(root,textvariable=monthValue)
dayEntry=Entry(root,textvariable=dayValue)
nameEntry.grid(row=1,column=1,pady=10)
yearEntry.grid(row=2,column=1,pady=10)
monthEntry.grid(row=3,column=1,pady=10)
dayEntry.grid(row=4,column=1,pady=10)
.grid(row=5,column=1,pady=10)

 root.mainloop()
                 
     

