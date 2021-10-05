from tkinter import *
from tkinter import messagebox
import tkinter
from typing import Container
from PIL import Image, ImageTk
import pymysql

def enableDisable(estado):
    bd=pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="bbdd"
        )
        
    try:
        cursor=bd.cursor()
        sql="select count(usuario) from login"
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        cursor.execute(sql)
        bd.commit()
        myresult = cursor.fetchall()
        
        if 1 in myresult:
            #print(len(myresult))
            estado = tkinter.DISABLED
        else:
           print(len(myresult))
           estado= tkinter.NORMAL
    except:
        bd.rollback()
        #messagebox.showinfo(message="No hay administradores",title="Aviso")
        bd.close()
def menu_pantalla():
    bd=pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="bbdd"
        )
    global pantalla
    global b1
   
    estado=tkinter.DISABLED
    pantalla=Tk()
    pantalla.geometry("350x420")
    pantalla.title("Bienvenido Profesor")
    pantalla.iconbitmap("LogoTec.ico")

    # Read the Image
    image = Image.open("TecMilpaAlta.gif")
    
    # Reszie the image using resize() method
    resize_image = image.resize((200, 150))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.pack()
    """
    label=Label(pantalla)
    label(text="Acceso al Sistema",bg="navy",fg="white",width="250",height="3",font=("Arial",15)).pack()"""
    label = Label(pantalla,text="Acceso al Sistema",bg="green",fg="white",width="250",height="3",font=("Arial",15))
    label.pack()
    Label(text="").pack()
    b1 = Button(pantalla,text = "Iniciar sesión",activeforeground = "red",activebackground = "pink",pady=15,padx=25,command=inicio_sesion)
    b1.pack()
    Label(text="").pack()
   
    b1 = Button(pantalla,state=tkinter.NORMAL, text = "Registrar",activeforeground = "red",activebackground = "pink",pady=15,padx=25,command=registrar)
    b1.pack()
    try:
        cursor=bd.cursor()
        sql="select count(usuario) from login"
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        cursor.execute(sql)
        bd.commit()
        myresult = cursor.fetchall()
        lista=list(myresult)
        print(lista[0][0])
        if lista[0][0]==1:
            #print(len(myresult))
            b1['state'] = tkinter.DISABLED
            print("Si esta")
        else:
           #print(len(myresult))
           #print("Hola")
           b1['state']= tkinter.NORMAL
    except:
        bd.rollback()
        #messagebox.showinfo(message="No hay administradores",title="Aviso")
        bd.close()
    
    pantalla.mainloop()
   

#Funcion para pantalla externa
def inicio_sesion():
    global pantalla1
    pantalla1=Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("LogoTec.ico")
    Label(pantalla1,text="Ingrese su Usuario y contraseña",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()
    Label(pantalla1,text="").pack()

    #Etiquetas
    global nombreUsuario_verify
    global contrasenaUsuario_verify
    nombreUsuario_verify=StringVar()
    contrasenaUsuario_verify=StringVar()
    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1,text="Usuario").pack()
    nombre_usuario_entry=Entry(pantalla1,textvariable=nombreUsuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1,text="Contraseña").pack()
    contrasena_usuario_entry=Entry(pantalla1,textvariable=contrasenaUsuario_verify,show="°")
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1,text="Iniciar Sesion",command=validacionDatos).pack()
def registrar():
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("LogoTec.ico")
    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()
    Label(pantalla2,text="Ingresa un usuario y contraseña",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()
    Label(pantalla2,text="").pack()

    Label(pantalla2,text="Usuario").pack()
    nombreusuario_entry=Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()
    Label(pantalla2,text="Contraseña").pack()
    contrasena_entry=Entry(pantalla2,show="°")
    contrasena_entry.pack()
    Label(pantalla2).pack()
    Button(pantalla2,text="Registrar",command=inserta_datos).pack()

def inserta_datos():
    try:
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        fcursor=bd.cursor()
        #sql="INSERT INTO login (usuario,contrasena) VALUES ({0},{1})".format(nombreusuario_entry.get(),contrasena_entry.get())
    # sql="INSERT INTO login (usuario,contrasena) VALUES ('david','12345')"
        #validaciones
        fcursor.execute("SELECT usuario FROM login")
        """if fcursor.fetchall():
            messagebox.showinfo(message="Usuario y contraseña correcta",title="Sesion")
            pantalla.destroy()
            from inicio import inicio"""
        try:
            fcursor.execute("INSERT INTO login (usuario,contrasena) VALUES ('{0}','{1}')".format(str(nombreusuario_entry.get()),str(contrasena_entry.get())))
            bd.commit()#me lo envia a la base de datos
            messagebox.showinfo(message="Registro exitoso",title="Aviso")
            pantalla.destroy()
            menu_pantalla()
            
            
        except:
            print(bd.rollback())
            #messagebox.showinfo(message="Registro no registrado",title="Aviso")
            pantalla2.destroy()
        bd.close()#Se cierra la conexion
    except:    
        pantalla2.destroy()
        messagebox.showinfo(message="Base de datos no conectada",title="Aviso")
        
        


def validacionDatos():
    try:
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        fcursor=bd.cursor()
        fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreUsuario_verify.get()+"' and contrasena='"+contrasenaUsuario_verify.get()+"'")
        if fcursor.fetchall():
            #messagebox.showinfo(message="Usuario y contraseña correcta",title="Sesion")
            pantalla.destroy()
            from inicio import inicio
        else:
            messagebox.showinfo(message="Usuario y contraseña imcorrecta",title="Sesion")
        bd.close()
    except:
        messagebox.showinfo(message="Base de datos no conectada",title="Sesion")
        pantalla1.destroy()
        

menu_pantalla()