""" 5) Escreva um programa que inverta os caracteres de um string. 


    IMPORTANTE: 

        a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

        b) Evite usar funções prontas, como, por exemplo, reverse; """

import tkinter as tk

def invert_and_update():
    original_text = entry.get()
    inverted_text = invert_string(original_text)
    result_label.config(text=f"String Invertida: {inverted_text}")

def invert_string(text):
    inverted_text = ""
    for char in text:
        inverted_text = char + inverted_text
    return inverted_text

root = tk.Tk()
root.title("Inverter Strings")
root.geometry("600x200") 
label = tk.Label(root, text="Digite uma string:", font=("Times", 14))
label.pack()
entry = tk.Entry(root, font=("Times", 14))
entry.pack()
button = tk.Button(root, text="Inverter", command=invert_and_update, font=("Times", 14))
button.pack()
result_label = tk.Label(root, text="", font=("Times", 14))
result_label.pack()
root.mainloop()
