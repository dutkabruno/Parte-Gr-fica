import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

# "\n" é quebra de linha, mesmo dentro do texto podemos quebrar a linha, como no exemplo abaixo
mensagem = tk.Label(text="Sistema de busca de Cotação de Moedas")
mensagem.pack()

# "mensagem = tk.Label()" para funcionar, precisa ter "mensagem.pack()" depois, mas na linha debaixo, se colocar na mesma linha não funciona
mensagem = tk.Label(text="Sistema de busca de Cotação de Moedas", fg='white', bg='black', width=50, height=10)
mensagem.pack()

# "width" é a largura, e "height" é a altura, sendo que o máximo da tela é "width = 256" e "height = 56(eu acho)"
mensagem2 = tk.Label(text=" Selecione a moeda desejada ", fg='black', bg='white', width=70, height=15)
mensagem2.pack()

moeda = tk.Entry(width=35, fg='white', bg='black')
moeda.pack()

janela.mainloop()