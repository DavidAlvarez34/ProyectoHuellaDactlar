from tkinter import *
from tkinter import messagebox
from tkinter import StringVar, ttk
import tkinter as tk
from PIL import Image, ImageTk
import pymysql
import random
import serial
import time
import threading
from tkinter.scrolledtext import *

class Alumnos():
    def insertar_datos():
        bd=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor=bd.cursor()
        sql=f"INSERT INTO Lista_{elgrupo}(num_control,nombre_alumno,apellido_paterno,apellido_materno,ident_huella,iden_grupo) VALUES ('{num_control.get()}','{nombre.get()}','{ape_pat.get()}','{ape_mat.get()}','{str(numero)}','{elgrupo}')"#.format(num_control.get(),nombre.get(),ape_pat.get(),ape_mat.get(),str(n),elgrupo)
        #sql="CREATE TABLE Lista(num_control VARCHAR(15) NOT NULL,nombre_alumno VARCHAR(50),apellido_paterno VARCHAR(50),apellido_materno VARCHAR(50),ident_huella VARCHAR(10),iden_grupo VARCHAR(15),PRIMARY KEY (num_control),FOREIGN KEY (iden_grupo) REFERENCES grupo(iden_grupo))"
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
            messagebox.showinfo(message="Registro exitso",title="Aviso")
            bd.close()
    def cerrar():
        from inicio import inicio
        ventana3.destroy()
        
        
        print("Hola")
    def selection_changed(event):
            global elgrupo
            print("Nuevo elemento seleccionado:", monthchoosen.get())
            elgrupo=monthchoosen.get()
    def registroAlumnos():
        global num_control
        global nombre
        global ape_pat
        global ape_mat
        global ventana3
        global app
        ventana3=Tk()
        ventana3.title("Formulario de registro Alumno")
        ventana3.geometry("300x700")
        ventana3.configure(background="#F2F2F2")
        ventana3.iconbitmap("LogoTec.ico")
    
        #-------Menu 
        menubar = tk.Menu(ventana3)
        ventana3.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu Principal", command=Alumnos.cerrar)

        #Etiquetas
        etiqueta=Label(ventana3,text="Elige grupo",bg="gray",fg="white",font=("Arial",12))
        etiqueta.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        global monthchoosen
        n = tk.StringVar()
        monthchoosen = ttk.Combobox(ventana3, width = 10, textvariable = n)
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
        monthchoosen.bind("<<ComboboxSelected>>",Alumnos.selection_changed)

        numeroControl=Label(ventana3,text="Numero Control",bg="gray",fg="white",font=("Arial",12))
        numeroControl.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)

        num_control=Entry(ventana3)
        num_control.pack(padx=6,pady=6,ipady=2,ipadx=2,fill=X)

        etiqueta=Label(ventana3,text="Nombre",bg="gray",fg="white",font=("Arial",12))
        etiqueta.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        #Se crea el cuadro de texto
        nombre=Entry(ventana3)
        nombre.pack(padx=6,pady=6,ipady=5,ipadx=5,fill=X)

        el=Label(ventana3,text="Apellido Paterno",bg="gray",fg="white",font=("Arial",12))
        el.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)

        ape_pat=Entry(ventana3)
        ape_pat.pack(padx=6,pady=6,ipady=5,ipadx=5,fill=X)

        e2=Label(ventana3,text="Apellido Materno",bg="gray",fg="white",font=("Arial",12))
        e2.pack(padx=2,pady=2,ipady=1,ipadx=1,fill=X)
        ape_mat=Entry(ventana3)
        ape_mat.pack(padx=6,pady=6,ipady=5,ipadx=5,fill=X)
        boton=Button(ventana3,text="Registrar",fg="black",bg="#DAF7A6",width=13,command=Alumnos.insertar_datos)
        boton.pack(fill=X)
        #Botones
        #boton=Button(ventana3,text="Registrar",fg="black")
        #boton.pack(side=LEFT)
        
        app = MainFrame(ventana3)
        app.mainloop()
        ventana3.mainloop()
   
                
class MainFrame(Frame):
    global hilo1,isRun
    hilos=random.randint(1,101)
    def __init__(self, master=None):
        super().__init__(master, width=200, height=20)                
        self.master = master    
        self.master.protocol('WM_DELETE_WINDOW     ',self.askQuit)
        self.pack()
        
        self.hilo1 = threading.Thread(target=self.getSensorValues,daemon=True)#Crea un objeto hilo
        #daemon=True cuando se cierra el programa se cierra el proceso
        try:
            self.arduino = serial.Serial("COM3",57600,timeout=1.0)#tiempo de espera de la conexion 
            time.sleep(1)#esperar un segundo para aceder 
        except:
            print("Dispositivo no encontrado")
            self.hilo1.start()
        #variables de globales a nivel de clase
        
        self.create_widgets()
        self.isRun=True
        self.hilo1.start()#inicia el hilo que esta corriendo en una funcion

    def askQuit(self):
        self.isRun=False
        time.sleep(1.1)
        self.hilo1.join(0.1)#el hilo se detiene
        self.master.quit()# la ventana se cierra
        self.master.destroy()#se destruye la ventana
        from inicio import inicio
        print("*** finalizando...")
    def getSensorValues(self):#lee los valores de las funciones
        #---------------Esto es lo del arduino
        num=0
        list=""
        count = 0
        global numero
        numero=random.randint(1,128)
        print("Numero de enrolamiento",numero)
        while self.isRun: 
                num+=1
                #Opcion que registra a los usuarios
                opcion='E'
                try:
                    self.arduino.write(opcion.encode('ascii'))#metodo para enviar la cadena
                    cad =self.arduino.readline().decode('ascii')
                    time.sleep(0.5)
                    self.arduino.write(str(numero).encode('ascii'))
                    if cad != "":
                        TextBox.insert(END,str(cad)+"\n")
                        print(cad)
                        TextBox.yview(END)
                    count += 1
                
                    if(cad=="Encontrado"):
                        print("Paso lista")
                    hola=cad
                    list+=hola

                    if(num==19):
                        self.isRun=True
                        time.sleep(1.1)
                        self.hilo1.join(0.1)#el hilo se detiene
                        self.master.quit()# la ventana se cierra
                        self.master.destroy()
                        print(num," ------Saliendo---")
                        
                        break
                    #print(num)
                except:
                    messagebox.showinfo(message="dispositivo no encontrado",title="Aviso")
                    print("sensor no encontrado")
                    break               
    def create_widgets(self):
        global TextBox
        TextBox = ScrolledText( height='15', width='45', wrap=WORD)
        TextBox.pack(fill=BOTH, side=RIGHT, expand=True)
        #TextBox.grid(column=0, row=24, rowspan=8,  sticky=N+S+W)
"""  
def main(): 
    global window2
    window2 = Tk()
    window2.wm_title("Administradores")
    window2.geometry("300x500")
    app = MainFrame(window2)
    app.mainloop()"""
    
    
