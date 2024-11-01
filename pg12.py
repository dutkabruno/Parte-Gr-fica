import tkinter as tk

#utilizando uma função para puxar a moeda digitada
def buscar_cotação():
    print(moeda.get())

janela = tk.Tk()

mensagem = tk.Label(text='Escreva a moeda', width=35, height=5, fg ='black', bg='white')
mensagem.grid(row=0, column=0)

moeda = tk.Entry(width=41, fg='white', bg='black')
moeda.grid(row=1, column=0)

mensagem1 = tk.Label(text='Aperte o botão', width=35, height=5, fg='white', bg='black')
mensagem1.grid(row=2, column=0)

botão = tk.Button(text="Este Botão", width=35, height=5, fg="black", bg="white", command=buscar_cotação)
botão.grid(row=3, column=0)

janela.mainloop()