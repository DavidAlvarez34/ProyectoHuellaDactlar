from tkinter import *
from tkinter import messagebox
from tkinter import StringVar, ttk
import tkinter as tk
from PIL import Image, ImageTk
import pymysql
class Milista():
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
        sql=f"CREATE TABLE Lista_{elgrupo}(num_control VARCHAR(15) NOT NULL,nombre_alumno VARCHAR(50),apellido_paterno VARCHAR(50),apellido_materno VARCHAR(50),ident_huella VARCHAR(10),iden_grupo VARCHAR(15),PRIMARY KEY (num_control),FOREIGN KEY (iden_grupo) REFERENCES grupo(iden_grupo))"
        
        try:
            cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitso",title="Aviso")

        except:
            bd.rollback()
            messagebox.showinfo(message="Ya hay una lista con el mismo nombre",title="Aviso")
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
            global elgrupo
            print("Nuevo elemento seleccionado:", monthchoosen.get())
            elgrupo=monthchoosen.get()
    def registroLista():
        global nombreLista
        
        ventana39=Tk()
        ventana39.title("Crea una lista")
        ventana39.geometry("300x200")
        ventana39.configure(background="#F2F2F2")
        ventana39.iconbitmap("LogoTec.ico")
        """
        # Read the Image
        image = Image.open("TecMilpaAlta.gif")    
        # Reszie the image using resize() method
        resize_image = image.resize((150, 150))    
        img = ImageTk.PhotoImage(resize_image)    
        # create label and add resize image
        label1 = Label(image=img)
        label1.image = img
        label1.pack()"""
        #Etiquetas
        etiqueta=Label(ventana39,text="Elige grupo de la lista",bg="gray",fg="white",font=("Arial",12))
        etiqueta.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        global monthchoosen
        n = tk.StringVar()
        monthchoosen = ttk.Combobox(ventana39, width = 10, textvariable = n)
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
        monthchoosen.bind("<<ComboboxSelected>>",Milista.selection_changed)

        #Botones
        boton=Button(ventana39,text="Registrar",fg="black",width=10,command=Milista.insertar_datos)
        boton.pack(padx=1,pady=1,ipady=2,ipadx=2,fill=X)
        """
        boton2=Button(ventana,text="insertar columnas",fg="black",width=10,command=insertar_columna)
        boton2.pack(side=LEFT)
        boton3=Button(ventana,text="Actualizar",fg="black",width=10)
        boton3.pack(side=LEFT)
        boton4=Button(ventana,text="Eliminar",fg="black",width=10)
        boton4.pack(side=LEFT)"""
        ventana39.mainloop()
