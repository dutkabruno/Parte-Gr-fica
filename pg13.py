import tkinter as tk

dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text='Cotação não encontrada')
    mensagem_cotacao.grid(row=3, column=0, columnspan=2)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'

#def buscar_cotação():
#    print(moeda.get())

janela = tk.Tk()

mensage = tk.Label(text="Sistema de Banco de Cotação de Moedas", width=70, height=5, fg='white', bg='black')
mensage.grid(row=0, column=0, columnspan=2)

mensagem = tk.Label(text='Escreva a moeda', width=35, height=5, fg ='black', bg='white')
mensagem.grid(row=1, column=0)

moeda = tk.Entry(fg='white', bg='black')
moeda.grid(row=1, column=1)

mensagem1 = tk.Label(text='Aperte o botão', width=35, height=5, fg='black', bg='white')
mensagem1.grid(row=2, column=0)

botão = tk.Button(text="Este Botão", width=35, height=5, fg="white", bg="black", command=buscar_cotacao)
botão.grid(row=2, column=1)

janela.mainloop()