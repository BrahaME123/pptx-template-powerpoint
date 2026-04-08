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
        self.x, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.x, self.h-80))
        self.root.title("Generar Convocatoria")
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
            mensaje_valor = mensaje_abajo.get()
            acompañado_valor = acompañado_por.get()
            
            if not colonia_valor or not fecha_valor or not hora_valor or not lugar_valor or not mensaje_valor or not acompañado_valor:
                resultado_label.configure(text = "Llena todos los campos para generar el archivo correctamente.")
                return
            
            else:
                carpeta = crear_carpeta()
                nombre_archivo = f"{colonia_valor}_{fecha_valor}.pptx"
                ruta = os.path.join(carpeta, nombre_archivo)

                
                
                if not ruta:
                    return 
                archivo = generar_power(colonia_valor, lugar_valor,fecha_valor,hora_valor,ruta, mensaje_valor, acompañado_valor)
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
                resultado_label.configure(text="No se ha seleccionado ningun archivo para eliminar, selecciona uno de la tabla primero.")
                return
            
            ruta = tabla.item(selected[0])["values"][1]
            
        
            
            if os.path.exists(ruta):
                os.remove(ruta)
                for row in tabla.get_children():
                 if tabla.item(row)["values"][1] == ruta:
                    tabla.delete(row)
                    break
                eliminar_json(ruta)
                resultado_label.configure(text="ARCHIVO ELIMINADO CORRECTAMENTE.")
            else:
                resultado_label.configure(text="La convocatoria que intentas eliminar no existe.")
            
            print(ruta)
            
            
        def crear_carpeta():
            
            directorio =  os.path.join(os.path.expanduser("~"),"Documentos")
            carpeta = os.path.join(directorio,"CONVOCATORIAS GENERADAS")
            if not os.path.exists(carpeta):
                os.makedirs(carpeta, exist_ok=True)
                print(f"carpeta creada: {carpeta} ")
            
            return carpeta

        def abrir_carpeta(carpeta):
            if os.path.exists(carpeta):
                os.startfile(carpeta)
            else:
                resultado_label.configure(text="La carpeta donde se guardan las convocatorias no existe.")
          
          
        def abrir_archivo():
            selected = tabla.selection()
            
            if not selected:
                resultado_label.configure(text="No ha seleccionado una convocatoria para abrir.")
                return
            
            item = tabla.item(selected[0])
            ruta = item["values"][1]
            if os.path.exists(ruta):
                os.startfile(ruta)
            else:
                resultado_label.configure(text="La convocatoria que intentas abrir no existe.")
            
        
                    
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
                
        label = customtkinter.CTkLabel(master=frame, text="Generar Convocatoria", font=("Verdana", 24))
        label.pack(pady=12, padx=10)
        
        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Colonia: ")
        entry1.pack(pady=12, padx=10)
        
        entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Fecha: ")
        entry2.pack(pady=12, padx=10)
        
        entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Hora: ")
        entry3.pack(pady=12, padx=10)
        
        lugar = customtkinter.CTkEntry(master=frame, placeholder_text="Lugar: ")
        lugar.pack(pady=12, padx=10)
        
        mensaje_abajo = customtkinter.CTkEntry(master=frame, placeholder_text="Mensaje adicional.", width=340,  height=90)
        mensaje_abajo.pack(pady=12, padx=10)
         
        acompañado_por = customtkinter.CTkEntry(master=frame, placeholder_text="Acompañados por: ",  width=300)
        acompañado_por.pack(pady=12,padx=10)
        
        frame2 =  customtkinter.CTkFrame(master=self.root)
        
        button = customtkinter.CTkButton(master=frame2, text="Generar", command=lambda:(crear_carpeta(), Login(), abrir_carpeta(carpeta=crear_carpeta())) , hover_color="black" )
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
    
      
        tabla = ttk.Treeview(frame, columns= ('Nombre', "Direccion"), show='headings')
        tabla.heading('Nombre', text="Archivo")
        tabla.heading('Direccion', text="Direccion del Archivo")
        tabla.column('Nombre', width=500, anchor = 'center')
        tabla.column('Direccion', width=900 , anchor = 'center')
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
        