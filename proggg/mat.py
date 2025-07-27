import tkinter as tk
from tkinter import messagebox
import json
import os

productos = []
clientes = []

def guardar_datos():
    datos = {"productos": productos, "clientes": clientes}
    with open("ferreteria.json", "w") as f:
        json.dump(datos, f, indent=4)

def cargar_datos():
    if os.path.exists("ferreteria.json"):
        with open("ferreteria.json", "r") as f:
            datos = json.load(f)
            productos.extend(datos.get("productos", []))
            clientes.extend(datos.get("clientes", []))

def ingresar_producto():
    def guardar():
        try:
            id_ = entry_id.get()
            nombre = entry_nombre.get()
            precio = entry_precio.get()
            cantidad = entry_cantidad.get()
            proveedor = entry_proveedor.get()

            if not all([id_, nombre, precio, cantidad, proveedor]):
                messagebox.showerror("Error", "Todos los campos deben estar llenos.")
                return

            precio = float(precio)
            cantidad = int(cantidad)

            if cantidad < 40:
                messagebox.showwarning("Stock bajo", f"El stock actual ({cantidad}) está por debajo del mínimo (40).")
                return
            elif cantidad > 200:
                messagebox.showwarning("Stock alto", f"El stock actual ({cantidad}) está por encima del máximo (200).")
                return

            producto = {
                "id": id_,
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "proveedor": proveedor,
                "stock_min": 40,
                "stock_max": 200
            }

            productos.append(producto)
            guardar_datos()
            messagebox.showinfo("Éxito", "Producto ingresado correctamente.")
            ventana_producto.destroy()
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser numéricos.")

    ventana_producto = tk.Toplevel(ventana)
    ventana_producto.title("Ingresar Producto")
    ventana_producto.geometry("400x300")

    tk.Label(ventana_producto, text="ID:").pack()
    entry_id = tk.Entry(ventana_producto)
    entry_id.pack()

    tk.Label(ventana_producto, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana_producto)
    entry_nombre.pack()

    tk.Label(ventana_producto, text="Precio:").pack()
    entry_precio = tk.Entry(ventana_producto)
    entry_precio.pack()

    tk.Label(ventana_producto, text="Cantidad:").pack()
    entry_cantidad = tk.Entry(ventana_producto)
    entry_cantidad.pack()

    tk.Label(ventana_producto, text="Proveedor:").pack()
    entry_proveedor = tk.Entry(ventana_producto)
    entry_proveedor.pack()

    tk.Button(ventana_producto, text="Guardar", command=guardar).pack(pady=5)

def ingresar_cliente():
    def guardar():
        cedula = entry_cedula.get()
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()

        if not all([cedula, nombre, direccion, telefono, correo]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        cliente = {
            "cedula": cedula,
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo
        }

        clientes.append(cliente)
        guardar_datos()
        messagebox.showinfo("Éxito", "Cliente ingresado correctamente.")
        ventana_cliente.destroy()

    ventana_cliente = tk.Toplevel(ventana)
    ventana_cliente.title("Ingresar Cliente")
    ventana_cliente.geometry("400x300")

    tk.Label(ventana_cliente, text="Cédula:").pack()
    entry_cedula = tk.Entry(ventana_cliente)
    entry_cedula.pack()

    tk.Label(ventana_cliente, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana_cliente)
    entry_nombre.pack()

    tk.Label(ventana_cliente, text="Dirección:").pack()
    entry_direccion = tk.Entry(ventana_cliente)
    entry_direccion.pack()

    tk.Label(ventana_cliente, text="Teléfono:").pack()
    entry_telefono = tk.Entry(ventana_cliente)
    entry_telefono.pack()

    tk.Label(ventana_cliente, text="Correo:").pack()
    entry_correo = tk.Entry(ventana_cliente)
    entry_correo.pack()

    tk.Button(ventana_cliente, text="Guardar", command=guardar).pack(pady=5)

def eliminar_datos():
    def eliminar():
        tipo = opcion.get()
        identificador = entry_id.get()

        if tipo == "Producto":
            for p in productos:
                if p["id"] == identificador:
                    productos.remove(p)
                    guardar_datos()
                    messagebox.showinfo("Eliminado", "Producto eliminado.")
                    ventana_eliminar.destroy()
                    return
        elif tipo == "Cliente":
            for c in clientes:
                if c["cedula"] == identificador:
                    clientes.remove(c)
                    guardar_datos()
                    messagebox.showinfo("Eliminado", "Cliente eliminado.")
                    ventana_eliminar.destroy()
                    return

        messagebox.showerror("No encontrado", "No se encontró el registro.")

    ventana_eliminar = tk.Toplevel(ventana)
    ventana_eliminar.title("Eliminar Registro")
    ventana_eliminar.geometry("400x250")

    opcion = tk.StringVar(value="Producto")

    tk.Radiobutton(ventana_eliminar, text="Producto", variable=opcion, value="Producto").pack()
    tk.Radiobutton(ventana_eliminar, text="Cliente", variable=opcion, value="Cliente").pack()

    tk.Label(ventana_eliminar, text="Ingrese ID o Cédula:").pack()
    entry_id = tk.Entry(ventana_eliminar)
    entry_id.pack()

    tk.Button(ventana_eliminar, text="Eliminar", command=eliminar).pack(pady=5)

def vender_producto():
    def vender():
        id_producto = entry_id.get()
        try:
            cantidad_vendida = int(entry_cantidad.get())
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser numérica.")
            return

        for producto in productos:
            if producto["id"] == id_producto:
                if producto["cantidad"] < cantidad_vendida:
                    messagebox.showerror("Stock insuficiente", "No hay suficiente stock para esta venta.")
                    return
                producto["cantidad"] -= cantidad_vendida
                guardar_datos()
                if producto["cantidad"] < 40:
                    messagebox.showwarning("Stock bajo", "El stock ha caído por debajo del mínimo (40).")
                messagebox.showinfo("Venta realizada", "Producto vendido correctamente.")
                ventana_venta.destroy()
                return

        messagebox.showerror("No encontrado", "Producto no encontrado.")

    ventana_venta = tk.Toplevel(ventana)
    ventana_venta.title("Vender Producto")
    ventana_venta.geometry("400x250")

    tk.Label(ventana_venta, text="ID del producto:").pack()
    entry_id = tk.Entry(ventana_venta)
    entry_id.pack()

    tk.Label(ventana_venta, text="Cantidad a vender:").pack()
    entry_cantidad = tk.Entry(ventana_venta)
    entry_cantidad.pack()

    tk.Button(ventana_venta, text="Vender", command=vender).pack(pady=5)

def procesar_opcion():
    opcion = entrada.get()
    if opcion == "1":
        ingresar_producto()
    elif opcion == "2":
        ingresar_cliente()
    elif opcion == "3":
        vender_producto()
    elif opcion == "4":
        eliminar_datos()
    elif opcion == "5":
        ventana.quit()
    else:
        messagebox.showwarning("Opción inválida", "Por favor, ingrese una opción válida (1-5).")

def solicitar_clave():
    def verificar():
        if entry_clave.get() == "1209":
            ventana_login.destroy()
            mostrar_menu()
        else:
            messagebox.showerror("Acceso denegado", "Clave incorrecta.")

    ventana_login = tk.Tk()
    ventana_login.title("Ingreso de Vendedor")
    ventana_login.geometry("350x150")

    tk.Label(ventana_login, text="Ingrese la clave del vendedor:").pack(pady=5)
    entry_clave = tk.Entry(ventana_login, show="*")
    entry_clave.pack()
    tk.Button(ventana_login, text="Entrar", command=verificar).pack(pady=5)

    ventana_login.mainloop()

def mostrar_menu():
    global ventana, entrada
    cargar_datos()
    messagebox.showinfo("Bienvenida", "¡Bienvenido al sistema de ferretería!")

    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.geometry("400x350")

    etiqueta = tk.Label(
        ventana,
        text="Seleccione una opción:\n"
             "1. Ingresar Producto\n"
             "2. Ingresar Cliente\n"
             "3. Vender Producto\n"
             "4. Eliminar\n"
             "5. Salir",
        font=("Courier", 10),
        justify="left"
    )
    etiqueta.pack(pady=10)

    entrada = tk.Entry(ventana)
    entrada.pack()

    tk.Button(ventana, text="Enviar", command=procesar_opcion).pack(pady=10)

    ventana.mainloop()

solicitar_clave()