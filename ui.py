import customtkinter
from pptx_handler import generar_power
from tkinter import filedialog
class App:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        
        self.root = customtkinter.CTk()
        self.root.title("Generar Invitación")
        self.root.geometry('1000x600')

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
            
            ruta = filedialog.asksaveasfilename(defaultextension=".pptx", filetypes=[("PowerPoint", "*.pptx")])
            
            if not ruta:
                return
            archivo = generar_power(colonia_valor, lugar_valor,fecha_valor,hora_valor,ruta)
            resultado_label.configure(text=f"Archivo generado correctamente. {archivo}.pptx")
            print(f'powerpoint generado: {archivo}.pptx ')
        
        def Salir():
            self.root.destroy()
            
                    
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
        
        button = customtkinter.CTkButton(master=frame, text="Generar", command=Login, hover_color="black" )
        button.pack(pady=12, padx=10) 
        resultado_label = customtkinter.CTkLabel(master=frame, text="")
        resultado_label.pack(pady=10) 
        
        
        exit = customtkinter.CTkButton(master=frame, text="Salir", command=Salir, hover_color="red")
        exit.pack(pady=20, padx = 15)
        
    
    
    def run(self):
        self.root.mainloop()
        