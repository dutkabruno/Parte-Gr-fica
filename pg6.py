import tkinter as tk

janela = tk.Tk()

mensagem1 = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem1.pack()

mensagem2 = tk.Label(text="Selecione a Moeda Desejada", fg='black', bg='white', width=35, height=5)
mensagem2.pack()

moeda=tk.Entry(width=35, fg="white", bg="black")
moeda.pack()

janela.mainloop()