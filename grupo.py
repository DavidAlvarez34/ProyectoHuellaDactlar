import pymysql
import tkinter as tk
from tkinter import StringVar, ttk ,messagebox
class Grupos():
    def editarGrupo():
        #UPDATE grupo SET iden_grupo = ‘valor’ WHERE iden_grupo='valor'
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor=bd.cursor()
        #sql="INSERT INTO Alumno(num_control,nombre_alumno,apellido_paterno,apellido_materno,ident_huella) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(num_control.get(),nombre.get(),ape_pat.get(),ape_mat.get(),str(n))
        sql="UPDATE grupo SET iden_grupo = '{0}' WHERE iden_grupo='{1}'".format(nombreGrupoEditarNew_entry.get(),nombreGrupoEditar_entry.get())
        try:
            cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitso",title="Aviso")
        except:
            bd.rollback()
            messagebox.showinfo(message="Fallo en la actualizacion",title="Aviso")
            bd.close()
    def ventanaGrupoActualizar():
        global ventana2
        ventana2=tk.Tk()
        ventana2.title("Resgistra Grupo")
        ventana2.geometry("330x250")
        ventana2.configure(background="#F2F2F2")
        ventana2.iconbitmap("LogoTec.ico")
        global nombreGrupoEditar_entry
        global nombreGrupoEditarNew_entry
        nombreGrupoEditar_entry=StringVar()
        nombreGrupoEditarNew_entry=StringVar()
        tk.Label(ventana2,text="Ingrese un nombre unico para identificar el grupo",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()
        tk.Label(ventana2,text="").pack()

        tk.Label(ventana2,text="Grupo a editar").pack()
        nombreGrupoEditar_entry=tk.Entry(ventana2)
        nombreGrupoEditar_entry.pack()
        tk.Label(ventana2,text="Nuevo nombre del grupo").pack()
        nombreGrupoEditarNew_entry=tk.Entry(ventana2)
        nombreGrupoEditarNew_entry.pack()
        tk.Label(ventana2).pack()
        tk.Button(ventana2,text="Actulizar",command=Grupos.editarGrupo).pack()
        ventana2.mainloop()

    def eliminarGrupo():
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor=bd.cursor()
        sql="DELETE FROM grupo WHERE iden_grupo = '{0}' ".format(nombreGrupoEliminar_entry.get())
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        try:
            cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Eliminado exitso",title="Aviso")
            bd.close()
        except:
            bd.rollback()
            messagebox.showinfo(message="Eliminado no exitso",title="Aviso")
            bd.close()
        return ventana2.destroy()
    def ventanaGrupoEliminar():
        global ventana2
        ventana2=tk.Tk()
        ventana2.title("Resgistra Grupo")
        ventana2.geometry("330x200")
        ventana2.configure(background="#F2F2F2")
        ventana2.iconbitmap("LogoTec.ico")
        global nombreGrupoEliminar_entry
        nombreGrupoEliminar_entry=StringVar()
        tk.Label(ventana2,text="Ingrese un nombre unico para identificar el grupo",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()
        tk.Label(ventana2,text="").pack()

        tk.Label(ventana2,text="Grupo").pack()
        nombreGrupoEliminar_entry=tk.Entry(ventana2)
        nombreGrupoEliminar_entry.pack()
        tk.Label(ventana2).pack()
        tk.Button(ventana2,text="Eliminar",command=Grupos.eliminarGrupo).pack()
        ventana2.mainloop()

    