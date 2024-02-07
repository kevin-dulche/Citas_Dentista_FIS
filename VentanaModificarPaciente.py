import re
from tkinter import StringVar
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from VentanaRecepcionista import *
from datetime import datetime

class VentanaModificarPaciente:
    def __init__(self, usuario, paciente):
        self.usuario = usuario
        self.ventana = Tk()
        self.ventana.title("Alta de Paciente" + " - " + self.usuario[1])

        # Centrar la ventana en la pantalla
        self.centrar_ventana()

        # Evitar que la ventana cambie de tamaño
        self.ventana.resizable(0, 0)

        # Crear un objeto Canvas
        canvas = Canvas(self.ventana, width=800, height=600)
        canvas.pack()

        # Cargar la imagen y redimensionarla
        imagen_original = PhotoImage(file="./assets/reload.png")
        imagen_redimensionada = imagen_original.subsample(13, 13)  # Redimensionar a la mitad
        
        lbAltaPaciente = Label(self.ventana, text="Alta de Paciente", font=("Arial", 20, "bold"), anchor="center")
        lbAltaPaciente.place(x=20, y=10, width=210, height=69)

        lbNombre = Label(self.ventana, text="Nombre(s): ", font=("Arial", 15), anchor="w")
        lbNombre.place(x=20, y=89, width=130, height=40)
        # Texto a mostrar
        nombre = "Juan Pérez"
        # Label para mostrar el nombre
        self.labelNombre = tk.Label(self.ventana, text=nombre, font=("Arial", 14))
        self.labelNombre.place(x=160, y=89, width=170, height=40)  # Ajustar el tamaño según sea necesario
        self.labelNombre.configure(state="disabled")  # Deshabilitar la edición del Label

        # Crear el botón con la imagen redimensionada
        boton_con_imagen = Button(self.ventana, image=imagen_redimensionada)
        boton_con_imagen.image = imagen_redimensionada  # Mantener referencia a la imagen para evitar que se elimine de la memoria
        boton_con_imagen.place(x=340, y=89, width=40, height=40)

        lbNombre = Label(self.ventana, text="Apellidos ", font=("Arial", 15), anchor="w")
        lbNombre.place(x=20, y=139, width=130, height=40)

        lbApellidoPaterno = Label(self.ventana, text="Paterno: ", font=("Arial", 15), anchor="w")
        lbApellidoPaterno.place(x=20, y=189, width=130, height=40)
        self.texto_apellido_paterno = StringVar()
        self.textoApellidoPaterno = Entry(self.ventana, textvariable=self.texto_apellido_paterno)
        self.textoApellidoPaterno.configure(font=("Arial", 14))
        self.textoApellidoPaterno.place(x=160, y=189, width=170, height=40)

        lbApellidoMaterno = Label(self.ventana, text="Materno: ", font=("Arial", 15), anchor="w")
        lbApellidoMaterno.place(x=20, y=239, width=130, height=40)
        self.texto_apellido_materno = StringVar()
        self.textoApellidoMaterno = Entry(self.ventana, textvariable=self.texto_apellido_materno)
        self.textoApellidoMaterno.configure(font=("Arial", 14))
        self.textoApellidoMaterno.place(x=160, y=239, width=170, height=40)

        lbEdad = Label(self.ventana, text="Edad: ", font=("Arial", 15), anchor="w")
        lbEdad.place(x=20, y=289, width=130, height=40)
        self.texto_edad = StringVar()
        self.textoEdad = Entry(self.ventana, textvariable=self.texto_edad)
        self.textoEdad.configure(font=("Arial", 14))
        self.textoEdad.bind("<KeyRelease>", lambda event, entry=self.textoEdad, var=self.texto_edad: self.validar_numero(event, entry, var))
        self.textoEdad.place(x=160, y=289, width=170, height=40)

        lbPeso = Label(self.ventana, text="Peso (kg): ", font=("Arial", 15), anchor="w")
        lbPeso.place(x=20, y=339, width=130, height=40)
        self.texto_peso = StringVar()
        self.textoPeso = Entry(self.ventana, textvariable=self.texto_peso)
        self.textoPeso.configure(font=("Arial", 14))
        self.textoPeso.bind("<KeyRelease>", lambda event, entry=self.textoPeso, var=self.texto_peso: self.validar_numero(event, entry, var))
        self.textoPeso.place(x=160, y=339, width=170, height=40)

        lbEstatura = Label(self.ventana, text="Estatura (cm): ", font=("Arial", 15), anchor="w")
        lbEstatura.place(x=20, y=389, width=130, height=40)
        self.texto_estatura = StringVar()
        self.textoEstatura = Entry(self.ventana, textvariable=self.texto_estatura)
        self.textoEstatura.configure(font=("Arial", 14))
        self.textoEstatura.bind("<KeyRelease>", lambda event, entry=self.textoEstatura, var=self.texto_estatura: self.validar_numero(event, entry, var))
        self.textoEstatura.place(x=160, y=389, width=170, height=40)

        lbSexo = Label(self.ventana, text="Sexo: ", font=("Arial", 15), anchor="w")
        lbSexo.place(x=20, y=439, width=130, height=40)
        opciones_sexo = ["Masculino", "Femenino"]
        self.texto_sexo = StringVar()
        self.comboSexo = Combobox(self.ventana, textvariable=self.texto_sexo, values=opciones_sexo, font=("Arial", 15), state="readonly")
        self.comboSexo.place(x=160, y=439, width=170, height=40)

        # Etiqueta para la entrada de texto
        lbPatologias = Label(self.ventana, text="Patologías: ", font=("Arial", 15), anchor="w")
        lbPatologias.place(x=20, y=489, width=130, height=40)
        self.textoPatologias = Text(self.ventana, font=("Arial", 14))
        self.textoPatologias.place(x=160, y=489, width=170, height=100)  # Ajustar el tamaño según sea necesario
        scroll_vertical = Scrollbar(self.ventana, orient="vertical", command=self.textoPatologias.yview)
        scroll_vertical.place(x=340, y=489, height=100)
        self.textoPatologias.config(yscrollcommand=scroll_vertical.set)

        botonAltaPaciente = Button(self.ventana, text="Alta", font=("Arial", 15), anchor="center", command=self.AltaPaciente, bg="SteelBlue1", fg="white")
        botonAltaPaciente.place(x=387.5, y=539, width=120, height=40)

        botonCancelar = Button(self.ventana, text="Cancelar", font=("Arial", 15), anchor="center", command=self.cancelar, bg="SlateGray3", fg="white")
        botonCancelar.place(x=587.5, y=539, width=120, height=40)

        lbDireccion = Label(self.ventana, text="Dirección", font=("Arial", 20, "bold"), anchor="center")
        lbDireccion.place(x=400, y=10, width=210, height=69)

        lbCalle = Label(self.ventana, text="Calle: ", font=("Arial", 15), anchor="w")
        lbCalle.place(x=400, y=89, width=130, height=40)
        self.texto_calle = StringVar()
        self.textoCalle = Entry(self.ventana, textvariable=self.texto_calle)
        self.textoCalle.configure(font=("Arial", 14))
        self.textoCalle.place(x=580, y=89, width=170, height=40)

        lbNumero = Label(self.ventana, text="Número: ", font=("Arial", 15), anchor="w")
        lbNumero.place(x=400, y=139, width=130, height=40)
        self.texto_numero = StringVar()
        self.textoNumero = Entry(self.ventana, textvariable=self.texto_numero)
        self.textoNumero.configure(font=("Arial", 14))
        self.textoNumero.bind("<KeyRelease>", lambda event, entry=self.textoNumero, var=self.texto_numero: self.validar_numero(event, entry, var))
        self.textoNumero.place(x=580, y=139, width=170, height=40)

        lbColonia = Label(self.ventana, text="Colonia: ", font=("Arial", 15), anchor="w")
        lbColonia.place(x=400, y=189, width=130, height=40)
        self.texto_colonia = StringVar()
        self.textoColonia = Entry(self.ventana, textvariable=self.texto_colonia)
        self.textoColonia.configure(font=("Arial", 14))
        self.textoColonia.place(x=580, y=189, width=170, height=40)

        lbCodigoPostal = Label(self.ventana, text="Código Postal: ", font=("Arial", 15), anchor="w")
        lbCodigoPostal.place(x=400, y=239, width=130, height=40)
        self.texto_codigo_postal = StringVar()
        self.textoCodigoPostal = Entry(self.ventana, textvariable=self.texto_codigo_postal)
        self.textoCodigoPostal.configure(font=("Arial", 14))
        self.textoCodigoPostal.bind("<KeyRelease>", lambda event, entry=self.textoCodigoPostal, var=self.texto_codigo_postal: self.validar_numero(event, entry, var))
        self.textoCodigoPostal.place(x=580, y=239, width=170, height=40)

        lbMunicipio = Label(self.ventana, text="Municipio: ", font=("Arial", 15), anchor="w")
        lbMunicipio.place(x=400, y=289, width=130, height=40)
        self.texto_municipio = StringVar()
        self.textoMunicipio = Entry(self.ventana, textvariable=self.texto_municipio)
        self.textoMunicipio.configure(font=("Arial", 14))
        self.textoMunicipio.place(x=580, y=289, width=170, height=40)


        lbEstado = Label(self.ventana, text="Estado: ", font=("Arial", 15), anchor="w")
        lbEstado.place(x=400, y=339, width=130, height=40)
        estados_mexico = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Coahuila", "Colima", "CDMX", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"]
        self.texto_estado = StringVar()
        self.combo_estado = Combobox(self.ventana, textvariable=self.texto_estado, values=estados_mexico, font=("Arial", 15), state="readonly")
        self.combo_estado.place(x=580, y=339, width=170, height=40)

        lbTelefono = Label(self.ventana, text="Teléfono: ", font=("Arial", 15), anchor="w")
        lbTelefono.place(x=400, y=389, width=130, height=40)
        self.texto_telefono = StringVar()
        self.textoTelefono = Entry(self.ventana, textvariable=self.texto_telefono)
        self.textoTelefono.configure(font=("Arial", 14))
        self.textoTelefono.bind("<KeyRelease>", lambda event, entry=self.textoTelefono, var=self.texto_telefono: self.validar_numero(event, entry, var))
        self.textoTelefono.place(x=580, y=389, width=170, height=40)

        lbFechaNacimiento = Label(self.ventana, text="Fecha Nacimiento:", font=("Arial", 15), anchor="w")
        lbFechaNacimiento.place(x=400, y=439, width=170, height=40)

        self.fecha_nacimiento = DateEntry(self.ventana, font=("Arial", 14), date_pattern='yyyy-mm-dd')
        self.fecha_nacimiento.place(x=580, y=439, width=170, height=40)

        lbFechaAlta = Label(self.ventana, text="Fecha Alta:", font=("Arial", 15), anchor="w")
        lbFechaAlta.place(x=400, y=489, width=170, height=40)

        fecha_actual = datetime.now().strftime('%Y-%m-%d')

        self.fecha_alta = DateEntry(self.ventana, font=("Arial", 14), date_pattern='yyyy-mm-dd', state='readonly')
        self.fecha_alta.set_date(fecha_actual)
        self.fecha_alta.configure(state='disabled')
        self.fecha_alta.place(x=580, y=489, width=170, height=40)

        self.ventana.mainloop()

    def validar_numero(self, event, entry, var):
        # Esta función valida que el contenido del Entry sea solo números o un punto
        nuevo_valor = var.get()
        if not re.match(r'^\d*\.?\d*$', nuevo_valor):
            # Si el nuevo valor no es un número ni un punto ni está vacío, eliminar el último carácter ingresado
            var.set(nuevo_valor[:-1])

    def toggle_password(self):
        # Cambiar el estado de mostrar/ocultar la contraseña
        if self.textoContraseña.cget("show") == "":
            self.textoContraseña.configure(show="*")
        else:
            self.textoContraseña.configure(show="")


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

    def AltaPaciente(self):
        
        try:
            # Configura la conexión a la base de datos (ajusta según tu configuración)
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="login"
            )

            self.cursor = self.conexion.cursor()

            if self.textoUsuario.get() == "" or self.textoContraseña.get() == "" or self.textoNombre.get() == "" or self.textoApellidoPaterno.get() == "" or self.textoApellidoMaterno.get() == "" or self.textoEdad.get() == "" or self.textoPeso.get() == "" or self.textoCalle.get() == "" or self.textoNumero.get() == "" or self.textoColonia.get() == "" or self.textoCodigoPostal.get() == "" or self.textoMunicipio.get() == "" or self.textoTelefono.get() == "":
                messagebox.showerror("Error", "Favor de llenar todos los campos")
                return
            username = self.textoUsuario.get() 
            password = self.textoContraseña.get()
            role = "Paciente"
            nombre_s = self.textoNombre.get()
            apellido_paterno = self.textoApellidoPaterno.get()
            apellido_materno = self.textoApellidoMaterno.get()
            edad = self.textoEdad.get()
            peso = self.textoPeso.get()
            sexo = self.comboSexo.get()
            calle = self.textoCalle.get()
            numero = self.textoNumero.get()
            colonia = self.textoColonia.get()
            codigo_postal = self.textoCodigoPostal.get()
            alcaldia_municipio = self.textoMunicipio.get()
            estado = self.combo_estado.get()
            telefono = self.textoTelefono.get()
            fechaNacimiento = self.fecha_nacimiento.get_date()
            fechaAlta = self.fecha_alta.get_date()
            patologias = ''

            # Inserta usuario
            query_insert_usuario = "INSERT INTO usuarios (name, password, role) VALUES (%s, %s, %s)"
            datos_usuario = (username, password, role)
            self.cursor.execute(query_insert_usuario, datos_usuario)

            # Obtiene el ID del usuario recién insertado
            ultimo_id_usuario = self.cursor.lastrowid

            # Inserta paciente con el mismo ID del usuario
            query_insert_paciente = "INSERT INTO pacientes (paciente_id, nombres, apellido_paterno, apellido_materno, edad, peso, sexo, calle, numero, colonia, codigo_postal, alcaldia_municipio, estado, telefono, fecha_nacimiento, fecha_alta, patologias) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            datos_paciente = (ultimo_id_usuario, nombre_s, apellido_paterno, apellido_materno, edad, peso, sexo, calle, numero, colonia, codigo_postal, alcaldia_municipio, estado, telefono, fechaNacimiento, fechaAlta, patologias)
            self.cursor.execute(query_insert_paciente, datos_paciente)

            # Confirmar la transacción
            self.conexion.commit()
            messagebox.showinfo("Alta de Paciente", "Paciente registrado con éxito")
            self.cancelar()

            # Cierra el cursor y la conexión
            self.cursor.close()
            self.conexion.close()

        except Exception as err:
            messagebox.showerror("Error", f"Error en la carga de datos:\n{str(err)}")

    def cancelar(self):
        self.ventana.destroy()
        self.regreso = VentanaRecepcionista(self.usuario)
        self.regreso.ventana.mainloop() 

class VentanaIdentificacion:
    def __init__(self, usuario):
        self.usuario = usuario
        self.ventana = Tk()
        self.ventana.title("Modificar Paciente" + " - " + self.usuario[1])

        # Centrar la ventana en la pantalla
        self.centrar_ventana()

        # Evitar que la ventana cambie de tamaño
        self.ventana.resizable(0, 0)

        lbModificarPaciente = Label(self.ventana, text="Paciente a modificar:", font=("Arial", 20, "bold"), anchor="center")
        lbModificarPaciente.place(x=100, y=10, width=300, height=69)

        lbNombre = Label(self.ventana, text="Nombre(s): ", font=("Arial", 15), anchor="w")
        lbNombre.place(x=55, y=89, width=160, height=40)
        self.texto_nombre = StringVar()
        self.textoNombre = Entry(self.ventana, textvariable=self.texto_nombre)
        self.textoNombre.configure(font=("Arial", 14))
        self.textoNombre.place(x=255, y=89, width=190, height=40)

        lbApellidoPaterno = Label(self.ventana, text="Apellido Paterno: ", font=("Arial", 15), anchor="w")
        lbApellidoPaterno.place(x=55, y=139, width=160, height=40)
        self.texto_apellido_paterno = StringVar()
        self.textoApellidoPaterno = Entry(self.ventana, textvariable=self.texto_apellido_paterno)
        self.textoApellidoPaterno.configure(font=("Arial", 14))
        self.textoApellidoPaterno.place(x=255, y=139, width=190, height=40)

        lbApellidoMaterno = Label(self.ventana, text="Apellido Materno: ", font=("Arial", 15), anchor="w")
        lbApellidoMaterno.place(x=55, y=189, width=160, height=40)
        self.texto_apellido_materno = StringVar()
        self.textoApellidoMaterno = Entry(self.ventana, textvariable=self.texto_apellido_materno)
        self.textoApellidoMaterno.configure(font=("Arial", 14))
        self.textoApellidoMaterno.place(x=255, y=189, width=190, height=40)

        botonModificarPaciente = Button(self.ventana, text="Modificar", font=("Arial", 15), anchor="center", bg="SteelBlue1", fg="white")
        botonModificarPaciente.place(x=86, y=310, width=120, height=40)

        botonCancelar = Button(self.ventana, text="Cancelar", font=("Arial", 15), anchor="center", command=self.cancelar, bg="SlateGray3", fg="white")
        botonCancelar.place(x=293, y=310, width=120, height=40)

        self.ventana.mainloop()

    def centrar_ventana(self):
        ancho_ventana = 500
        alto_ventana = 400

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # Calcular las coordenadas x, y para centrar la ventana
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        # Establecer las dimensiones y la posición de la ventana
        self.ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

    def cancelar(self):
        self.ventana.destroy()
        self.regreso = VentanaRecepcionista(self.usuario)
        self.regreso.ventana.mainloop() 

# prueba = VentanaModificarPaciente((2,"Fernanda Estevez","Hola12345","Recepcionista"))
        
# prueba = VentanaIdentificacion((2,"Fernanda Estevez","Hola12345","Recepcionista"))