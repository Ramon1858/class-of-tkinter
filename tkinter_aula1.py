import tkinter as tk

def display():
    texto = input_1.get()
    text_display.config(text=f'{texto}')

janela = tk.Tk()
janela.title('Teste')

janela.geometry ('350x500')

text = tk.Label(janela,text= 'cadastro que usa só o nome')
text.pack()

input_1 = tk.Entry(janela,width= 15,fg ='green',bg='black',font= 'arial')
input_1.pack()

btn = tk.Button(janela,text='click here before you login', command=display)
btn.pack()

text_display = tk.Label(janela, text='vai mostrar aqui')
text_display.pack()

janela.mainloop()