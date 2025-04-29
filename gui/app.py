from gui.events import simulate_click
import tkinter as tk

def start_gui():
    window = tk.Tk()
    window.title('Kinetics simulator')
    window.geometry('600x400')
    labels = ['Reaction order', 'Initial concentration', 'Reaction rate constant', 'Time']
    input_fields = {}

    for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text, font=30)
        label.grid(row=i, column=0, pady=5, padx=5,sticky='w')

        if label_text == 'Reaction order':
            var = tk.StringVar(window)
            var.set('0')
            entry = tk.OptionMenu(window, var, '0', '1', '2')
        else: 
            var = tk.StringVar(window) 
            entry = tk.Entry(window, textvariable=var)
        
        entry.grid(row=i, column=1, pady=5, padx=5)
        input_fields[label_text] = var

    button = tk.Button(window, text='Simulate', command=lambda: simulate_click(input_fields))
    button.grid(row=4, column=1)

    window.mainloop()