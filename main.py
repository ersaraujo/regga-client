import tkinter as tk

# Funções para atualizar a tela com diferentes emojis
def feliz():
    canvas.itemconfig(rosto, image=feliz_img)

def sede():
    canvas.itemconfig(rosto, image=sede_img)

def chorando():
    canvas.itemconfig(rosto, image=chorando_img)

# Criar a janela principal
root = tk.Tk()
root.title("Emojis")

# Carregar as imagens dos emojis
feliz_img = tk.PhotoImage(file="feliz.png")
sede_img = tk.PhotoImage(file="sede.png")
chorando_img = tk.PhotoImage(file="chorando.png")

# Criar a tela com o emoji inicialmente feliz
canvas = tk.Canvas(root, width=1280, height=720)
rosto = canvas.create_image(640, 360, anchor=tk.CENTER, image=feliz_img)
canvas.pack()

# Criar botões para mudar os emojis
btn_feliz = tk.Button(root, text="Feliz", command=feliz)
btn_feliz.pack(side=tk.LEFT)
btn_sede = tk.Button(root, text="Sede", command=sede)
btn_sede.pack(side=tk.LEFT)
btn_chorando = tk.Button(root, text="Chorando", command=chorando)
btn_chorando.pack(side=tk.LEFT)

# Executar a aplicação
