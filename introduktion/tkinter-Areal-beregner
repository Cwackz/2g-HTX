import math
import tkinter as tk
from tkinter import ttk, messagebox

def calculate_area():
    valg = int(selected_figure.get())
    if valg == 1:  
        try:
            r = float(radius_entry.get())
            result = math.pi * r**2
            result_label.config(text=f"Resultat: {result:.2f}")
        except ValueError:
            messagebox.showerror("Fejl", "Ugyldigt input. Indtast et gyldigt nummer.")
    elif valg == 2:  
        try:
            l = float(length_entry.get())
            b = float(width_entry.get())
            result = l * b
            result_label.config(text=f"Resultat: {result:.2f}")
        except ValueError:
            messagebox.showerror("Fejl", "Ugyldigt input. Indtast gyldige numre.")
            
    radius_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)

def on_figure_selection(*args):
    valg = int(selected_figure.get())
    if valg == 1:  
        length_label.grid_remove()
        length_entry.grid_remove()
        width_label.grid_remove()
        width_entry.grid_remove()
        
        radius_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        radius_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w", columnspan=2)
    elif valg == 2:  
        radius_label.grid_remove()
        radius_entry.grid_remove()
        
        length_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        length_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        width_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        width_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

root = tk.Tk()
root.title("Områdets lommeregner")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TRadiobutton", font=("Arial", 12), width=10)  

figure_label = ttk.Label(root, text="Vælg en figur:")
figure_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

selected_figure = tk.StringVar()
selected_figure.set("1")  
figure_choices = [("Cirkel", 1), ("Rektangel", 2)]
for idx, (text, value) in enumerate(figure_choices):
    ttk.Radiobutton(root, text=text, variable=selected_figure, value=value, command=on_figure_selection).grid(row=1, column=idx, padx=10, pady=5)

radius_label = ttk.Label(root, text="Indtast radius:")
radius_entry = ttk.Entry(root)
length_label = ttk.Label(root, text="Indtast længden:")
length_entry = ttk.Entry(root)
width_label = ttk.Label(root, text="Indtast bredden: ")
width_entry = ttk.Entry(root)

calculate_button = ttk.Button(root, text="Beregn", command=calculate_area)
calculate_button.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

result_label = ttk.Label(root, text="Resultat:")
result_label.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

on_figure_selection()

root.mainloop()
