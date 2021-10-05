from tkinter import *
from tkinter.scrolledtext import *
import pymysql
from tkinter import messagebox
from tkinter import StringVar, ttk ,messagebox  
class VerAlumnosVentana:
    def selection_changed(event):
        global elgrupo
        print("Nuevo elemento seleccionado:", monthchoosen.get())
        elgrupo=monthchoosen.get()
        ventana34.destroy()
        VerAlumnosVentana.verAlumnos()
    def ventanaAlumnoEliminar():
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
        monthchoosen.bind("<<ComboboxSelected>>",VerAlumnosVentana.selection_changed)

        #------------------------------------Otro Elemento
        Label(ventana34).pack()
        #tk.Button(ventana34,text="Eliminar",command=EliminarElAlumno.eliminarAdministrador).pack()
        ventana34.mainloop()
    def verAlumnos():
        window = Tk()
        window.wm_title("Scroll From Bottom")
        window.geometry("500x200")
        TextBox = ScrolledText(window, height='10', width='45', wrap=WORD)
        bd=pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="bbdd"
            )
        
        try:
            cursor=bd.cursor()
            sql=f"select * from lista_{elgrupo}"
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
        #Just adds 100 lines to the TextBox
        count = 0
        while(count<len(mygrupo)):

            TextBox.insert(END, str(count)+":" +str(mygrupo[count])+"\n")

            #Pushes the scrollbar and focus of text to the end of the text input.
            TextBox.yview(END)
            count += 1
        TextBox.pack(fill=BOTH, side=LEFT, expand=True)

        window = mainloop()

