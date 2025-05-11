from tkinter import messagebox
from gui.inputs import validate_user_inputs, basic_schema, temperature_schema
from core.kinetisc import calculate_k_arrhenius
from core.logic import simulate

def basic_simulate_click(input_fields):
    try:
        cleaned_data = validate_user_inputs(input_fields, basic_schema)
        
        order = cleaned_data['Reaction order']
        a0 = cleaned_data['Initial concentration']
        k = cleaned_data['Reaction rate constant']
        t = cleaned_data['Time']

        simulate(order, a0, k, t)

    except ValueError as error_message:
        messagebox.showerror('Invalid input', error_message)


def temp_simulate_click(input_fields):
    try:
        cleaned_data = validate_user_inputs(input_fields, temperature_schema)
        
        order = cleaned_data['Reaction order']
        a0 = cleaned_data['Initial concentration']
        t = cleaned_data['Time']
        af = cleaned_data['Arrhenius factor']
        temp = cleaned_data['Temperature']
        ea = cleaned_data['Activation energy']
        k = calculate_k_arrhenius(af, ea, temp, order)

        simulate(order, a0, k, t)

    except ValueError as error_message:
        messagebox.showerror('Invalid input', error_message)