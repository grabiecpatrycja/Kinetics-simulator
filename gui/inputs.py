from tkinter import TclError

def validate_user_inputs(input_fields):
    try:
        order = input_fields['Reaction order'].get()
        a0 = input_fields['Initial concentration'].get()
        k = input_fields['Reaction rate constant'].get()
        t = input_fields['Time'].get()

        print(type(order))
        if a0 <= 0:
            return 'Initial concentration must be greater than 0.', None
        if k <= 0:
            return 'Reaction rate constant must be greater than 0.', None
        if t <= 0 or t> 1000:
            return 'Time must be between 0 and 1000 seconds.', None
        
        cleaned_data = {
            'reaction_order': order,
            'initial_concentration': a0,
            'rate_constant': k,
            'time': t
        }
        return '', cleaned_data
    
    except TclError:
        return 'All inputs must be numeric.', None