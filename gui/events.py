from tkinter import messagebox
from gui.inputs import get_user_inputs, validate_inputs
from core.logic import simulate

def simulate_click(input_fields):
    user_data = get_user_inputs(input_fields)
    valid, error_message, cleaned_data = validate_inputs(user_data)
    if not valid:
        messagebox.showerror('Invalid input', error_message)
    simulate(cleaned_data)