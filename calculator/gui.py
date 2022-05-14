
from tkinter import *
from tkinter import ttk
import tkinter

root = Tk()
root.title("Subnetting FLSM Calculator GUI")
root.resizable(0,0)
frame = ttk.Frame(root, padding = 10)
frame.grid()
ttk.Label(frame, text = "Ingrese una dirección IP").grid(column = 0, row = 0)
ttk.Entry(frame).grid(column = 0, row = 1)
ttk.Label(frame, text = "Ingrese la cantidad de subredes a calcular").grid(column = 0, row = 2)
ttk.Entry(frame).grid(column = 0, row = 3)

root.tree=ttk.Treeview(frame, height = 10)
root.tree.grid(row=4, column=0, columnspan=5, pady=10, ipady=10)
        
root.tree["columns"]=("Column 2", "Column 3", "Column 4", "Column 5")
root.tree.column("#0", width=170, minwidth=170)
root.tree.column("Column 2", width=170, minwidth=170)
root.tree.column("Column 3", width=170, minwidth=170)
root.tree.column("Column 4", width=170, minwidth=170)
root.tree.column("Column 5", width=170, minwidth=170)
        
root.tree.heading("#0", text="Subred id", anchor=tkinter.CENTER)
root.tree.heading("Column 2", text="Dirección de red", anchor=tkinter.CENTER)
root.tree.heading("Column 3", text="Primera ip", anchor=tkinter.CENTER)
root.tree.heading("Column 4", text="Última ip", anchor=tkinter.CENTER)
root.tree.heading("Column 5", text="Broadcast", anchor=tkinter.CENTER)

root.mainloop()


