from gui.basic_tab import build_basic_tab
from gui.temperature_tab import build_temperature_tab
import tkinter as tk
from tkinter import ttk

def start_gui():
    window = tk.Tk()
    window.title('Kinetics simulator')
    window.geometry('600x400')
    
    notebook = ttk.Notebook(window)
    notebook.pack(expand=True, fill='both')

    tab_basic = tk.Frame(notebook)
    notebook.add(tab_basic, text='Basic Reaction')

    tab_temp = tk.Frame(notebook)
    notebook.add(tab_temp, text='Temperature Effecr')

    build_basic_tab(tab_basic)
    build_temperature_tab(tab_temp)

    window.mainloop()