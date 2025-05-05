from tkinter import messagebox
from gui.inputs import validate_user_inputs
from core.logic import simulate

def simulate_click(input_fields):
    error_message, cleaned_data = validate_user_inputs(input_fields)
    if error_message:
        messagebox.showerror('Invalid input', error_message)
    simulate(cleaned_data)