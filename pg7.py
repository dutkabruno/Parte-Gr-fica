import tkinter as tk

janela = tk.Tk()

# "row" é a linha, e "column" é a coluna da tabela
mensagem = tk.Label(text='Sistema de Busca de Cotação de Moedas', width=35, height=5, fg='black', bg='white')
mensagem.grid(row=1, column=0)

mensagem1 = tk.Label(text='Selecione a moeda desejada',width=35, height=5, fg='white', bg='black')
mensagem1.grid(row=1, column=0)

moeda=tk.Entry()
moeda.grid(row=1, column=1, fg='white', bg='black')

janela.mainloop()