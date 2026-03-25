from tkinter import *

root = Tk()
root.geometry('400x280')
root.title('Piter es joto')

#en py cuanto intentamos modificar una variable externa dentro de una función
#hay una palabra clave especial 
counter = 0
a = Label(root, text=f"Probando ando {str(counter)} ",  foreground="white", background="black")
a.pack(padx=20)
    
def Click():
    #proyectos reales global se evita, tal vez haciendola una clase?
    #simon
    
    global counter
    counter += 1
    if counter == 25:
        button.config(text="ya no c puede", state="disabled")
        resButton.config(bg="red")
    else:
        button.config(state="normal")
        resButton.config(bg="green") 
    #config: metodo que tienen todos los widgets para modificar las propiedades después de crearlos
    #cuando creamos un widget, le pasamos propiedades, ex. text="", bg="".
    #eso solo lo configurea en el momento. si después queremos cambiasr algo usamos .config()  
    number.config(text=str(counter))    
    a.config(text="Numero: "+str(counter))        
    print(counter)
        
    
def restart_Counter():
    global counter
    counter = 0
    button.config(text="Click Heree", state="normal" )
    resButton.config(bg="green")
    a.config(text="Numero: "+str(counter))
    number.config(text = str(counter))
    
    
    
    
    
number = Label(root , text=str(counter))
number.pack()

resButton = Button(root, bg="dark cyan", text="Restart Here", command=restart_Counter)
resButton.pack(pady=20)

button = Button(root , bg="dark green" ,text="Click Here", command=Click)
button.pack()


root.mainloop()