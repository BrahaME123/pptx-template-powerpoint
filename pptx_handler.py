from pptx import *
import os


def generar_power(colonia, lugar, fecha, hora, ruta):
    prs = Presentation("formato_3.pptx")

    def get_value(filename="log.txt"):
        with open(filename, "a+") as f:
            f.seek(0)
            val = int(f.read() or 0) + 1
            f.seek(0)
            f.truncate()
            f.write(str(val))
            return val

    veces = 1


    if prs:
        print("inicio")
    else:
        print('no se encontró el formato')
        
    slide = prs.slides[0]
            
    def replace_text(shape,new_text):
        if not shape.has_text_frame:
            return
        for paragraph in shape.text_frame.paragraphs:
            if paragraph.runs:
                paragraph.runs[0].text = new_text
                for run in paragraph.runs[1:]:
                    run.text = ""
                break


    


    for shape in slide.shapes:

        if shape.name == 'colonia':
            replace_text(shape, colonia)
                                                                        
        elif shape.name == 'lugar':
            replace_text(shape, lugar)
            
        elif shape.name == 'hora':
            replace_text(shape, hora)
        elif shape.name == 'fecha':
            replace_text(shape,fecha)

    contador = get_value()
    nombre_archivo = f"{contador}.pptx"
    prs.save(ruta)
    os.startfile(ruta)
    return ruta

    