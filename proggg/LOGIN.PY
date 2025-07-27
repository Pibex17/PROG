import tkinter as tk from tkinter import messagebox, PhotoImage import json import os

#------------------ Archivos de usuario ------------------

ARCHIVO_USUARIOS = "usuarios.json" PIN_ADMIN = "1234"  # PIN fijo dado por el administrador

Cargar usuarios existentes o crear archivo

usuarios = {} if os.path.exists(ARCHIVO_USUARIOS): with open(ARCHIVO_USUARIOS, "r") as f: usuarios = json.load(f)

#------------------ Funciones de usuario ------------------

def guardar_usuarios(): with open(ARCHIVO_USUARIOS, "w") as f: json.dump(usuarios, f, indent=4)

def crear_cuenta(): def registrar(): u = entry_usuario.get() c = entry_contraseña.get() p = entry_pin.get()

if not u or not c:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
        return
    if p != PIN_ADMIN:
        messagebox.showerror("PIN incorrecto", "El PIN ingresado no es válido.")
        return
    if u in usuarios:
        messagebox.showwarning("Usuario existe", "Ese usuario ya está registrado.")
        return

    usuarios[u] = c
    guardar_usuarios()
    messagebox.showinfo("Cuenta creada", "Tu cuenta ha sido creada exitosamente.")
    ventana_crear.destroy()

ventana_crear = tk.Toplevel()
ventana_crear.title("Crear Cuenta")

tk.Label(ventana_crear, text="Usuario:").pack()
entry_usuario = tk.Entry(ventana_crear)
entry_usuario.pack()

tk.Label(ventana_crear, text="Contraseña:").pack()
entry_contraseña = tk.Entry(ventana_crear, show="*")
entry_contraseña.pack()

tk.Label(ventana_crear, text="PIN Administrador:").pack()
entry_pin = tk.Entry(ventana_crear, show="*")
entry_pin.pack()

tk.Button(ventana_crear, text="Registrar", command=registrar).pack(pady=5)

def cambiar_contraseña(): def actualizar(): u = entry_usuario.get() c = entry_nueva.get()

if u not in usuarios:
        messagebox.showerror("No existe", "Ese usuario no está registrado.")
        return

    usuarios[u] = c
    guardar_usuarios()
    messagebox.showinfo("Actualizado", "Contraseña actualizada correctamente.")
    ventana_cambiar.destroy()

ventana_cambiar = tk.Toplevel()
ventana_cambiar.title("Cambiar Contraseña")

tk.Label(ventana_cambiar, text="Usuario:").pack()
entry_usuario = tk.Entry(ventana_cambiar)
entry_usuario.pack()

tk.Label(ventana_cambiar, text="Nueva Contraseña:").pack()
entry_nueva = tk.Entry(ventana_cambiar, show="*")
entry_nueva.pack()

tk.Button(ventana_cambiar, text="Actualizar", command=actualizar).pack(pady=5)

def login(): u = entry_usuario.get() c = entry_contraseña.get()

if usuarios.get(u) == c:
    messagebox.showinfo("Bienvenido", f"¡Hola {u}! Ingresaste correctamente.")
    ventana_login.destroy()
    # Aquí iría el llamado a la ventana principal
else:
    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

#------------------ Interfaz gráfica ------------------

ventana_login = tk.Tk() ventana_login.title("Login Ferretería") ventana_login.geometry("400x400")

Imagen decorativa (opcional, reemplaza 'logo.png' por la tuya)

try: imagen = PhotoImage(file="logo.png") tk.Label(ventana_login, image=imagen).pack() except: tk.Label(ventana_login, text="Sistema de Ferretería", font=("Arial", 16, "bold")).pack(pady=10)

Usuario y contraseña

tk.Label(ventana_login, text="Usuario:").pack() entry_usuario = tk.Entry(ventana_login) entry_usuario.pack(pady=5)

tk.Label(ventana_login, text="Contraseña:").pack() entry_contraseña = tk.Entry(ventana_login, show="*") entry_contraseña.pack(pady=5)

Botones

tk.Button(ventana_login, text="Iniciar Sesión", width=20, command=login).pack(pady=5) tk.Button(ventana_login, text="Crear Cuenta", width=20, command=crear_cuenta).pack(pady=5) tk.Button(ventana_login, text="Cambiar Contraseña", width=20, command=cambiar_contraseña).pack(pady=5)

ventana_login.mainloop()