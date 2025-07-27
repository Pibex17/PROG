# Importamos las librerias necesarias
import tkinter as tk  # Para crear interfaces graficas
from tkinter import messagebox  # Para mostrar cuadros de dialogo (errores, advertencias, informacion)
import csv  # Para trabajar con archivos .csv
import os  # Para verificar si el archivo ya existe en el disco

# Creamos una lista vacia que almacenara todos los productos
productos = []

# Definimos el nombre del archivo donde se guardaran los productos
archivo_csv = "productos.csv"

# Si el archivo ya existe, lo abrimos y cargamos sus productos a la lista
if os.path.exists(archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as file:  # Abrimos el archivo en modo lectura
        reader = csv.DictReader(file)  # Leemos las filas del archivo como diccionarios
        productos = list(reader)  # Convertimos el lector en una lista y la guardamos

# Funcion para guardar la lista de productos en el archivo CSV
def guardar_en_archivo():
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:  # Abrimos el archivo en modo escritura
        campos = ['ID', 'Nombre', 'Precio', 'Cantidad', 'Proveedor', 'StockMin', 'StockMax']  # Encabezados del CSV
        writer = csv.DictWriter(file, fieldnames=campos)  # Creamos un escritor de diccionarios
        writer.writeheader()  # Escribimos la primera fila (encabezado)
        for p in productos:  # Recorremos la lista de productos
            writer.writerow(p)  # Escribimos cada producto en una fila del CSV

# Funcion que se llama al presionar el boton "Agregar Producto"
def agregar_producto():
    # Obtenemos los valores ingresados por el usuario desde los campos de entrada
    id_ = entrada_id.get()
    nombre = entrada_nombre.get()
    precio = entrada_precio.get()
    cantidad = entrada_cantidad.get()
    proveedor = entrada_proveedor.get()
    stock_min = entrada_stock_min.get()
    stock_max = entrada_stock_max.get()

    # Verificamos que todos los campos hayan sido completados
    if not all([id_, nombre, precio, cantidad, proveedor, stock_min, stock_max]):
        messagebox.showerror("Error", "Por favor llena todos los campos.")  # Mostramos mensaje de error
        return  # Salimos de la funcion sin guardar nada

    try:
        # Convertimos los campos que deben ser numericos a su tipo correspondiente
        precio = float(precio)  # Convertimos el precio a decimal
        cantidad = int(cantidad)  # Convertimos la cantidad a entero
        stock_min = int(stock_min)  # Convertimos el stock minimo a entero
        stock_max = int(stock_max)  # Convertimos el stock maximo a entero
    except ValueError:
        messagebox.showerror("Error", "Precio, cantidad y stock deben ser numericos.")  # Si hay error al convertir
        return  # No seguimos con el proceso

    # Comprobamos si la cantidad esta fuera del rango de stock definido
    if cantidad < stock_min:
        messagebox.showwarning("Stock bajo", f"El producto '{nombre}' tiene stock por debajo del minimo.")
    elif cantidad > stock_max:
        messagebox.showwarning("Stock alto", f"El producto '{nombre}' tiene stock por encima del maximo.")

    # Creamos un diccionario con la informacion del nuevo producto
    producto = {
        "ID": id_,
        "Nombre": nombre,
        "Precio": f"{precio:.2f}",  # Formateamos el precio con dos decimales
        "Cantidad": cantidad,
        "Proveedor": proveedor,
        "StockMin": stock_min,
        "StockMax": stock_max
    }

    productos.append(producto)  # Agregamos el producto a la lista
    guardar_en_archivo()  # Llamamos a la funcion para guardar la lista en el archivo CSV
    messagebox.showinfo("Producto agregado", f"Producto '{nombre}' registrado correctamente.")  # Mostramos mensaje de exito
    limpiar_campos()  # Limpiamos los campos de entrada del formulario

# Funcion para limpiar todos los campos del formulario
def limpiar_campos():
    entrada_id.delete(0, tk.END)  # Borramos el contenido del campo ID
    entrada_nombre.delete(0, tk.END)  # Borramos el contenido del campo Nombre
    entrada_precio.delete(0, tk.END)  # Borramos el contenido del campo Precio
    entrada_cantidad.delete(0, tk.END)  # Borramos el contenido del campo Cantidad
    entrada_proveedor.delete(0, tk.END)  # Borramos el contenido del campo Proveedor
    entrada_stock_min.delete(0, tk.END)  # Borramos el contenido del campo Stock Minimo
    entrada_stock_max.delete(0, tk.END)  # Borramos el contenido del campo Stock Maximo

# --------------------------
# Inicio de la interfaz grafica
# --------------------------

ventana = tk.Tk()  # Creamos la ventana principal
ventana.title("Registro de Productos")  # Establecemos el titulo de la ventana
ventana.geometry("400x500")  # Establecemos el tamano de la ventana (ancho x alto)

# Creamos etiquetas y campos de entrada para cada dato del producto

# Campo ID
tk.Label(ventana, text="ID").pack()  # Etiqueta "ID"
entrada_id = tk.Entry(ventana)  # Campo de entrada para el ID
entrada_id.pack()  # Posicionamos el campo en la ventana

# Campo Nombre
tk.Label(ventana, text="Nombre").pack()  # Etiqueta "Nombre"
entrada_nombre = tk.Entry(ventana)  # Campo de entrada para el nombre
entrada_nombre.pack()

# Campo Precio
tk.Label(ventana, text="Precio").pack()  # Etiqueta "Precio"
entrada_precio = tk.Entry(ventana)  # Campo de entrada para el precio
entrada_precio.pack()

# Campo Cantidad
tk.Label(ventana, text="Cantidad").pack()  # Etiqueta "Cantidad"
entrada_cantidad = tk.Entry(ventana)  # Campo de entrada para la cantidad
entrada_cantidad.pack()

# Campo Proveedor
tk.Label(ventana, text="Proveedor").pack()  # Etiqueta "Proveedor"
entrada_proveedor = tk.Entry(ventana)  # Campo de entrada para el proveedor
entrada_proveedor.pack()

# Campo Stock minimo
tk.Label(ventana, text="Stock minimo").pack()  # Etiqueta "Stock minimo"
entrada_stock_min = tk.Entry(ventana)  # Campo de entrada para el stock minimo
entrada_stock_min.pack()

# Campo Stock maximo
tk.Label(ventana, text="Stock maximo").pack()  # Etiqueta "Stock maximo"
entrada_stock_max = tk.Entry(ventana)  # Campo de entrada para el stock maximo
entrada_stock_max.pack()

# Boton para agregar el producto
tk.Button(ventana, text="Agregar Producto", command=agregar_producto).pack(pady=10)  # Al hacer clic se ejecuta agregar_producto()

# Boton para salir del programa
tk.Button(ventana, text="Salir", command=ventana.quit).pack()  # Cierra la ventana al hacer clic

# Iniciamos el bucle principal de la interfaz grafica
ventana.mainloop()
