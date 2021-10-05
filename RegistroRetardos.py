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
from itertools import groupby
import re
class RegistroLosRetardos():
    def insertar_datos():
        bd = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        
        # sql=f"INSERT INTO Lista_{elgrupo}(num_control,nombre_alumno,apellido_paterno,apellido_materno,ident_huella,iden_grupo) VALUES ('{num_control.get()}','{nombre.get()}','{ape_pat.get()}','{ape_mat.get()}','{str(numero)}','{elgrupo}')"#.format(num_control.get(),nombre.get(),ape_pat.get(),ape_mat.get(),str(n),elgrupo)
        #sql="CREATE TABLE Lista(num_control VARCHAR(15) NOT NULL,nombre_alumno VARCHAR(50),apellido_paterno VARCHAR(50),apellido_materno VARCHAR(50),ident_huella VARCHAR(10),iden_grupo VARCHAR(15),PRIMARY KEY (num_control),FOREIGN KEY (iden_grupo) REFERENCES grupo(iden_grupo))"
        #---UPDATE alumnos SET curso='secundaria' WHERE curso='primaria'---
        time.sleep(0.4)
        presencia="Retardo"
        try:
            cursor = bd.cursor()
            for i in list2:
                sql=f"UPDATE lista_{elegirGrupo} SET dia_{mifecha}='{presencia}' WHERE ident_huella='{str(i)}'"
                cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitso", title="Aviso")
        except:
            bd.rollback()
            messagebox.showinfo(message="Registro no exitso", title="Aviso")
            bd.close()
    def obtenerIdentificador():
        global list2
        #Patron para encontrar los id de las huellas 
        patron = re.compile('#[0-9]+')
        #una varible que ejecuta el patron
        hola= patron.findall(lista)
        print(hola)
        #Elimina los elementos repetidos
        list2=list(set(hola))
        print("Esto ya es el identificador: ",list2)
        time.sleep(0.2)
        RegistroLosRetardos.insertar_datos()
    def cerrar():
        from inicio import inicio
        ventana3.destroy()

        print("Hola")

    def selection_changed(event):
        global mifecha
        print("Nuevo elemento seleccionado:", monthchoosen.get())
        mifecha = monthchoosen.get()

    def asistenciaAlumnos(mielemento):
        global ventana3
        global app
        global elegirGrupo
        elegirGrupo=mielemento
        print("Psar lista al grupo: ",elegirGrupo)
        ventana3 = Tk()
        ventana3.title("Formulario de registro Alumno")
        ventana3.geometry("300x700")
        ventana3.configure(background="#F2F2F2")
        ventana3.iconbitmap("LogoTec.ico")

        # -------Menu
        menubar = tk.Menu(ventana3)
        ventana3.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu Principal",
                            command=RegistroLosRetardos.cerrar)

        # Etiquetas
        etiqueta = Label(ventana3, text="Elige fecha",
                         bg="gray", fg="white", font=("Arial", 12))
        etiqueta.pack(padx=2, pady=2, ipady=1, ipadx=1, fill=X)
        #--------Seleccionar la fecha---------
        global monthchoosen
        n = tk.StringVar()
        monthchoosen = ttk.Combobox(ventana3, width=10, textvariable=n)
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
        monthchoosen['values'] = mygrupo
        monthchoosen.pack()
        monthchoosen.current()
        monthchoosen.bind("<<ComboboxSelected>>",
                          RegistroLosRetardos.selection_changed)
        # -------------Muestra el pase de lista----{-----------}
        app = MainFrame(ventana3)
        app.mainloop()
        ventana3.mainloop()
# PasarListaGrupo.fecha()
# PasarListaGrupo.asistenciaAlumnos()
class MainFrame(Frame):
    global hilo1, isRun
    def __init__(self, master=None):
        super().__init__(master, width=200, height=20)
        self.master = master
        #self.master.protocol('WM_DELETE_WINDOW     ', self.askQuit)
        self.pack()
        self.hilo2 = threading.Thread(
            target=self.getSensorValues, daemon=True)  # Crea un objeto hilo
        # daemon=True cuando se cierra el programa se cierra el proceso
        try:
            # tiempo de espera de la conexion
            self.arduino = serial.Serial("COM3", 57600, timeout=1.0)
            time.sleep(1)  # esperar un segundo para aceder
        except:
            print("Dispositivo no encontrado")
            # self.hilo2.start()
        # variables de globales a nivel de clase

        self.create_widgets()
        self.isRun = True
        self.hilo2.start()  # inicia el hilo que esta corriendo en una funcion

    def askQuit(self):
        self.isRun = False
        time.sleep(1.1)
        self.hilo2.join(0.1)  # el hilo se detiene
        self.master.quit()  # la ventana se cierra
        self.master.destroy()  # se destruye la ventana
        from inicio import inicio
        print("*** finalizando...")

    def getSensorValues(self):  # lee los valores de las funciones
        # ---------------Esto es lo del arduino
        global lista
        num = 0
        lista = ""
        count = 0
        
        while self.isRun:
            num += 1
            # Opcion que registra a los usuarios
            opcion = 'H'
            try:
                # metodo para enviar la cadena
                self.arduino.write(opcion.encode('ascii'))
                cad = self.arduino.readline().decode('ascii')
                TextBox.insert(END, str(cad)+"\n")
                print(cad)
                TextBox.yview(END)
                count += 1
                hola = cad
                lista += hola
                if(num == 19):
                    print("Saliendo")
                    RegistroLosRetardos.obtenerIdentificador()
                    break
                #self.arduino.write(str(numero).encode('ascii'))
                """TextBox.insert(END, str(cad)+"\n")
                print(cad)
                TextBox.yview(END)
                count += 1
                hola = cad
                list += hola
                if(num == 19):
                    self.isRun = True
                    time.sleep(1.1)
                    self.hilo2.join(0.1)  # el hilo se detiene
                    self.master.quit()  # la ventana se cierra
                    self.master.destroy()
                    print(num, " ------Saliendo---")
                    print(list)
                    break"""
                # print(num)
            except:
                messagebox.showinfo(
                    message="dispositivo no encontrado", title="Aviso")
                print(list)
                print("sensor no encontrado")
                break

    def create_widgets(self):
        global TextBox
        TextBox = ScrolledText(height='15', width='45', wrap=WORD)
        TextBox.pack(fill=BOTH, side=RIGHT, expand=True)
        #TextBox.grid(column=0, row=24, rowspan=8,  sticky=N+S+W)
