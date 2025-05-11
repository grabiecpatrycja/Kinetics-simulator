from gui.events import basic_simulate_click
import tkinter as tk

def build_basic_tab(parent):
    labels = {
        'Reaction order': '',
        'Initial concentration': 'mol/L',
        'Reaction rate constant': '',
        'Time': 's'}
    
    input_fields = {}

    for i, (label_text, unit) in enumerate(labels.items()):
        label = tk.Label(parent, text=label_text, font=30)
        label.grid(row=i, column=0, pady=5, padx=5, sticky='w')

        if label_text == 'Reaction order':
            var = tk.IntVar()
            var.set(0)
            entry = tk.OptionMenu(parent, var, 0, 1, 2)
        else: 
            var = tk.DoubleVar(value=0.0) 
            entry = tk.Entry(parent, textvariable=var)
        
        entry.grid(row=i, column=1, pady=5, padx=5)
        input_fields[label_text] = var

        unit_label = tk.Label(parent, text=unit)
        unit_label.grid(row=i, column=2, pady=5, padx=5, sticky='w')

    button = tk.Button(parent, text='Simulate', command=lambda: basic_simulate_click(input_fields))
    button.grid(row=4, column=1)