from tkinter import StringVar
from VentanaRecepcionista import *


class VentanaBajaPaciente:
    def __init__(self, usuario):
        self.usuario = usuario
        self.ventana = Tk()
        self.ventana.title("Baja de Paciente" + " - " + self.usuario[1])

        # Centrar la ventana en la pantalla
        self.centrar_ventana()

        # Evitar que la ventana cambie de tamaño
        self.ventana.resizable(0, 0)

        lbBajaPaciente = Label(self.ventana, text="Baja de Paciente", font=("Arial", 20, "bold"), anchor="center")
        lbBajaPaciente.place(x=90, y=10, width=220, height=69)

        lbUsuario = Label(self.ventana, text="Usuario: ", font=("Arial", 15), anchor="w")
        lbUsuario.place(x=20, y=89, width=130, height=40)
        self.texto_usuario = StringVar()
        self.textoUsuario = Entry(self.ventana, textvariable=self.texto_usuario)
        self.textoUsuario.configure(font=("Arial", 14))
        self.textoUsuario.place(x=160, y=89, width=170, height=40) # 19/2 = 9.5

        lbContraseña = Label(self.ventana, text="Contraseña: ", font=("Arial", 15), anchor="w")
        lbContraseña.place(x=20, y=139, width=130, height=40)
        self.texto_contraseña = StringVar()
        self.textoContraseña = Entry(self.ventana, textvariable=self.texto_contraseña, show="*")
        self.textoContraseña.configure(font=("Arial", 14))
        self.textoContraseña.place(x=160, y=139, width=170, height=40)

        self.btn_mostrar = Button(self.ventana, text="Mostrar", command=self.toggle_password)
        self.btn_mostrar.place(x=335, y=139, width=50, height=40)

        botonBajaPaciente = Button(self.ventana, text="Baja", font=("Arial", 15), anchor="center", command=self.BajaPaciente, bg="SteelBlue1", fg="white")
        botonBajaPaciente.place(x=53, y=210, width=120, height=40)

        botonCancelar = Button(self.ventana, text="Cancelar", font=("Arial", 15), anchor="center", command=self.cancelar, bg="SlateGray3", fg="white")
        botonCancelar.place(x=227, y=210, width=120, height=40)

        self.ventana.mainloop()

    def toggle_password(self):
        # Cambiar el estado de mostrar/ocultar la contraseña
        if self.textoContraseña.cget("show") == "":
            self.textoContraseña.configure(show="*")
        else:
            self.textoContraseña.configure(show="")

    def centrar_ventana(self):
        ancho_ventana = 400
        alto_ventana = 300

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # Calcular las coordenadas x, y para centrar la ventana
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        # Establecer las dimensiones y la posición de la ventana
        self.ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

    def BajaPaciente(self):
        
        try:
            if self.textoUsuario.get() == "" or self.textoContraseña.get() == "":
                messagebox.showerror("Error", "Favor de llenar todos los campos")
                return
            
            # Configura la conexión a la base de datos (ajusta según tu configuración)
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="login"
            )

            self.cursor = self.conexion.cursor()

            username = self.textoUsuario.get()
            password = self.textoContraseña.get()

            # Ejecuta la consulta
            consulta = "SELECT * FROM usuarios WHERE name = %s AND password = %s"
            parametros = (username, password)
            self.cursor.execute(consulta, parametros)

            # Recupera los resultados de la consulta
            resultados = self.cursor.fetchall()

            if resultados:
                # Muestra un cuadro de diálogo de confirmación
                respuesta = messagebox.askyesno("Confirmación", "¿Quieres continuar con la baja del paciente?")

                # Verifica la respuesta
                if respuesta:
                    pass
                else:
                    return
                # Si hay resultadosse procede con la baja
                usuario_actual = resultados[0]
                consulta = "DELETE FROM usuarios WHERE id = %s"
                id = usuario_actual[0]
                parametros = (id,)
                self.cursor.execute(consulta, parametros)

                consulta = "DELETE FROM pacientes WHERE paciente_id = %s"
                self.cursor.execute(consulta, parametros)
                # Confirmar la transacción
                self.conexion.commit()
                messagebox.showinfo("Baja de Paciente", "Paciente dado de baja exitosamente.")
                self.cancelar()

            else:
                # Si no hay resultados, mostrar un mensaje de error
                messagebox.showerror("Error", "Nombre de usuario y/o contraseña incorrectos.")

            # Cierra el cursor y la conexión
            self.cursor.close()
            self.conexion.close()
                

        except Exception as err:
            messagebox.showerror("Error", f"Error en la baja de datos:\n{str(err)}")

    def cancelar(self):
        self.ventana.destroy()
        self.regreso = VentanaRecepcionista(self.usuario)
        self.regreso.ventana.mainloop() 

# prueba = VentanaBajaPaciente((2,"Fernanda Estevez","Hola12345","Recepcionista"))