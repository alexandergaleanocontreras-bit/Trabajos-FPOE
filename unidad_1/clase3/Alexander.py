from tkinter import Frame, Tk
from tkinter.messagebox import askyesno

principal = Tk()
principal.title('prueba de eventos')

def digitar_letra(evento):
    print("digitaste la letra", repr(evento.char))

def click_izquierdo(event):
    frame.focus_set()
    print("clickeado en: ", event.x, event.y)

def el_usuario_quiere_salir():
    if askyesno('Salir de la aplicacion', '¿Seguro que quieres cerrar la aplicacion?'):
        principal.destroy()

frame = Frame(principal, width=500, height=500)
frame.bind("<Key>", digitar_letra)
frame.bind("<Button-1>", click_izquierdo)
frame.pack()
frame.focus_set()

principal.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)

principal.mainloop()  
