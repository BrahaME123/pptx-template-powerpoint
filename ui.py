import customtkinter
from pptx_handler import generar_power
from tkinter import filedialog, messagebox
from tkinter import ttk
import os 
from utils import *
class App:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        self.root = customtkinter.CTk()
        self.root.title("Generar PowerPoint")
        self.root.geometry('1200x950')
        self.root.iconbitmap('')
        self.style = ttk.Style()
        self.style.theme_use("vista")
        self.style.configure("Treeview", background = "black",foreground = "white", fieldbackground = "light cyan")
        self._build_ui()        
        
        
    def _build_ui(self):
        
     
        
        def Login():
            colonia_valor = entry1.get()
            fecha_valor = entry2.get()
            hora_valor = entry3.get()
            lugar_valor = lugar.get()
            
            
            if not colonia_valor or not fecha_valor or not hora_valor or not lugar_valor:
                resultado_label.configure(text = "Llena todos los campos para generar el archivo correctamente.")
                return
            
            carpeta = crear_carpeta()
            nombre_archivo = f"{colonia_valor}_{fecha_valor}.pptx"
            ruta = os.path.join(carpeta, nombre_archivo)

            
            
            if not ruta:
                return 
            archivo = generar_power(colonia_valor, lugar_valor,fecha_valor,hora_valor,ruta)
            resultado_label.configure(text=f"Archivo generado correctamente. {ruta}")
            print(f'powerpoint generado: {ruta} ')
            nombre_archivo = os.path.basename(ruta)
            agregar_archivo(nombre_archivo,ruta)
            cargar_tabla()
        
        def Salir():
            self.root.destroy()
           
           
           
        def eliminar_archivo():
            
            selected = tabla.selection()
            
            if not selected:
                messagebox.showwarning("Error", "No ha seleccionado un archivo para eliminar")
                return
            
            ruta = tabla.item(selected[0])["values"][1]
            
        
            
            if os.path.exists(ruta):
                os.remove(ruta)
                for row in tabla.get_children():
                 if tabla.item(row)["values"][1] == ruta:
                    tabla.delete(row)
                    break
                eliminar_json(ruta)
            else:
                messagebox.showerror("Error", "La convocatoria no existe.")    
            
            print(ruta)
            
            
        def crear_carpeta():
            
            directorio =  os.path.join(os.path.expanduser("~"),"Documentos")
            carpeta = os.path.join(directorio,"CONVOCATORIAS GENERADAS")
            if not os.path.exists(carpeta):
                os.makedirs(carpeta, exist_ok=True)
                print(f"carpeta creada: {carpeta} ")
        
            return carpeta
          
        def abrir_archivo():
            selected = tabla.selection()
            
            if not selected:
                messagebox.showwarning("Error", "No ha seleccionado una convocatoria para abrir")
                return
            
            item = tabla.item(selected[0])
            ruta = item["values"][1]
            if os.path.exists(ruta):
                os.startfile(ruta)
            else:
                messagebox.showerror("Error", "La convocatiroa no existe.")
            
        
                    
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        
                
        label = customtkinter.CTkLabel(master=frame, text="Generar PowerPoint", font=("Verdana", 24))
        label.pack(pady=12, padx=10)
        
        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Colonia: ")
        entry1.pack(pady=12, padx=10)
        
        entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Fecha: ")
        entry2.pack(pady=12, padx=10)
        
        entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Hora: ")
        entry3.pack(pady=12, padx=10)
        
        lugar = customtkinter.CTkEntry(master=frame, placeholder_text="Lugar: ")
        lugar.pack(pady=12, padx=10)
        
        
        frame2 =  customtkinter.CTkFrame(master=self.root)
        
        button = customtkinter.CTkButton(master=frame2, text="Generar", command=lambda:(crear_carpeta(), Login()) , hover_color="black" )
        button.grid(row = 0, column = 0, padx=10) 
        resultado_label = customtkinter.CTkLabel(master=frame, text="")
        resultado_label.pack(pady=5)         
        
        exit = customtkinter.CTkButton(master=frame2, text="Salir", command=Salir, hover_color="red")
        exit.grid(row = 0, column = 1, padx=10) 
        
        abrir = customtkinter.CTkButton(master=frame2, text="Abrir Convocatoria", command=abrir_archivo, hover_color="green")
        abrir.grid(row = 0, column = 2, padx=10) 
        eliminar = customtkinter.CTkButton(master=frame2, text="Eliminar Convocatoria", command=eliminar_archivo, hover_color="red")
        eliminar.grid(row = 0, column = 3, padx=10)

        frame2.pack(padx=20, pady=10)
    
        # frame2 = customtkinter.CTkFrame(master=self.root)
        # frame2.pack(pady=10, padx=60, fill="x")
        
        # frame2.columnconfigure(0, weight=1)
        # frame2.columnconfigure(1, weight=1)
        
        
        
        # titulo2 = customtkinter.CTkLabel(master=frame2, text="Archivos Generados Anteriormente", font=("Verdana", 18))
        # titulo2.grid(row=0, column=0, columnspan=2, pady=15, padx=10)
         


        # guardados = customtkinter.CTkLabel(master=frame2,text="Archivos: ")
        # guardados.grid(row=1,column=0, columnspan=2, pady=5,padx=15, sticky="w")    
        # texto1 = customtkinter.CTkLabel(master=frame2, text="ejemplo")
        # texto1.grid(row=1, column=0, columnspan=2, pady=15, padx=6)
        
        # texto2 = customtkinter.CTkLabel(master=frame2, text="ejemplo")
        # texto2.grid(row=1, column=0, columnspan=2, pady=15, padx=6)
        
        # info = customtkinter.CTkLabel(master=frame2, text="Lorem Ipsum",)
        # info.grid(row=3, column=0, columnspan=2, pady= 20, padx=10)
        tabla = ttk.Treeview(frame, columns= ('Nombre', "Direccion"), show='headings')
        tabla.heading('Nombre', text="Archivo")
        tabla.heading('Direccion', text="Direccion del Archivo")
        tabla.column('Nombre', width=500)
        tabla.column('Direccion', width=900)
        tabla.pack(padx=10, pady=20)
        #datos en la tabls
        def cargar_tabla():
            for fila in tabla.get_children():
                tabla.delete(fila)
                
            datos = cargar_info()
            for item in datos:
                tabla.insert("", 'end', values=(item["nombre"], item["ruta"]))
            
        cargar_tabla()
        
        
    def run(self):
        self.root.mainloop()
        