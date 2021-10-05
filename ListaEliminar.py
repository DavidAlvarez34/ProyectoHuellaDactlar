from Lista import Milista
from tkinter import *
from tkinter import messagebox
from tkinter import StringVar, ttk
import tkinter as tk
from PIL import Image, ImageTk
import pymysql
import random

class MilistaEliminar():
    def insertar_datos():
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        grupos="la diosa"
        cursor=bd.cursor()
        #sql="INSERT INTO Alumno(num_control,nombre_alumno,apellido_paterno,apellido_materno,ident_huella,iden_grupo) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(num_control.get(),nombre.get(),ape_pat.get(),ape_mat.get(),str(n),elgrupo)
        #sql=f"CREATE TABLE Lista_{elgrupo}(num_control VARCHAR(15) NOT NULL,nombre_alumno VARCHAR(50),apellido_paterno VARCHAR(50),apellido_materno VARCHAR(50),ident_huella VARCHAR(10),iden_grupo VARCHAR(15),PRIMARY KEY (num_control),FOREIGN KEY (iden_grupo) REFERENCES grupo(iden_grupo))"
        sql=f"DROP TABLE Lista_{miGrupo}"
        try:
            cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Lista Completa Eliminada",title="Aviso")

        except:
            bd.rollback()
            messagebox.showinfo(message="No hay Lista creada",title="Aviso")
            bd.close()
    def insertar_columna():
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor=bd.cursor()
        #print(fecha)
        #Agregar una columna para pasar lista el dia de la clase
        sql="ALTER TABLE Alumno add fecha varchar(50)"
        try:
            cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitso",title="Aviso")
        except:
            bd.rollback()
            messagebox.showinfo(message="Registro exitso",title="Aviso")
            bd.close()
    def selection_changed(event):
            global miGrupo
            miGrupo=monthchoosen7.get()
            print(miGrupo)
    def eliminaLista():
        global nombreLista
        global monthchoosen7
        ventana39=Tk()
        ventana39.title("Elimine una Lista")
        ventana39.geometry("300x200")
        ventana39.configure(background="#F2F2F2")
        ventana39.iconbitmap("LogoTec.ico")
        #Etiquetas
        etiqueta=Label(ventana39,text="Elige grupo de la lista",bg="gray",fg="white",font=("Arial",12))
        etiqueta.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        n = tk.StringVar()
        monthchoosen7 = ttk.Combobox(ventana39, width = 10, textvariable = n)
        try:
            bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
            )
            cursor=bd.cursor()
            sql="select * from grupo"
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
            cursor.execute(sql)
            bd.commit()
            myresult = cursor.fetchall()
            mygrupo=[]
            for x in myresult:
                mygrupo.append(x)
        except:
            bd.rollback()
            messagebox.showinfo(message="No hay Grupos",title="Aviso")
            bd.close()
        # Adding combobox drop down list
        monthchoosen7['values'] =mygrupo
        monthchoosen7.pack()
        monthchoosen7.current()
        monthchoosen7.bind("<<ComboboxSelected>>",MilistaEliminar.selection_changed)
        #Botones
        boton=Button(ventana39,text="Eliminar",fg="black",width=10,command=MilistaEliminar.insertar_datos)
        boton.pack(padx=1,pady=1,ipady=2,ipadx=2,fill=X)
        ventana39.mainloop()
