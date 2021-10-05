from tkinter import *
from tkinter.scrolledtext import *
import pymysql
from tkinter import messagebox
def verAdministrador():
    window2 = Tk()
    window2.wm_title("Administradores")
    window2.geometry("500x200")
    TextBox = ScrolledText(window2, height='10', width='45', wrap=WORD)
    bd=pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="bbdd"
            )
        
    try:
        cursor=bd.cursor()
        sql="select * from login"
        #sql="CREATE TABLE Grupo (iden_grupo VARCHAR(15) NOT NULL, PRIMARY KEY (iden_grupo))"
        cursor.execute(sql)
        bd.commit()
        myresult = cursor.fetchall()
        mygrupo=[]
        for x in myresult:
            mygrupo.append(x)
    except:
        bd.rollback()
        messagebox.showinfo(message="No hay administradores",title="Aviso")
        bd.close()
        #Just adds 100 lines to the TextBox
    count = 0
    while(count<len(mygrupo)):

        TextBox.insert(END, str(count)+":" +str(mygrupo[count])+"\n")

            #Pushes the scrollbar and focus of text to the end of the text input.
        TextBox.yview(END)
        count += 1
    TextBox.pack(fill=BOTH, side=LEFT, expand=True)

    window2 = mainloop()

    
