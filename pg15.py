import tkinter as tk

# "ttk" é uma extenção do tkinter
from tkinter import ttk

janela = tk.Tk()

dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000,
    'Kjkj': 90438569034905
}

# "list(dicionario_cotacoes.keys())" cira uma lista com os dados do "dicionario_cotacoes", com as "keys" já definidas, que são as entre aspas
moedas = list(dicionario_cotacoes.keys())
# "Combobox" cria uma aba para escolher uma das opções possíveis
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text='Cotação não encontrada')
    mensagem_cotacao.grid(row=4, column=0, columnspan=2)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'

def buscar_cotacoes():
    texto= caixa_texto.get("1.0",tk.END)
    lista_moedas = texto.split('\n')
    #print(lista_moedas)
    mensagem_cotacoes=[]
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}:{cotacao}')
    mensagem3 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem3.grid(row=7, column=1)

mensage = tk.Label(text="Sistema de Banco de Cotação de Moedas", width=70, height=5, fg='white', bg='black')
mensage.grid(row=0, column=0, columnspan=2)

mensagem = tk.Label(text='Escreva a moeda', width=35, height=5, fg ='black', bg='white')
mensagem.grid(row=1, column=0, rowspan=2)

#moeda = tk.Entry(fg='white', bg='black')
#moeda.grid(row=1, column=1)

mensagem1 = tk.Label(text='Aperte o botão', width=35, height=5, fg='black', bg='white')
mensagem1.grid(row=2, column=1)

caixa_texto= tk.Text(width= 10, height=5)
caixa_texto.grid(row=6, column=0, sticky='nswe')

mensagem2=tk.Label(text='Caso você queira pagar mais 1 cotação ao mesmo tempo, digite uma moeda em cada linha')
mensagem2.grid(row=5, column=0, columnspan=2)

botao = tk.Button(text="Buscar Cotação",command=buscar_cotacao)
botao.grid(row=3, column=1)

botao_multiplascotacoes = tk.Button(text='Buscar Cotações', command=buscar_cotacoes)
botao_multiplascotacoes.grid(row=6, column=1)

janela.mainloop()