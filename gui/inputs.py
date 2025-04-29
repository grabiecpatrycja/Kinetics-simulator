def get_user_inputs(input_fields):
    return {
        'reaction_order': input_fields['Reaction order'].get(),
        'initial_concentration': input_fields['Initial concentration'].get(),
        'rate_constant': input_fields['Reaction rate constant'].get(),
        'time': input_fields['Time'].get()
    }

def validate_inputs(data):
    try:
        order = int(data['reaction_order'])
        a0 = float(data['initial_concentration'])
        k = float(data['rate_constant'])
        t = float(data['time'])

        if a0 <= 0:
            return False, 'Initial concentration must be greater than 0.', None
        if k <= 0:
            return False, 'Reaction rate constant must be greater than 0.', None
        if t <= 0 or t > 1000:
            return False, 'Time must be between 0 and 1000 seconds.', None
        
        cleaned_data = {
            'reaction_order': order,
            'initial_concentration': a0,
            'rate_constant': k,
            'time': t
        }
        return True,'', cleaned_data
    
    except ValueError:
        return False, 'All inputs must be numeric.', None