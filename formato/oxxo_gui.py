from tkinter import *
ventana = Tk()
ventana.geometry("600x400")
ventana.title('gui')
ventana.iconbitmap('imgs/maicra.ico')
num = 0

frame1 = Frame(ventana)
frame1.configure(width=300, height=200, bg="red", bd=5)
frame1.pack()

frame2 = Frame(frame1)
frame2.configure(width=100, height=100, bg="indigo", bd=5)
frame2.pack()

labelframe = LabelFrame(frame1, text="Naco estupido", bg="light cyan", padx=10, pady=10,bd=0)
labelframe.configure(width=300, height=100)
labelframe.pack()




def resize_frame():
    global num
    colores = ['blue', 'green', 'red','light cyan','white']
    num+=1
    if num == len(colores):
        num = 0
    #frame2.config(width=500,height=100, bg=colores[num])
    frame1.config(bg=colores[num])
    btn1.config(bg=colores[num])

btn1 = Button(frame1, text="Hola", command=resize_frame)
btn1.pack(pady=20)



#osease que frame 1 se ajusta al tamaño del frame 2


"""
frame1 se encoje para ajustarse a su contenido (frame2)
en lugar de mantener el 300x200

frame1.propagate(False) evita que se encoja
"""

#bd = border



ventana.mainloop()
