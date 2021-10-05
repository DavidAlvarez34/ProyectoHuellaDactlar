import pymysql
import tkinter as tk
from tkinter import StringVar, ttk ,messagebox    
class EliminarElAlumno():
    def eliminarAdministrador():
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor=bd.cursor()
        sql=f"DELETE FROM lista_{elgrupo} WHERE num_control = {unElemento} "
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
        return ventana34.destroy(),ventana341.destroy()
    def ventanaAlumnoEliminarControl():
            global ventana341
            ventana341=tk.Tk()
            ventana341.title("Resgistra Grupo")
            ventana341.geometry("330x200")
            ventana341.configure(background="#F2F2F2")
            ventana341.iconbitmap("LogoTec.ico")
            global nombreGrupoEliminar_entry
            nombreGrupoEliminar_entry=StringVar()
            tk.Label(ventana341,text="Selecione el grupo",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()
            tk.Label(ventana341,text="").pack()

            #------------------------------------Otro Elemento
            tk.Label(ventana341,text="").pack()
            global monthchoosen2
            n = tk.StringVar()
            monthchoosen2= ttk.Combobox(ventana341, width = 10, textvariable = n)
            try:
                bd=pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="bbdd"
                )
                cursor=bd.cursor()
                sql=f"select num_control from lista_{elgrupo}"
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
            monthchoosen2['values'] =mygrupo
        
            monthchoosen2.pack()
            monthchoosen2.current()
            monthchoosen2.bind("<<ComboboxSelected>>",EliminarElAlumno.selection_changed2)
            tk.Label(ventana341).pack()
            tk.Button(ventana341,text="Eliminar",command=EliminarElAlumno.eliminarAdministrador).pack()
            ventana341.mainloop()
    def selection_changed(event):
        global elgrupo
        print("Nuevo elemento seleccionado:", monthchoosen.get())
        elgrupo=monthchoosen.get()
        
        EliminarElAlumno.ventanaAlumnoEliminarControl()
    def selection_changed2(event):
        global unElemento
        print("Nuevo elemento seleccionado:", monthchoosen2.get())
        unElemento=monthchoosen2.get()
    def ventanaAlumnoEliminar():
        global ventana34
        ventana34=tk.Tk()
        ventana34.title("Resgistra Grupo")
        ventana34.geometry("330x200")
        ventana34.configure(background="#F2F2F2")
        ventana34.iconbitmap("LogoTec.ico")
        global nombreGrupoEliminar_entry
        nombreGrupoEliminar_entry=StringVar()
        tk.Label(ventana34,text="Selecione el grupo",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()
        tk.Label(ventana34,text="").pack()
        
        global monthchoosen
        n = tk.StringVar()
        monthchoosen = ttk.Combobox(ventana34, width = 10, textvariable = n)
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
        monthchoosen['values'] =mygrupo
    
        monthchoosen.pack()
        monthchoosen.current()
        monthchoosen.bind("<<ComboboxSelected>>",EliminarElAlumno.selection_changed)

        #------------------------------------Otro Elemento
        tk.Label(ventana34).pack()
        #tk.Button(ventana34,text="Eliminar",command=EliminarElAlumno.eliminarAdministrador).pack()
        ventana34.mainloop()

        
#EliminarElAlumno.ventanaAlumnoEliminar()