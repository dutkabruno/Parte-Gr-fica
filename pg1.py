import tkinter as tk

janela = tk.Tk()

# "\n" é quebra de linha, mesmo dentro do texto podemos quebrar a linha, como no exemplo abaixo
mensagem = tk.Label(text="Sistema de busca de Cotação de Moedas\nMoedas novas são suspeitas\ntome cuidado com as pessoas que as usam\n\n\n\n\n\n\n\n\n")
mensagem.pack()

# "mensagem = tk.Label()" para funcionar, precisa ter "mensagem.pack()" depois, mas na linha debaixo, se colocar na mesma linha não funciona
mensagem = tk.Label(text="Sistema de busca de Cotação de Moedas\nMoedas novas são suspeitas\ntome cuidado com as pessoas que as usam")
mensagem.pack()

janela.mainloop()