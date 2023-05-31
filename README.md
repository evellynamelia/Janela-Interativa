# Janela-Interativa
Este é um pequeno programa em Python que utiliza a biblioteca Tkinter para criar uma janela interativa. A janela exibe uma pergunta e apresenta botões de resposta 'Sim' e 'Não'. Ao passar o mouse sobre o botão 'Não', ele se move aleatoriamente. Ao clicar no botão 'Sim', uma mensagem adicional é exibida na janela. A aparência da janela é personalizada com cores de fundo e fontes.

# Explicação:

<li><i>Importação dos módulos:</i></li>
<br>

    import tkinter as tk
    import random
    
Essas linhas importam os módulos **"tkinter"** e **"random"**. O **"tkinter"** é usado para criar a interface gráfica, enquanto o **"random"** é usado para gerar números aleatórios.

<li><i>Criação da janela principal:</i></li>
<br>

    root = tk.Tk()
    root.geometry('250x250')
    root.configure(bg="#00b8f8")

Essas linhas criam a janela principal. A função **"tk.Tk()"** cria a instância da janela e **"root"** é o nome dessa instância. **"root.geometry('250x250')"** define a geometria da janela para ter uma largura de 250 pixels e uma altura de 250 pixels. **"root.configure(bg="#00b8f8")"** define  cor de fundo da janela como "#00b8f8".

<li><i>Função <b>"hover()"</b></i>:</li>
<br>

    def hover(event):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    nao.place(x=x, y=y)
    
    
Essa função é chamada quando o evento **"< Enter >"** ocorre, que é quando o mouse é passado sobre o botão "Não". Ela gera coordenadas aleatórias (**x** e **y**) e move o botão "Não" para essas coordenadas usando **"nao.place(x=x, y=y)"**.

<li><i>Função <b>"mensagem()"</b></i>:</li>
<br>
  
    def mensagem():
    message = tk.Label(root, text='Me passa um pix?', bg='#00b8f8', font=("Arial", 10, "bold"))
    message.place(x=70, y=120, relx=0, rely=0)
    
Essa função é chamada quando o botão "Sim" é clicado. Ela cria um rótulo **"(Label)"** chamado **"message"** com o texto "Me passa um pix?" e personaliza sua aparência com uma cor de fundo **"bg='#00b8f8'"** e uma fonte **"font=("Arial", 10, "bold")"**. Em seguida, o rótulo é colocado na janela nas coordenadas **"(70, 120)"** usando **"message.place(x=70, y=120, relx=0, rely=0)"**.

<li></i>Label <b>"pergunta":</b></i></li>
<br>

    pergunta = tk.Label(root, text='Manda <3', bg='#00b8f8', font=("Arial", 11, "bold"))
    pergunta.pack(pady=20)
    
Essas linhas criam um rótulo **"(Label)"** chamado **"pergunta"** com o texto "Manda <3" e personalizam sua aparência com uma cor de fundo **"bg='#00b8f8'"** e uma fonte **"font=("Arial", 11, "bold")"**. Em seguida, o rótulo é embalado **"(pack())"** na janela com um preenchimento vertical de **"20"** pixels **"(pady=20)"**.

<li><i>Botões <b>"nao"</b> e <b>"sim"</b>:</i></li>
<br>

    nao = tk.Button(root, text='Não', bg='#fffbf3')
    nao.place(x=140, y=80) 
    nao.bind('<Enter>', hover) 

    sim = tk.Button(root, text='Sim', bg='#fffbf3', command=mensagem)
    sim.place(x=25, y=80, relx=0, rely=0)

Essas linhas criam dois botões, **"nao"** e **"sim"**. O botão **"nao"** exibe o texto "Não" e tem uma cor de fundo **"bg='#fffbf3'"**. Ele é posicionado nas coordenadas **"(140, 80)"** usando **"nao.place(x=140, y=80)"**. Além disso, o evento **"< Enter >"** é vinculado ao botão **"nao"**, ou seja, quando o mouse é passado sobre ele, a função **"hover()"** é chamada.

O botão sim exibe o texto **"Sim"** e também tem uma cor de fundo **"bg='#fffbf3'".** Ele é posicionado nas coordenadas **(25, 80)** usando **"sim.place(x=25, y=80, relx=0, rely=0)"**. Quando o botão **sim** é clicado, a função **mensagem()** é chamada.

<li><i>Loop principal:</i></li>
<br>

    root.mainloop()

Essa linha inicia o loop principal da janela, que permite que a interface gráfica seja exibida e responda aos eventos do usuário.


