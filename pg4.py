import tkinter as tk

janela = tk.Tk()

#como trocar a cor do texto e do fundo da imagem "fg" a cor da letra, e "bg" a cor do fundo
mensagem = tk.Label(text="Carro maneiro", fg='#7FFF00',bg='#8B4513', width= 256, height=28)
mensagem.pack()

mensagem = tk.Label(text="Carro super maneiro", fg='#DDA0DD', bg='#FF0000', width= 256, height=18)
mensagem.pack()

mensagem = tk.Label(text="Carro super mega maneiro", fg='#FFFFE0', bg='#B0E0E6', width= 256, height=10)
mensagem.pack()

janela.mainloop()