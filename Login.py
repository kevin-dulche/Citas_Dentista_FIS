from tkinter import Tk, Label, Button, Entry, messagebox
from PIL import Image, ImageTk
import tkinter as tk 
import mysql.connector

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Login")

        # Centrar la ventana en la pantalla
        self.centrar_ventana()

        # Evitar que la ventana cambie de tamaño
        self.ventana.resizable(0, 0)

        imagen = Image.open("./assets/imglogin.png")
        imagen = ImageTk.PhotoImage(imagen)

        label_imagen = Label(self.ventana, image=imagen)
        label_imagen.place(x=136, y=20, width=128, height=128)

        lb0 = Label(self.ventana, text="Login", font=("Arial", 20, "bold"), anchor="center")
        lb0.place(x=150, y=158, width=100, height=30)

        lb1 = Label(self.ventana, text="Usuario: ", font=("Arial", 16), anchor="e")
        lb1.place(x=50, y=198, width=130, height=30)

        self.txt1 = Entry(self.ventana)
        self.txt1.place(x=190, y=198, width=170, height=30)

        lb2 = Label(self.ventana, text="Contraseña: ", font=("Arial", 16), anchor="e")
        lb2.place(x=50, y=238, width=130, height=30)

        self.txt2 = Entry(self.ventana, show="*")
        self.txt2.place(x=190, y=238, width=170, height=30)

        buttonIngresar = Button(self.ventana, text="Ingresar", font=("Arial", 16), anchor="center", command=self.iniciar_sesion)
        buttonIngresar.place(x=75, y=290, width=100, height=50)

        buttonLimpiar = Button(self.ventana, text="Limpiar", font=("Arial", 16), anchor="center", command=self.limpiar_entry)
        buttonLimpiar.place(x=225, y=290, width=100, height=50)

        boton_salir = Button(self.ventana, text="Salir", font=("Arial", 16), command=self.salir, bg="red", fg="white")
        boton_salir.place(x=162.5, y=355, width=75, height=30)

        self.ventana.mainloop()

    def centrar_ventana(self):
        ancho_ventana = 400
        alto_ventana = 400

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # Calcular las coordenadas x, y para centrar la ventana
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        # Establecer las dimensiones y la posición de la ventana
        self.ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

    def limpiar_entry(self):
        self.txt1.delete(0, tk.END)
        self.txt2.delete(0, tk.END)

    def salir(self):
        self.ventana.destroy()

    def iniciar_sesion(self):
        usuario = self.txt1.get()
        contrasena = self.txt2.get()

        # Configuración de la conexión a la base de datos
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'login',
            'raise_on_warnings': True
        }

        # Intentar conectar a la base de datos
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            # Consultar datos en la base de datos
            consulta = "SELECT * FROM usuarios WHERE name = %s AND password = %s"
            parametros = (usuario, contrasena)
            cursor.execute(consulta, parametros)

            # Obtener los resultados
            resultados = cursor.fetchall()

            if resultados:
                # Si hay resultados, el inicio de sesión es exitoso
                self.ventana.destroy()  # Cerrar la ventana de inicio de sesión
                usuario_actual = resultados[0]
                abrir_ventana_segun_rol(usuario_actual)

            else:
                # Si no hay resultados, mostrar un mensaje de error
                messagebox.showerror("Error", "Nombre de usuario y/o contraseña incorrectos.")

        except mysql.connector.Error as err:
            messagebox.showerror("Error de MySQL", f"Error de MySQL: {err}")

        finally:
            # Cerrar la conexión
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

def abrir_ventana_segun_rol(usuario):
    _, _, _, rol = usuario

    # Importa VentanaRecepcionista aquí para evitar un error de importación circular

    if rol == 'Administrador':
        VentanaAdmin(usuario)
    elif rol == 'Recepcionista':
        from VentanaRecepcionista import VentanaRecepcionista
        VentanaRecepcionista(usuario)
    elif rol == 'Recepcionista':
        VentanaPaciente(usuario)
    else:
        messagebox.showwarning("Advertencia", "Rol desconocido")

class VentanaAdmin:
    def __init__(self, usuario):
        self.ventana = Tk()
        self.ventana.title("Ventana de Administrador")

        # Contenido específico para el rol de administrador
        
class VentanaPaciente:
    def __init__(self, usuario):
        self.ventana = Tk()
        self.ventana.title("Ventana de Recepcionista")

        # Contenido específico para el rol de usuario

class VentanaDentista:
    def __init__(self, usuario):
        self.ventana = Tk()
        self.ventana.title("Ventana de Recepcionista")

        # Contenido específico para el rol de usuario