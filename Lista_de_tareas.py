from tkinter import *

papel= Tk()
papel.title("PAVL & Co.")
papel.geometry("500x600")
#papel.resizable(False,False)
entradas=StringVar()
def azul():
    papel.config(bg="lightblue")
def rosa():
    papel.config(bg="pink")
def verde():
    papel.config(bg="lightgreen")
def blanco():
    papel.config(bg="white")
def gris():
    papel.config(bg="lightgrey")

def guardadores():
    with open("Lista de tareas.txt","a") as abrrir:
        escribir=abrrir.write(f"{entrada.get()}\n")
    Lista.insert(1,entradas.get())
    

bara=Menu(papel)
papel.config(menu=bara)
menu=Menu(bara,tearoff=0)
bara.add_cascade(label="Archivos",menu=menu)

menu2=Menu(bara,tearoff=0)
menu.add_command(label="Nuevo")

menu.add_command(label="Cerrar",command=exit)

bara.add_cascade(label="Color de fondo",menu=menu2)
menu2.add_command(label="Azul cielo",command=azul)
menu2.add_command(label="Rosa",command=rosa)
menu2.add_command(label="Verde claro",command=verde)
menu2.add_command(label="Blanco",command=blanco)
menu2.add_command(label="Gris",command=gris)

Lista=Listbox(papel,width=100,borderwidth=2,height=30,relief="raised")
Lista.pack(padx=20,pady=20)

entrada=Entry(papel,width=50,borderwidth=2,relief="raised",textvar=entradas)
entrada.pack()

guardador=Button(papel,text="Guardador",bg="yellow",fg="black",command=guardadores).pack(pady=10)


mainloop()