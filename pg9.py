import tkinter as tk

# tem como mecher em muita coisa com o "row", "column", "rowspan" e "columnspan".
janela = tk.Tk()

mensagem = tk.Label(text="Sistema de Cotação de Moedas", width=35, height=5)
mensagem.grid(row=0, column=0, rowspan=2, columnspan=2)

mensagem1 = tk.Label(text='Selecione a moeda', width=35, height=5)
mensagem1.grid(row=2, column=0)

mensagem2 = tk.Label(text='Selecione a quantidade', width=35, height=5)
mensagem2.grid(row=2, column=1)

moeda = tk.Entry(width=35)
moeda.grid(row=1, column=2)

janela.mainloop()