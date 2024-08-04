import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Conversor de Unidades")

style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), background='lightblue')
style.configure('TCombobox', font=('Arial', 12), padding=5)
style.configure('TButton', font=('Arial', 12), padding=5, relief='flat', background='skyblue')
style.map('TButton', background=[('active', 'deepskyblue')])

units_length = ['metros', 'kilómetros', 'centímetros', 'milímetros']
units_weight = ['gramos', 'kilogramos', 'libras', 'onzas']
units_temperature = ['Celsius', 'Fahrenheit', 'Kelvin']

def convert_length(value, from_unit, to_unit):
    conversions = {
        'metros': 1,
        'kilómetros': 1000,
        'centímetros': 0.01,
        'milímetros': 0.001
    }
    value_in_meters = value * conversions[from_unit]
    return value_in_meters / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'gramos': 1,
        'kilogramos': 1000,
        'libras': 453.592,
        'onzas': 28.3495
    }
    value_in_grams = value * conversions[from_unit]
    return value_in_grams / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32

def update_conversion():
    try:
        value = float(value_entry.get())
        unit_type = unit_type_var.get()
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        
        if unit_type == 'Longitud':
            result = convert_length(value, from_unit, to_unit)
        elif unit_type == 'Peso':
            result = convert_weight(value, from_unit, to_unit)
        elif unit_type == 'Temperatura':
            result = convert_temperature(value, from_unit, to_unit)
        
        result_label.config(text=f"Resultado: {result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Por favor ingrese un valor numérico válido.")

config_frame = tk.Frame(root, padx=20, pady=20, background='lightblue')
config_frame.pack(padx=20, pady=20)

unit_type_var = tk.StringVar(value='Longitud')
unit_type_label = tk.Label(config_frame, text="Tipo de Unidad:", background='lightblue')
unit_type_label.grid(row=0, column=0, sticky='w')
unit_type_menu = ttk.Combobox(config_frame, textvariable=unit_type_var, values=['Longitud', 'Peso', 'Temperatura'])
unit_type_menu.grid(row=0, column=1)

from_unit_var = tk.StringVar()
from_unit_label = tk.Label(config_frame, text="Desde Unidad:", background='lightblue')
from_unit_label.grid(row=1, column=0, sticky='w')
from_unit_menu = ttk.Combobox(config_frame, textvariable=from_unit_var)
from_unit_menu.grid(row=1, column=1)

to_unit_var = tk.StringVar()
to_unit_label = tk.Label(config_frame, text="Hasta Unidad:", background='lightblue')
to_unit_label.grid(row=2, column=0, sticky='w')
to_unit_menu = ttk.Combobox(config_frame, textvariable=to_unit_var)
to_unit_menu.grid(row=2, column=1)

value_entry = tk.Entry(config_frame, width=15, font=('Arial', 12))
value_entry.grid(row=3, column=1, pady=10)

convert_button = ttk.Button(config_frame, text="Convertir", command=update_conversion)
convert_button.grid(row=4, column=1, pady=10)

result_label = tk.Label(config_frame, text="Resultado:", background='lightblue')
result_label.grid(row=5, column=1, pady=10)

def update_unit_options(*args):
    unit_type = unit_type_var.get()
    if unit_type == 'Longitud':
        units = units_length
    elif unit_type == 'Peso':
        units = units_weight
    elif unit_type == 'Temperatura':
        units = units_temperature
    
    from_unit_menu['values'] = units
    to_unit_menu['values'] = units
    if from_unit_var.get() not in units:
        from_unit_var.set(units[0])
    if to_unit_var.get() not in units:
        to_unit_var.set(units[0])

unit_type_var.trace_add('write', update_unit_options)

root.mainloop()
