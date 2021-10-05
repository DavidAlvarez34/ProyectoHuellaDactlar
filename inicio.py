import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox
from ventanaExportarExcel import ventanaGrupoExcel
import pymysql
import datetime
from tkinter import scrolledtext as st
from itertools import groupby
#----------Codigo externo----------
from RegistroRetardos import   RegistroLosRetardos
from grupo import Grupos
from muestraAlumnos import VerAlumnosVentana
from veradministradores import *
from EliminarAdministrador import eliminarAdninistrador
from EliminarAlumno import EliminarElAlumno
from EditarAlumno import EditarDatoAlumno
from EliminarTodo import *
from Lista import Milista
from ListaEliminar import MilistaEliminar
from registroAlumno import *
from PaseLista import PasarListaGrupo
num = 0;global bd
try:
    bd = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        db="bbdd"
    )
except:
    messagebox.showinfo(message="base de datos no conectada", title="Aviso")
    Tk().destroy()
    # ventana grupo
def ventanaGrupo():
    global ventana2
    ventana2 = tk.Tk()
    ventana2.title("Resgistra Grupo")
    ventana2.geometry("330x200")
    ventana2.configure(background="#F2F2F2")
    ventana2.iconbitmap("LogoTec.ico")
    global nombreGrupo_entry
    nombreGrupo_entry = StringVar()
    tk.Label(ventana2, text="Ingrese un nombre unico para identificar el grupo",
             bg="green", fg="white", width="250", height="3", font=("Arial", 15)).pack()
    tk.Label(ventana2, text="").pack()
    tk.Label(ventana2, text="Grupo").pack()
    nombreGrupo_entry = tk.Entry(ventana2)
    nombreGrupo_entry.pack()
    tk.Label(ventana2).pack()
    tk.Button(ventana2, text="Registrar", command=nuevoGrupo).pack()
    ventana2.mainloop()
    # Insertar datos
def funcionRegistro():
    ventana.destroy()
    Alumnos.registroAlumnos()
def funcionPaseLista():
    try:
        ventana.destroy()
        PasarListaGrupo.asistenciaAlumnos(unElemento)
    except:
        messagebox.showinfo(message="Elige el grupo", title="Aviso")
        Tk().destroy()
        inicio()
def funcionPasarRetardo():
    try:
        ventana.destroy()
        RegistroLosRetardos.asistenciaAlumnos(unElemento)
    except:
        messagebox.showinfo(message="Elige el grupo", title="Aviso")
        Tk().destroy()
        inicio()
def nuevoGrupo():
    cursor = bd.cursor()
    sql = "INSERT INTO grupo(iden_grupo) VALUES ('{0}')".format(
        nombreGrupo_entry.get())
    try:
        cursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitso", title="Aviso")
        ventana2.destroy()
        verGrupos()
        ventana.update()
    except:
        bd.rollback()
        messagebox.showinfo(message="Registro no exitso", title="Aviso")
        bd.close()
        return ventana2.destroy()
def myInfo():
    messagebox.showinfo(
        message="Programa Desarrollado por David Orea Alvarez 2021", title="Aviso")
def fecha():
    global subcadena
    try:
        cursor = bd.cursor()
        sql = "SELECT CURDATE();"

        # sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        cursor.execute(sql)
        bd.commit()
        myresult = cursor.fetchall()
        mifecha =""
        for x in myresult:
            mifecha=str(x)
        print(type(mifecha))
        l = [int(''.join(i)) for is_digit, i in groupby(mifecha, str.isdigit) if is_digit]
        fechalista=""
        for i in l:
            fechalista+=str(i)+"_"
        subcadena=fechalista[0:len(fechalista)-1]
        print(subcadena)
    except:
        bd.rollback()
        messagebox.showinfo(message="No hay Grupos", title="Aviso")
        bd.close()
fecha()
def insertar_datos(subcadena):
        cursor=bd.cursor()
        print("fecha que se va insertar: ",subcadena)
        sql=f"INSERT INTO mifecha(fecha_dia) VALUES ('{subcadena}')"#.format(num_control.get(),nombre.get(),ape_pat.get(),ape_mat.get(),str(n),elgrupo)
        #sql="CREATE TABLE Lista(num_control VARCHAR(15) NOT NULL,nombre_alumno VARCHAR(50),apellido_paterno VARCHAR(50),apellido_materno VARCHAR(50),ident_huella VARCHAR(10),iden_grupo VARCHAR(15),PRIMARY KEY (num_control),FOREIGN KEY (iden_grupo) REFERENCES grupo(iden_grupo))"
        try:
            cursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitso",title="Aviso")

        except (pymysql.Error)as e:
            bd.rollback()
            #messagebox.showinfo(message="Registro no exitso",title="Aviso")
            print("Fecha no insertada error: ",e)
            bd.close()
def insertar_columna():
    fechaHoy=subcadena
    print("Fecha de Hoy",fechaHoy)
    cursor = bd.cursor()
    # print(fecha)
    # Agregar una columna para pasar lista el dia de la clase
    sql = f"ALTER TABLE lista_{unElemento} add dia_{fechaHoy} varchar(50)"
    try:
        cursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitso", title="Aviso")
        insertar_datos(fechaHoy)
    except (pymysql.Error)as e:
        bd.rollback()
        messagebox.showinfo(message="Registro no exitso "+str(e), title="Aviso")
        ventana.destroy()
        inicio()
        bd.close()
def selection_changed(event):
    global unElemento
    unElemento = ""
    print("Nuevo elemento seleccionado:", monthchoosen.get())
    unElemento = str(monthchoosen.get())
    return unElemento
def verGrupos():
    global mygrupo
    try:
        cursor = bd.cursor()
        sql = "select * from grupo"
        # sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
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
def deleteAllFootprint():
    global valueSensor
    global opcion
    arduino = serial.Serial("COM3",57600,timeout=1.0)
    num=0
    time.sleep(1.5)
    isRun=True
    while isRun: 
        opcion='B'
        arduino.write(opcion.encode('ascii'))#metodo para enviar la cadena
        cad =arduino.readline().decode('ascii')
        num+=1
        if num == 6:
            isRun=False
            print("Saliendo")
            break
        print(num)
        print(cad)
def inicio():
    global unElemento
    global ventana
    ventana = tk.Tk()
    ventana.title("Bienvenido Profesor")
    ventana.geometry("330x300")
    ventana.configure(background="#F2F2F2")
    ventana.iconbitmap("LogoTec.ico")

    label2 = ttk.Label(ventana, text="Grupo").grid(column=2, row=0)
    n = tk.StringVar()
    global monthchoosen
    monthchoosen = ttk.Combobox(ventana, width=10, textvariable=n)

    verGrupos()
    # Adding combobox drop down list
    monthchoosen['values'] = mygrupo

    monthchoosen.grid(column=2, row=2)
    monthchoosen.current()
    monthchoosen.bind("<<ComboboxSelected>>", selection_changed)

    boton1 = tk.Button(ventana, text="Agregar Dia Lista", command=insertar_columna)
    boton1.grid(column=3, row=2)
    boton2=tk.Button(ventana, text="Registrar asistencia",command=funcionPaseLista)
    boton2.grid(column=4, row=2)
    label1 = ttk.Label(ventana, text="sensor")
    label1.grid(column=1, row=2)
    # Instaciar clase
    # print(pruebas.unElemento)
    # Crear el menun
    menubar = tk.Menu(ventana)
    ventana.config(menu=menubar)
    filemenu = tk.Menu(menubar, tearoff=0)
    present = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo Grupo", command=ventanaGrupo)
    filemenu.add_command(label="Editar Grupo",
                         command=Grupos.ventanaGrupoActualizar)
    filemenu.add_command(label="Eliminar grupo",
                         command=Grupos.ventanaGrupoEliminar)
    filemenu.add_command(label="Exportar un grupo a excel",
                         command=ventanaGrupoExcel)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=ventana.quit)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Crea una lista", command=Milista.registroLista)
    editmenu.add_command(label="Agregar nuevo Alumno", command=funcionRegistro)
    editmenu.add_command(label="Ver Alumnos de una lista",
                         command=VerAlumnosVentana.ventanaAlumnoEliminar)
    editmenu.add_command(label="Editar Alumno",
                         command=EditarDatoAlumno.ventanaAlumnoEligeGrupo)
    editmenu.add_command(label="Eliminar Alumno",
                         command=EliminarElAlumno.ventanaAlumnoEliminar)
    editmenu.add_command(label="Eliminar Lista",
                         command=MilistaEliminar.eliminaLista)
    helpmenu = tk.Menu(menubar, tearoff=0)
    # helpmenu.add_command(label="Agregar Nuevo Administrador")
    helpmenu.add_command(label="Ver administrador", command=verAdministrador)
    helpmenu.add_command(label="Eliminar administrador",command=eliminarAdninistrador.ventanaAdministradorEliminar)
    helpmenu.add_command(label="Eliminar todas las huellas",command=deleteAllFootprint)

    present.add_command(label="Registrar retardos",command=funcionPasarRetardo)
    present.add_command(label="Editar Pase de Lista")
    
    helpmenu.add_command(label="Acerca de...", command=myInfo)
    menubar.add_cascade(label="Grupo", menu=filemenu)
    menubar.add_cascade(label="Lista Alumnos", menu=editmenu)
    menubar.add_cascade(label="Asistencia", menu=present)
    menubar.add_cascade(label="Administrador", menu=helpmenu)
    ventana.mainloop()
inicio()
