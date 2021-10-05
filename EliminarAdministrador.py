import pymysql
import tkinter as tk
from tkinter import StringVar, ttk ,messagebox
import sys    
class eliminarAdninistrador():
    def eliminarAdministrador():
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor=bd.cursor()
        sql="DELETE FROM login WHERE usuario = '{0}' ".format(unElemento)
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        try:
            cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Eliminado exitso",title="Aviso")
            bd.close()
            sys.exit()
        except:
            bd.rollback()
            messagebox.showinfo(message="Eliminado no exitso",title="Aviso")
            bd.close()
        return ventana24.destroy()
    def selection_changed(event):
        global unElemento
        unElemento=""
        print("Nuevo elemento seleccionado:", monthchoosen.get()) 
        unElemento=monthchoosen.get()
        print(unElemento)
        return unElemento
    def ventanaAdministradorEliminar():
        global ventana24
        ventana24=tk.Tk()
        ventana24.title("Resgistra Grupo")
        ventana24.geometry("330x200")
        ventana24.configure(background="#F2F2F2")
        ventana24.iconbitmap("LogoTec.ico")
        global nombreGrupoEliminar_entry
        nombreGrupoEliminar_entry=StringVar()
        tk.Label(ventana24,text="Elimine un Administrador",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()
        tk.Label(ventana24,text="").pack()
        global monthchoosen
        n = tk.StringVar()
        monthchoosen = ttk.Combobox(ventana24, width = 10, textvariable = n)
        try:
            bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
            )
            cursor=bd.cursor()
            sql="select usuario from login"
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
        monthchoosen['values'] =mygrupo
    
        monthchoosen.pack()
        monthchoosen.current()
        monthchoosen.bind("<<ComboboxSelected>>",eliminarAdninistrador.selection_changed)
        tk.Label(ventana24).pack()
        tk.Button(ventana24,text="Eliminar",command=eliminarAdninistrador.eliminarAdministrador).pack()
        ventana24.mainloop()
