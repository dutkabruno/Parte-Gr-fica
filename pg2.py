import tkinter as tk

janela = tk.Tk()

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas")
mensagem.pack()

mensagem2 = tk.Label(text=" Selecione a moeda desejada ")
mensagem2.pack()

mensagem3 = tk.Label(text=" Moeda 1 = Moeda de 1 centavo\nMoeda 2 = Moeda de 5 centavos\nMoeda 3 = Moeda de 10 centavos\nMoeda 4 = Moeda de 25 centavos\nMoeda 5 = Moeda de 50 centavos\nMoeda 6 = Moeda de 1 real ")
mensagem3.pack()

janela.mainloop()