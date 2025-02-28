import tkinter as tk


def somar():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    soma = n1 + n2
    resultado.config(text=f'{soma}')

def sub():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    subtração = n1 - n2
    resultado.config(text=f'{subtração}')

def mult():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    multiplicação = n1 * n2
    resultado.config(text=f'{multiplicação}')

def div():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    divisão = n1 / n2
    resultado.config(text=f'{divisão}')

root = tk.Tk()

root.geometry('310x500')
root.title('CALCULATOR')

text = tk.Label(root,text='CALCULATOR',fg='cyan',justify='center',bg='black')
text.grid(row=1,column=1)

text2 = tk.Label(root,text='digite um numero')
text2.grid(row=2,column=2,pady=10,padx=10)

numero1 = tk.Entry(root,width=10)
numero1.grid(row=3,column=2,pady=10,padx=10)

text3 = tk.Label(root,text='digite um numero')
text3.grid(row=4,column=2,pady=10,padx=10)
                 
numero2 = tk.Entry(root,width=10)
numero2.grid(row=5,column=2,pady=10,padx=10)

resultado = tk.Label(root,text= 'resultado')
resultado.grid(row=6,column=2,pady=10,padx=10)

btn = tk.Button(root,text='+',command=somar)
btn.grid(row=7,column=1,pady=10,padx=7)

btn = tk.Button(root,text='-',command=sub)
btn.grid(row=7,column=2,pady=10,padx=6)

btn = tk.Button(root,text='x',command=mult)
btn.grid(row=7,column=3,pady=10,padx=19)

btn = tk.Button(root,text='/',command=div)
btn.grid(row=7,column=4,pady=10,padx=10)

root.mainloop()