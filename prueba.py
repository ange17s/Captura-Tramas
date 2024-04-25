from tkinter import tkk
import tkinter as tk


def on_double_click(event):
    item = tree.selection()[0]
    print("Doble clic en:", tree.item(item, "text"))

root = tk.Tk()
root.title("Interfaz sencilla")

# Label y Entry para capturar paquetes
label_capture = tk.Label(root, text="Paquetes a capturar:")
label_capture.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

entry_capture = tk.Entry(root)
entry_capture.grid(row=0, column=1, padx=5, pady=5)

# Botón
button_capture = tk.Button(root, text="Capturar")
button_capture.grid(row=0, column=2, padx=5, pady=5)

# Label para paquetes de la trama
label_frame = tk.LabelFrame(root, text="Paquetes de la trama")
label_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.EW)

# Treeview para mostrar los paquetes de la trama
tree = tk.tkk.TreeView(label_frame, columns=("Datos",), show="headings")
tree.heading("Datos", text="Datos del paquete")
tree.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)
tree.bind("<Double-1>", on_double_click)

# Scrollbar para el Treeview
scrollbar = tk.ttk.Scrollbar(label_frame, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
tree.config(yscrollcommand=scrollbar.set)

# Campo para conectar con otro programa
connect_field = tk.Text(root, height=5, width=50)
connect_field.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
