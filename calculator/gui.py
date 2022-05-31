
from cgitb import text
from optparse import Values
from re import sub
from tkinter import *
from tkinter import ttk
import tkinter

from net_calculator import SubnetAddress

class GraphicInterface():    

    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Subnetting FLSM Calculator GUI")
        self.root.resizable(0,0)
        self.frame = ttk.Frame(self.root, padding = 10)
        self.frame.grid()
        ttk.Label(self.frame, text = "Ingrese una dirección IP").grid(column = 0, row = 0)
        self.entry_ip = ttk.Entry(self.frame).grid(column = 0, row = 1)
        ttk.Label(self.frame, text = "Ingrese la cantidad de subredes a calcular").grid(column = 0, row = 2)
        self.subnet_acount = ttk.Entry(self.frame).grid(column = 0, row = 3)

        ttk.Button(self.frame, text='Calcular', command=self.compute).grid(column=1, row=3)

        self.root.tree=ttk.Treeview(self.frame, height = 10)
        self.root.tree.grid(row=4, column=0, columnspan=5, pady=10, ipady=10)
                
        self.root.tree["columns"]=("Column 2", "Column 3", "Column 4", "Column 5")
        self.root.tree.column("#0", width=170, minwidth=170)
        self.root.tree.column("Column 2", width=170, minwidth=170)
        self.root.tree.column("Column 3", width=170, minwidth=170)
        self.root.tree.column("Column 4", width=170, minwidth=170)
        self.root.tree.column("Column 5", width=170, minwidth=170)
                
        self.root.tree.heading("#0", text="Subred id", anchor=tkinter.CENTER)
        self.root.tree.heading("Column 2", text="Dirección de red", anchor=tkinter.CENTER)
        self.root.tree.heading("Column 3", text="Primera ip", anchor=tkinter.CENTER)
        self.root.tree.heading("Column 4", text="Última ip", anchor=tkinter.CENTER)
        self.root.tree.heading("Column 5", text="Broadcast", anchor=tkinter.CENTER)

    def execute(self):
        self.root.mainloop()

    def compute(self):
        subnet_address = SubnetAddress(ip=self.entry_ip.get(), subnetworks=self.subnet_acount.get())
        set_values = subnet_address.set_subnetworks()
        for i in set_values:
            self.root.tree.insert("", 'end', values=(i))        
