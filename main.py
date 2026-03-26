from pptx import *
import os
prs = Presentation("formato_3.pptx")
veces = 1
def get_value(filename="log.txt"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val


formato = ["EJEMPLO", "Salvia 116", "10:00 PM", "Lunes 20 de junio del 2025"]


"""
font_style = text_frame.paragraphs[0].runs[0].font
text_frame.clear()
run = text_frame.paragraphs[0].add_run()
run.font = font_style

"""

if prs:
    print("inicio")
else:
    print('no se encontró el formato')
    
slide = prs.slides[0]

"""""
             for paragraph in shape.text_frame.paragraphs:                 for run in paragraph.runs:                     run.text = "Hola"                     
             print(run.text)
"""

    


for shape in slide.shapes:

    if shape.name == 'colonia':
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                run.text = formato[0]                                                                
    elif shape.name == 'lugar':
        
        for paragraph in shape.text_frame.paragraphs:

            for run in paragraph.runs:
                shape.text_frame.clear()
                run.text = formato[1]                
                #for run in paragraph.runs:             
                # run.text = formato[1]
                # print(run.text)
        
    elif shape.name == 'hora':
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                    run.text = formato[2]      
                    print(run.text)              
                
    elif shape.name == 'fecha':
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    print(run.text)


    
contador = get_value()
print(f"guardado: {contador}" )
prs.save(f"{contador}.pptx")