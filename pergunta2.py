""" 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

    IMPORTANTE:  

    Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; """

import tkinter as tk

def fibo_number(num):
    fib_sequence = fibo_sequence(num)
    if num in fib_sequence:
        return True
    else:
        return False

def veri_fibo():
    num = int(entry.get())
    if fibo_number(num):
        result_label.config(text=f"O número {num} pertence à sequência de Fibonacci.")
    else:
        result_label.config(text=f"O número {num} não pertence à sequência de Fibonacci.")

def fibo_sequence(a):
    fib = [0, 1]
    while fib[-1] < a:
        fib.append(fib[-1] + fib[-2])
    return fib

root = tk.Tk()
root.title("Sequência de Fibonacci")
root.geometry("600x200") 

label = tk.Label(root, text="Digite um número:", font=("Times", 14))
label.pack(pady=10)
entry = tk.Entry(root, font=("Times", 14))
entry.pack(pady=5)


button = tk.Button(root, text="Verificar", command=veri_fibo, font=("Times", 14))
button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Times", 14))
result_label.pack(pady=10)

root.mainloop()
