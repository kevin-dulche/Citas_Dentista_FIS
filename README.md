# Citas_Dentista_FIS

## Intrucciones

### Requisitos previos:
* Tener en una base de datos mysql, una base de datos predeterminada con la siguiente tabla `'usuarios'`:
```
+------+--------------------+----------------+----------------+
|  id  |      name          |    password    |     role       |
+------+--------------------+----------------+----------------+
|   1  | "Kevin Dulche"     |    12345678    | Administrador  |
|   2  | "Fernanda Estevez" |    Hola12345   | Recepcionista  |
|   3  | "Gabriel Aguirre"  |    87654321    | Administrador  |
+------+--------------------+----------------+----------------+
```
El csv se encuentra en la siguiente ruta `./data/tablaUsuarios.csv`

Tambien es necesario contar con una version de python >= 3.10 en el equipo

### Ejecución

Para el uso del programa se necesita seguir los siguientes pasos:

En la terminal de comandos (en la ruta en la que vas a querer el programa)
```
git clone
cd Citas_Dentista_FIS
python -m venv citas
.\citas\Scripts\activate
pip install -r requirements.txt
python GUI.py
```