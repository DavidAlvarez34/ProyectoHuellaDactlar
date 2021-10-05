from tkinter import *
from tkinter import messagebox
from tkinter import StringVar, ttk
import tkinter as tk
import pymysql
import random
class EditarDatoAlumno():
    def selection_changed(event):
        global elgrupo
        print("Nuevo elemento seleccionado:", monthchoosen.get())
        elgrupo=monthchoosen.get()
        #EditarDatoAlumno.editaAlumnos()
    def ventanaAlumnoEligeGrupo():
        global ventana34
        ventana34=Tk()
        ventana34.title("Resgistra Grupo")
        ventana34.geometry("330x200")
        ventana34.configure(background="#F2F2F2")
        ventana34.iconbitmap("LogoTec.ico")
        global nombreGrupoEliminar_entry
        nombreGrupoEliminar_entry=StringVar()
        Label(ventana34,text="Selecione el grupo",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()
        Label(ventana34,text="").pack()
        
        global monthchoosen
        n = StringVar()
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
        monthchoosen.bind("<<ComboboxSelected>>",EditarDatoAlumno.selection_changed)

        #------------------------------------Otro Elemento
        Label(ventana34).pack()
        tk.Button(ventana34,text="Enviar",command=EditarDatoAlumno.editaAlumnos).pack()
        ventana34.mainloop()
    def Edita_datos():
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor=bd.cursor()
        #ql="INSERT INTO Alumno(num_control,nombre_alumno,apellido_paterno,apellido_materno,ident_huella,iden_grupo) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(num_control.get(),nombre.get(),ape_pat.get(),ape_mat.get(),str(n),elgrupo)
        #sql="CREATE TABLE Alumno(num_control VARCHAR(15) NOT NULL,nombre_alumno VARCHAR(50),apellido_paterno VARCHAR(50),apellido_materno VARCHAR(50),ident_huella VARCHAR(10),iden_grupo VARCHAR(15),PRIMARY KEY(num_control),FOREIGN KEY (iden_grupo) REFERENCES grupo(iden_grupo))"
        sql=f"UPDATE lista_{elgrupo} SET nombre_alumno='{nombre.get()}',apellido_paterno='{ape_pat.get()}',apellido_materno='{ape_mat.get()}', iden_grupo ='{elgrupo}' WHERE num_control='{elgrupo2}'"
        print(sql)
        try:
            cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitso",title="Aviso")

        except:
            bd.rollback()
            messagebox.showinfo(message="Registro no exitso",title="Aviso")
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
            messagebox.showinfo(message="Registro no exitso",title="Aviso")
            bd.close()
    def registroHuella():
        global n; 
        #elegir un numero aleatorio de 1 a 127 para identificar el la huella
        n=random.randint(1,128)
        print(n)
    def selection_changed2(event):
            global elgrupo2
            print("Nuevo elemento seleccionado:", monthchoosen.get())
            elgrupo2=monthchoosen.get()
            print(elgrupo2)
    def editaAlumnos():
        global ventana37
        global num_control
        global nombre
        global ape_pat
        global ape_mat
        ventana37=Tk()
        ventana37.title("Formulario de editar Alumno")
        ventana37.geometry("300x700")
        ventana37.configure(background="#F2F2F2")
        ventana37.iconbitmap("LogoTec.ico")

        #Etiquetas
        etiqueta=Label(ventana37,text="Elige alumno por N° Control",bg="gray",fg="white",font=("Arial",12))
        etiqueta.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        #Edita el alumno
        global monthchoosen5
        global mygrupo2
        n = tk.StringVar()
        monthchoosen5 = ttk.Combobox(ventana37, width = 10, textvariable = n)
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
            myresult2 = cursor.fetchall()
            mygrupo2=[]
            for x in myresult2:
                mygrupo2.append(x)
        except:
            bd.rollback()
            print("Error")
            messagebox.showinfo(message="No hay Alumnos ni lista",title="Aviso")
            ventana37.destroy()
            bd.close()
        # Adding combobox drop down list
        monthchoosen5['values'] =mygrupo2
    
        monthchoosen5.pack()
        monthchoosen5.current()
        monthchoosen5.bind("<<ComboboxSelected>>",EditarDatoAlumno.selection_changed2)
        etiqueta=Label(ventana37,text="Elige grupo",bg="gray",fg="white",font=("Arial",12))
        etiqueta.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        #---------------combo box del grupo----------
        etiqueta=Label(ventana37,text="Nombre",bg="gray",fg="white",font=("Arial",12))
        etiqueta.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        #Se crea el cuadro de texto
        nombre=Entry(ventana37)
        nombre.pack(padx=6,pady=6,ipady=5,ipadx=5,fill=X)

        el=Label(ventana37,text="Apellido Paterno",bg="gray",fg="white",font=("Arial",12))
        el.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)

        ape_pat=Entry(ventana37)
        ape_pat.pack(padx=6,pady=6,ipady=5,ipadx=5,fill=X)

        e2=Label(ventana37,text="Apellido Materno",bg="gray",fg="white",font=("Arial",12))
        e2.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        ape_mat=Entry(ventana37)
        ape_mat.pack(padx=6,pady=6,ipady=5,ipadx=5,fill=X)
        boton=Button(ventana37,text="Editar",fg="black",bg="#DAF7A6",width=13,command=EditarDatoAlumno.Edita_datos)
        boton.pack(fill=X)
        ventana37.mainloop()  
