from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Rooms")
window.geometry("500x500")
#window.resizable(0,0)

uczestnicy = []
#m=5
def button_adding():
        #n=m
        global uczestnicy
        uczestnicy.append(str(entry.get()) + '\n')
        label3.configure(text= uczestnicy)
        #label4 = tk.Label( window, text = uczestnicy )
        #label4.grid(row=n, column=0)
        #n+=1

def button_delating():
        global uczestnicy
        uczestnicy.remove(str(entry.get()))
        label3.configure(text= uczestnicy)


label = tk.Label( window, text = "Dodaj osobę do listy:" )
label.grid(row=0, column=0)

entry = tk.Entry(window, fg="black", bg="yellow", width=30)
entry.grid(row=0, column=1) 

button_add = Button(window, text="Add", fg="black", width=12, height=1, bd=0, bg="azure", cursor="hand2", command=lambda: button_adding())
button_add.grid(row=0, column=2, padx=1, pady=1)
button_del = Button(window, text="Del", fg="black", width=12, height=1, bd=0, bg="azure", cursor="hand2", command=lambda: button_delating())
button_del.grid(row=0, column=3, padx=1, pady=1)

label1 = tk.Label( window, text = "" )
label1.grid(row=1, column=0)

label2 = tk.Label( window, text = "Lista uczestników:" )
label2.grid(row=2, column=0)

label3 = tk.Label( window, text = uczestnicy )
label3.grid(row=3, column=0)





window.mainloop()