from tkinter import *
from tkinter import messagebox
from tkinter import StringVar, ttk
import tkinter as tk
import pymysql
import xlsxwriter
import mysql.connector

def export():
    global table_name
    table_name=f"lista_{elgrupo}"
    print(table_name)
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(table_name + '.xlsx')
    worksheet = workbook.add_worksheet('MENU')

    # Create style for cells
    header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': '#2ECC71'})
    body_cell_format = workbook.add_format({'border': True})

    header, rows = fetch_table_data(table_name)

    row_index = 0
    column_index = 0

    for column_name in header:
        worksheet.write(row_index, column_index, column_name, header_cell_format)
        column_index += 1

    row_index += 1
    for row in rows:
        column_index = 0
        for column in row:
            worksheet.write(row_index, column_index, column, body_cell_format)
            column_index += 1
        row_index += 1

    print(str(row_index) + ' rows written successfully to ' + workbook.filename)

    # Closing workbook
    workbook.close()

def fetch_table_data(table_name):
    try:
        # The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
        cnx = mysql.connector.connect(
            host='localhost',
            database='bbdd',
            user='root',
            password=''
        )

        cursor = cnx.cursor()
        cursor.execute('select * from ' + table_name)

        header = [row[0] for row in cursor.description]

        rows = cursor.fetchall()

        # Closing connection
        cnx.close()
    except:
        messagebox.showinfo(message="No hay Grupos", title="Aviso")
         
    return header, rows


def selection_changed(event):
    global elgrupo
    print("Nuevo elemento seleccionado:", monthchoosen.get())
    elgrupo=monthchoosen.get()
def ventanaGrupoExcel():
    global ventana2
    ventana27 = tk.Tk()
    ventana27.title("Grupo")
    ventana27.geometry("330x200")
    ventana27.configure(background="#F2F2F2")
    ventana27.iconbitmap("LogoTec.ico")
    tk.Label(ventana27,text="Lista A excel",bg="green",fg="white",width="250",height="3",font=("Arial",15)).pack()

    tk.Label(ventana27,text="").pack()
    global monthchoosen
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(ventana27, width=10, textvariable=n)
    try:
        bd = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="bbdd"
        )
        cursor = bd.cursor()
        sql = "select * from grupo"
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
    monthchoosen['values'] =mygrupo
    
    monthchoosen.pack()
    monthchoosen.current()
    monthchoosen.bind("<<ComboboxSelected>>",selection_changed)
    tk.Label(ventana27,text="").pack()
    tk.Button(ventana27,text="Envia a excel",command=export).pack()
    ventana27.mainloop()
