from scapy.all import *
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import sys

def capturar(cantidad):
    global registros
    registros = sniff(count = cantidad)

def guardarInt():
    text1.delete("1.0", "end")
    valor = int(ent1.get())
    capturar(valor)
    i = 0
    for x in registros:
        reg=x.summary()
        trama = f"{i}-{reg}"
        print(i," - ", x.summary())
        text1.insert("end",f"{i}-{reg}\n")
        i=i+1

def guardarPaquete():
    val = int(ent2.get())


    nombreSugerido= f"paquete_{val}.txt"
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")), initialfile=nombreSugerido)
    if file:
        with open(file, "w") as file:
            file.write("Estos son los datos del paquete seleccionado")
            file.write("Informacion de la trama")
            
            stdout_backup = sys.stdout
            sys.stdout = file

            registros[val].show()

            sys.stdout = stdout_backup
            file.write("Distribucion de bytes")
            stdout_backup1 = sys.stdout
            sys.stdout = file

            hexdump(registros[val])

            sys.stdout = stdout_backup1

           

    
root = Tk()
wind = root
wind.title("Captura de tramas LAN y WLAN")
wind.geometry("850x600")
fondo = "#DBD1E9"
wind.config(bg=fondo)

frame1 = LabelFrame(wind, text = "Captura de paquetes", font =("calibri", 14))

frame1.pack(fill="both", expand="yes", padx=10, pady=10)

lbl1 = Label(frame1, text=" # Paquetes a capturar", width=15)
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(frame1)
ent1.grid(row = 0, column=1, padx=5, pady=3)
button = Button(frame1, text="Capturar", command=guardarInt)
button.grid(row=0, column=2, padx=5, pady=5)

lbl2 = Label(frame1, text=" Datos de paquetes", width=15)
lbl2.grid(row=2, column=0, padx=5, pady=3)
text1 = Text(frame1, width=80, height=28)
text1.grid(row=2, column=1, columnspan=2)

lbl3 = Label(frame1, text="# Paquete a ver", width=20)
lbl3.grid(row=3, column=0, padx=5, pady=3)
ent2 = Entry(frame1)
ent2.grid(row = 3, column=1, padx=5, pady=3)
button2 = Button(frame1, text="Guardar paquete", command=guardarPaquete)
button2.grid(row=3, column=2, padx=5, pady=5)

root.mainloop()