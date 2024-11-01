import tkinter as tk

janela = tk.Tk()

botao_classeeconomica = tk.Radiobutton(text="Classe econô,ica")
botao_classexecutiva = tk.Radiobutton(text="Classe Execuitivo")
botao_primeiraclasse = tk.Radiobutton(text="Primeira classe")
botao_classeeconomica.grid(row = 0, column = 0) 
botao_classexecutiva.grid(row = 0, column = 1) 
botao_primeiraclasse.grid(row = 0, column = 2)

tk.mainloop()