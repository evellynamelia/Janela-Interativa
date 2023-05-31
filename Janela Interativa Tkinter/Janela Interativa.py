import tkinter as tk 
import random

root = tk.Tk()
root.geometry('250x250')
root.configure(bg="#00b8f8")

def hover(event):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    nao.place(x=x, y=y)


def mensagem():
    message = tk.Label(root, text=' Texto teste1', bg='#00b8f8', font=("Arial", 10, "bold"))
    message.place(x=70, y=120, relx=0, rely=0)

pergunta = tk.Label(root, text='Texto teste', bg='#00b8f8', font=("Arial", 11, "bold"))
pergunta.pack(pady=20)

nao = tk.Button(root, text='Não', bg='#fffbf3')
nao.place(x=140, y=80) 
nao.bind('<Enter>', hover) 

sim = tk.Button(root, text='Sim', bg='#fffbf3', command=mensagem)
sim.place(x=25, y=80, relx=0, rely=0)

root.mainloop() 


