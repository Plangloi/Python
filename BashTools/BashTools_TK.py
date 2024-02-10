import os
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


mainwindow = tb.Window(themename="cyborg")


mainwindow.title("Bash Tool")
mainwindow.iconbitmap('image/codemy.ico')
mainwindow.geometry('500x350')

counter = 0
def changer():
        my_label2.config(text="ls")
        os.system('ls -la')
           
#create Label
my_label1 = tb.Label(text="User Tools",font=("Helvertica", 10), 
        bootstyle="danger")
        
my_label2 = tb.Label(text="Label2",font=("Helvertica", 28), 
        bootstyle="danger")

# -------
my_label3 = tb.Label(mainwindow, text="Combo Box 1",font=("Helvertica", 10))
my_label3.pack(pady=30)

#dropdown option
def clicker():
        my_label4.config(text=f"You click {my_combo.get()}!") 

def click_bind(e):
        my_label4.config(text=f"You click {my_combo.get()}!") 


Tools = ["admin_Tools", "Nmap", "SSH", "Network", "Processus", "Monitoring", "TBC"]
my_list1 = tb.Combobox(mainwindow, bootstyle="success", values=Tools)
my_list1.pack(pady=20)
# my_list1.current(0) #start with x menu
# bind comdo box
my_list1.bind("<<ComboboxSelected>>", click_bind)

my_button = tb.Button(mainwindow, text="Clicker ici", command=clicker, bootstyle="danger")
my_button.pack(pady=20)


#Position
my_label1.place(x=10, y=5)
my_label2.pack(pady=5)

#button 1
my_button = tb.Button(text="ls -la",
        bootstyle="success, outline", command=changer)
my_button.place(x=10, y=30)

        






mainwindow.mainloop()