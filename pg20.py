import tkinter as tk

janela = tk.Tk()

# o "checkbox" cria uma caixinha para vc decidir se quer ou não
var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text='Deseja receber e-mails promocionais?', variable = var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

tk.mainloop()