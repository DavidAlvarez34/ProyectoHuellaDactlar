from tkinter import *
from tkinter import messagebox
from tkinter import StringVar, ttk
import tkinter as tk
from PIL import Image, ImageTk
import pymysql
def selection_changed(event):
    global elgrupo
    print("Nuevo elemento seleccionado:", monthchoosen.get())
    elgrupo = monthchoosen.get()
def selection_changed2(event):
    global elgrupo
    print("Nuevo elemento seleccionado:", monthchoosen2.get())
    elgrupo = monthchoosen2.get()
def selection_changed3(event):
    if monthchoosen3.get() == 'Retardo':
        print(monthchoosen3.get())
def registroLista():
    global nombreLista
    ventana39 = Tk()
    ventana39.title("Edita Lista")
    ventana39.geometry("300x200")
    ventana39.configure(background="#F2F2F2")
    ventana39.iconbitmap("LogoTec.ico")
    # Etiquetas
    etiqueta = Label(ventana39, text="Editar Lista",
                     bg="gray", fg="white", font=("Arial", 12))
    etiqueta.pack(padx=2, pady=2, ipady=1, ipadx=1, fill=X)
    # -----Seleccione grupo---
    Label(ventana39, text="Seleccione el grupo").pack()
    global monthchoosen
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(ventana39, width=10, textvariable=n)
    try:
        bd = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor = bd.cursor()
        sql = "select * from grupo"
    #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        cursor.execute(sql)
        bd.commit()
        myresult = cursor.fetchall()
        mygrupo = []
        for x in myresult:
            mygrupo.append(x)
    except:
        bd.rollback()
        messagebox.showinfo(message="No hay Grupos", title="Aviso")
        bd.close()
    # Adding combobox drop down list
    monthchoosen['values'] = mygrupo
    monthchoosen.pack()
    monthchoosen.current()
    monthchoosen.bind("<<ComboboxSelected>>", selection_changed)
    # ---------------------------------------------------------
    Label(ventana39, text="Seleccione la fecha").pack()
    # --------Seleccionar la fecha---------
    global monthchoosen2
    n = tk.StringVar()
    monthchoosen2 = ttk.Combobox(ventana39, width=10, textvariable=n)
    try:
        bd = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor = bd.cursor()
        sql = "select * from mifecha"
    #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        cursor.execute(sql)
        bd.commit()
        myresult = cursor.fetchall()
        mygrupo = []
        for x in myresult:
            mygrupo.append(x)
    except:
        bd.rollback()
        messagebox.showinfo(message="No hay Grupos", title="Aviso")
        bd.close()
    # Adding combobox drop down list
    monthchoosen2['values'] = mygrupo
    monthchoosen2.pack()
    monthchoosen2.current()
    monthchoosen2.bind("<<ComboboxSelected>>",
                       selection_changed2)
    # ------------Seleccionar la opccion del pasa de asistencia ---------
    Label(ventana39, text="Seleccione la asistencia").pack()
    global monthchoosen3
    n = tk.StringVar()
    monthchoosen3 = ttk.Combobox(ventana39, width=10, textvariable=n)
    # Adding combobox drop down list
    monthchoosen3['values'] = ('Presente',
                               'Retardo',
                               None
                               )
    monthchoosen3.pack()
    monthchoosen3.current()
    monthchoosen3.bind("<<ComboboxSelected>>",
                       selection_changed3)
    # Botones
    boton = Button(ventana39, text="Cambiar", fg="black", width=10)
    boton.pack(padx=1, pady=1, ipady=2, ipadx=2, fill=X)
    ventana39.mainloop()
registroLista()
