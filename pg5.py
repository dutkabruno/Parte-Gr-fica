import tkinter as tk

janela = tk.Tk()

mensagem = tk.Label(text= "digite a sua moeda")
mensagem.pack

# "Entry" lança uma barra para digitação, podemos mudar o tamanho da barra, com "width" e a cor da letra com "fg", e cor do fundo com "bg".
moeda=tk.Entry()
moeda.pack()

janela.mainloop()