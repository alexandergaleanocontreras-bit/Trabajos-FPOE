from tkinter import Frame, Tk
from tkinter.messagebox import askyesno

principal = Tk()
principal.title ("prueba de eventos")

def digitar_letra(evento):
    print("digitaste la letra",repr(evento.char))

def click_izquierdo(event):
    Frame.focus_set()
    print("clickeado en:", event.x, event.y)
def el_usuario_quiere_salir():
    if askyesno("salir de la aplicacion", "¿Estás seguro de que quieres salir"):
        principal.destroy()

Frame = Frame(principal, width=500, height=500)
Frame.bind("<Key>", digitar_letra)
Frame.bind("<Button-1>",click_izquierdo)
Frame.focus_set()

principal.protocol("WM_DELETE_WINDOW",el_usuario_quiere_salir)
principal.mainloop()