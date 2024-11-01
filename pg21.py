import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()

# o "checkbox" cria uma caixinha para vc decidir se quer marcado ou não marcado
checkbox_promocoes = tk.Checkbutton(text='Deseja receber e-mails promocionais?', variable = var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

def enviar():
    print (var_promocoes.get())

botao_enviar = tk.Button (text="Enviar", command = enviar)
botao_enviar.grid(row=1, column=0)

tk.mainloop()