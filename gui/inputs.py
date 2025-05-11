from tkinter import TclError

basic_schema = {
    'Reaction order': {},
    'Initial concentration': {'min': 0},
    'Reaction rate constant': {'min': 0},
    'Time': {'min': 0, 'max': 6000}
}

temperature_schema ={
    'Reaction order': {},
    'Initial concentration': {'min': 0},
    'Time': {'min': 0, 'max': 6000},
    'Activation energy': {'min': 5, 'max': 300},
    'Arrhenius factor':{'min': 1e6, 'max': 10e20, 'optional': True},
    'Temperature': {'min': 0, 'max': 2000}
}

def validate_user_inputs(input_fields, schema):
    cleaned_data = {}
    for key, rules in schema.items():
        try:
            value = input_fields[key].get()

            if value is None:
                if rules.get('optional'):
                    continue
                else:
                    raise ValueError(f"Missing value for '{key}'.")
        except TclError:
            raise ValueError("All inputs must be numeric.")
        
        if 'optional' in rules and value == 0:
            cleaned_data[key] = None
            continue
        
        if 'min' in rules and value <= rules['min']:
            raise ValueError(f"{key} must be greater than {rules['min']}.")
        if 'max' in rules and value > rules['max']:
            raise ValueError(f"{key} cannot be greater than {rules['max']}.")

        cleaned_data[key] = value
    
    return cleaned_data