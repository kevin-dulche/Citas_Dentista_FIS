from Login import *

class VentanaPaciente:
    def __init__(self, usuario):
        self.ventana = Tk()
        self.ventana.title("Paciente" + " - " + usuario[1])

        # Centrar la ventana en la pantalla
        self.centrar_ventana()

        # Evitar que la ventana cambie de tamaño
        self.ventana.resizable(0, 0)

        # Crear un objeto Canvas
        canvas = Canvas(self.ventana, width=800, height=600)
        canvas.pack()

        lbPaciente = Label(self.ventana, text="Paciente", font=("Arial", 20, "bold"), anchor="center")
        lbPaciente.place(x=340, y=20, width=120, height=30)

        botonAltaPaciente = Button(self.ventana, text="Alta", font=("Arial", 16), anchor="center")
        botonAltaPaciente.place(x=87.5, y=70, width=150, height=50)

        botonBajaPaciente = Button(self.ventana, text="Baja", font=("Arial", 16), anchor="center")
        botonBajaPaciente.place(x=325, y=70, width=150, height=50)

        botonModificarPaciente = Button(self.ventana, text="Modificar", font=("Arial", 16), anchor="center")
        botonModificarPaciente.place(x=562.5, y=70, width=150, height=50)

        # Dibujar una línea horizontal
        canvas.create_line(50, 150, 750, 150, width=2)  # Coordenadas: (x1, y1, x2, y2)

        lbDentista = Label(self.ventana, text="Dentista", font=("Arial", 20, "bold"), anchor="center")
        lbDentista.place(x=340, y=170, width=120, height=30)

        botonAltaDentista = Button(self.ventana, text="Alta", font=("Arial", 16), anchor="center")
        botonAltaDentista.place(x=87.5, y=220, width=150, height=50)

        botonBajaDentista = Button(self.ventana, text="Baja", font=("Arial", 16), anchor="center")
        botonBajaDentista.place(x=325, y=220, width=150, height=50)

        botonModificarDentista = Button(self.ventana, text="Modificar", font=("Arial", 16), anchor="center")
        botonModificarDentista.place(x=562.5, y=220, width=150, height=50)

        # Dibujar una línea horizontal
        canvas.create_line(50, 300, 750, 300, width=2)  # Coordenadas: (x1, y1, x2, y2)

        lbCitas = Label(self.ventana, text="Citas", font=("Arial", 20, "bold"), anchor="center")
        lbCitas.place(x=340, y=320, width=120, height=30)

        botonAgendarCita = Button(self.ventana, text="Agendar", font=("Arial", 16), anchor="center")
        botonAgendarCita.place(x=87.5, y=370, width=150, height=50)

        botonCancelarCita = Button(self.ventana, text="Cancelar", font=("Arial", 16), anchor="center")
        botonCancelarCita.place(x=325, y=370, width=150, height=50)

        botonModificarCita = Button(self.ventana, text="Modificar", font=("Arial", 16), anchor="center")
        botonModificarCita.place(x=562.5, y=370, width=150, height=50)

        # Dibujar una línea horizontal
        canvas.create_line(50, 450, 750, 450, width=2)  # Coordenadas: (x1, y1, x2, y2)

        botonCerrarSesion = Button(self.ventana, text="Cerrar Sesión", font=("Arial", 16), anchor="center", command=self.regresar, bg="SteelBlue1", fg="white")
        botonCerrarSesion.place(x=200, y=500, width=150, height=50)

        botonSalir = Button(self.ventana, text="Salir", font=("Arial", 16), command=self.salir, bg="red", fg="white")
        botonSalir.place(x=450, y=500, width=150, height=50)

        self.ventana.mainloop()

    # Contenido específico para el rol de usuario

    def centrar_ventana(self):
        ancho_ventana = 800
        alto_ventana = 600

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # Calcular las coordenadas x, y para centrar la ventana
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        # Establecer las dimensiones y la posición de la ventana
        self.ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

    def salir(self):
        self.ventana.destroy()

    def regresar(self):
        self.ventana.destroy()
        self.regreso = Login()
        self.regreso.ventana.mainloop() 

# pruebas = VentanaPaciente("Paciente")