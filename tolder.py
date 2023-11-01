
import tkinter as tk

def calcular_pares():
    inicio = int(entrada_inicio.get())
    fin = int(entrada_fin.get())
    numeros_pares = [str(num) for num in range(inicio,fin + 1) if num % 2 == 0]
    resultado.set(", ". join(numeros_pares)) 
    
def boton_presionado():
    calcular_pares()
    
#crea una ventana tkinter

ventana = tk.Tk()
ventana.title("calculadora de numeros pares")
#crear configuracion de ventana 

ventana.configure(bg="lightblue")

#crear etiqueta de fondo y texto de colores personalizados



etiqueta_inicio = tk.Label(ventana, text="calculadora de numeros pares ", bg="blue", fg="white")
etiqueta_inicio.pack()

entrada_inicio = tk.Entry(ventana)
entrada_inicio.pack()

etiqueta_fin = tk.Label(ventana, text="fin ",)
etiqueta_fin.pack()

entrada_fin = tk.Entry(ventana)
entrada_fin.pack()
#variable para mostrar resultado 

resultado = tk.StringVar()
resultado_label = tk.Label(ventana,textvariable=resultado)
resultado_label.pack()

#crear boton calcular
boton_calcular = tk.Label(ventana,text="CALCULAR", bg="green", fg="white")
boton_calcular.config(command=boton_presionado)
boton_calcular.pack()

#iniciar la ventana

ventana.mainloop()