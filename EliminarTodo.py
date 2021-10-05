import pymysql
import tkinter as tk
from tkinter import StringVar, ttk ,messagebox
import serial,time

def eliminarTodo1():
    base=pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        db="bbdd"
    )
    cursor=base.cursor()
    sql="DELETE FROM login"
    try:
        
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
    
        cursor.execute(sql)
        base.commit()
        #messagebox.showinfo(message="Eliminado exitso",title="Aviso")
        base.close()
        eliminarTodo3()
    except:
        #bd.rollback()
        messagebox.showinfo(message="Eliminado no exitso",title="Aviso")
        #bd.close()
    #return bd.close()

def eliminarTodo2():
    bd=pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        db="bbdd"
    )
    try:
        cursor=bd.cursor()
        sql="DELETE FROM alumno"
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        cursor.execute(sql)
        bd.commit()
        #messagebox.showinfo(message="Eliminado exitso",title="Aviso")
        bd.close()
        eliminarTodo3()
    except:
        bd.rollback()
        #messagebox.showinfo(message="Eliminado no exitso",title="Aviso")
        bd.close()
    return bd.close()
def eliminarTodo3():
    bd=pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        db="bbdd"
    )
    try:
        cursor=bd.cursor()
        sql="DELETE FROM grupo"
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
    
        cursor.execute(sql)
        bd.commit()
        #messagebox.showinfo(message="Eliminado exitso",title="Aviso")
        pasarLista()
        bd.close()
    except:
        bd.rollback()
        #messagebox.showinfo(message="Eliminado no exitso",title="Aviso")
        bd.close()
    return bd.close()
def pasarLista():
    try:        
        global valueSensor
        arduino = serial.Serial("COM3",57600,timeout=1.0)
        num=0
        time.sleep(1)
        isRun=True
        list=""
        while isRun: 
            num+=1
            opcion='B'
            arduino.write(opcion.encode('ascii'))#metodo para enviar la cadena
            cad =arduino.readline().decode('ascii')
            print(cad)
            hola=cad
            list+=hola

            if(num==10):
                print(num)
                break
            print(num)
        print("Una lista: ",list)
    except:
         messagebox.showinfo(message="Dispositivo no coenctado",title="Aviso")