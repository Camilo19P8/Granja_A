import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# Conectar a la base de datos SQL Server
def conectar_bd():
    try:
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=CAMILO19P8\SQLEXPRESS;'
            'DATABASE=Gestion_Granja;'
            'Trusted_Connection=yes;'
        )
        return conexion
    except pyodbc.Error as error:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {error}")
        return None

# Función para agregar un cultivo a la base de datos
def agregar_cultivo():
    nombre = entry_nombre_cultivo.get()
    tipo = entry_tipo_cultivo.get()
    area = entry_area_cultivo.get()
    rendimiento = entry_rendimiento_cultivo.get()

    if nombre and tipo and area and rendimiento:
        try:
            conexion = conectar_bd()
            if conexion:
                cursor = conexion.cursor()
                consulta = "INSERT INTO cultivos (nombre, tipo, area, rendimiento) VALUES (?, ?, ?, ?)"
                datos = (nombre, tipo, area, rendimiento)
                cursor.execute(consulta, datos)
                conexion.commit()
                messagebox.showinfo("Éxito", "Cultivo agregado correctamente")
                limpiar_campos_cultivo()
                conexion.close()
        except pyodbc.Error as error:
            messagebox.showerror("Error", f"No se pudo agregar el cultivo: {error}")
    else:
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos")

# Función para consultar los cultivos en la base de datos
def consultar_cultivos():
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM cultivos")
            cultivos = cursor.fetchall()
            mostrar_tabla(cultivos)
            conexion.close()
    except pyodbc.Error as error:
        messagebox.showerror("Error", f"No se pudo consultar los cultivos: {error}")

# Función para modificar un cultivo en la base de datos
def modificar_cultivo():
    # Obtener el ID del cultivo seleccionado en la tabla
    seleccion = tabla_cultivos.focus()
    if seleccion:
        id_cultivo = tabla_cultivos.item(seleccion)['text']
        nombre = entry_nombre_cultivo.get()
        tipo = entry_tipo_cultivo.get()
        area = entry_area_cultivo.get()
        rendimiento = entry_rendimiento_cultivo.get()

        if nombre and tipo and area and rendimiento:
            try:
                conexion = conectar_bd()
                if conexion:
                    cursor = conexion.cursor()
                    consulta = "UPDATE cultivos SET nombre = ?, tipo = ?, area = ?, rendimiento = ? WHERE id = ?"
                    datos = (nombre, tipo, area, rendimiento, id_cultivo)
                    cursor.execute(consulta, datos)
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Cultivo modificado correctamente")
                    limpiar_campos_cultivo()
                    conexion.close()
            except pyodbc.Error as error:
                messagebox.showerror("Error", f"No se pudo modificar el cultivo: {error}")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos")
    else:
        messagebox.showwarning("Cultivo no seleccionado", "Por favor seleccione un cultivo de la tabla")

# Función para eliminar un cultivo de la base de datos
def eliminar_cultivo():
    # Obtener el ID del cultivo seleccionado en la tabla
    seleccion = tabla_cultivos.focus()
    if seleccion:
        id_cultivo = tabla_cultivos.item(seleccion)['text']
        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar este cultivo?")
        if respuesta:
            try:
                conexion = conectar_bd()
                if conexion:
                    cursor = conexion.cursor()
                    consulta = "DELETE FROM cultivos WHERE id = ?"
                    datos = (id_cultivo,)
                    cursor.execute(consulta, datos)
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Cultivo eliminado correctamente")
                    conexion.close()
            except pyodbc.Error as error:
                messagebox.showerror("Error", f"No se pudo eliminar el cultivo: {error}")
    else:
        messagebox.showwarning("Cultivo no seleccionado", "Por favor seleccione un cultivo de la tabla")

# Función para limpiar los campos de entrada de cultivos
def limpiar_campos_cultivo():
    entry_nombre_cultivo.delete(0, tk.END)
    entry_tipo_cultivo.delete(0, tk.END)
    entry_area_cultivo.delete(0, tk.END)
    entry_rendimiento_cultivo.delete(0, tk.END)

# Función para mostrar los cultivos en la tabla
def mostrar_tabla(cultivos):
    # Limpiar la tabla si ya hay datos
    for i in tabla_cultivos.get_children():
        tabla_cultivos.delete(i)
    # Insertar los nuevos datos
    for cultivo in cultivos:
        tabla_cultivos.insert("", tk.END, text=cultivo[0], values=cultivo[1:])

# Función para agregar un animal a la base de datos
def agregar_animal():
    especie = entry_especie.get()
    raza = entry_raza.get()
    edad = entry_edad.get()
    peso = entry_peso.get()

    if especie and raza and edad and peso:
        try:
            conexion = conectar_bd()
            if conexion:
                cursor = conexion.cursor()
                consulta = "INSERT INTO animales (especie, raza, edad, peso) VALUES (?, ?, ?, ?)"
                datos = (especie, raza, edad, peso)
                cursor.execute(consulta, datos)
                conexion.commit()
                messagebox.showinfo("Éxito", "Animal agregado correctamente")
                limpiar_campos_animal()
                conexion.close()
        except pyodbc.Error as error:
            messagebox.showerror("Error", f"No se pudo agregar el animal: {error}")
    else:
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos")

# Función para consultar los animales en la base de datos
def consultar_animales():
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM animales")
            animales = cursor.fetchall()
            mostrar_tabla_animales(animales)
            conexion.close()
    except pyodbc.Error as error:
        messagebox.showerror("Error", f"No se pudo consultar los animales: {error}")

# Función para modificar un animal en la base de datos
def modificar_animal():
    # Obtener el ID del animal seleccionado en la tabla
    seleccion = tabla_animales.focus()
    if seleccion:
        id_animal = tabla_animales.item(seleccion)['text']
        especie = entry_especie.get()
        raza = entry_raza.get()
        edad = entry_edad.get()
        peso = entry_peso.get()

        if especie and raza and edad and peso:
            try:
                conexion = conectar_bd()
                if conexion:
                    cursor = conexion.cursor()
                    consulta = "UPDATE animales SET especie = ?, raza = ?, edad = ?, peso = ? WHERE id = ?"
                    datos = (especie, raza, edad, peso, id_animal)
                    cursor.execute(consulta, datos)
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Animal modificado correctamente")
                    limpiar_campos_animal()
                    conexion.close()
            except pyodbc.Error as error:
                messagebox.showerror("Error", f"No se pudo modificar el animal: {error}")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos")
    else:
        messagebox.showwarning("Animal no seleccionado", "Por favor seleccione un animal de la tabla")

# Función para eliminar un animal de la base de datos
def eliminar_animal():
    # Obtener el ID del animal seleccionado en la tabla
    seleccion = tabla_animales.focus()
    if seleccion:
        id_animal = tabla_animales.item(seleccion)['text']
        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar este animal?")
        if respuesta:
            try:
                conexion = conectar_bd()
                if conexion:
                    cursor = conexion.cursor()
                    consulta = "DELETE FROM animales WHERE id = ?"
                    datos = (id_animal,)
                    cursor.execute(consulta, datos)
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Animal eliminado correctamente")
                    conexion.close()
            except pyodbc.Error as error:
                messagebox.showerror("Error", f"No se pudo eliminar el animal: {error}")
    else:
        messagebox.showwarning("Animal no seleccionado", "Por favor seleccione un animal de la tabla")

# Función para limpiar los campos de entrada de animales
def limpiar_campos_animal():
    entry_especie.delete(0, tk.END)
    entry_raza.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_peso.delete(0, tk.END)

# Función para mostrar los animales en la tabla
def mostrar_tabla_animales(animales):
    # Limpiar la tabla si ya hay datos
    for i in tabla_animales.get_children():
        tabla_animales.delete(i)
    # Insertar los nuevos datos
    for animal in animales:
        tabla_animales.insert("", tk.END, text=animal[0], values=animal[1:])

# Función para generar un reporte de la producción total de la granja
def generar_reporte_produccion():
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            # Obtener información de los cultivos
            cursor.execute("SELECT COUNT(*), SUM(area), SUM(rendimiento) FROM cultivos")
            cultivos_info = cursor.fetchone()

            # Obtener información de los animales
            cursor.execute("SELECT COUNT(DISTINCT especie), AVG(edad), AVG(peso) FROM animales")
            animales_info = cursor.fetchone()

            # Calcular el peso total de los animales
            cursor.execute("SELECT SUM(peso) FROM animales")
            peso_total_animales = cursor.fetchone()[0]
            if peso_total_animales is None:
                peso_total_animales = 0

            # Generar el reporte
            reporte_texto = ""
            reporte_texto += "Reporte de Producción de la Granja\n"
            reporte_texto += "====================================\n"
            reporte_texto += f"Cantidad de Cultivos: {cultivos_info[0]}\n"
            reporte_texto += f"Área Total de Cultivos: {cultivos_info[1]} m^2\n"
            reporte_texto += f"Rendimiento Total de Cultivos: {cultivos_info[2]} unidades\n"
            reporte_texto += "------------------------------------\n"
            reporte_texto += f"Cantidad de Especies de Animales: {animales_info[0]}\n"
            reporte_texto += f"Promedio de Edad de las Especies de Animales: {animales_info[1]:.2f} años\n"
            reporte_texto += f"Promedio de Peso de las Especies de Animales: {animales_info[2]:.2f} kg\n"
            reporte_texto += f"Peso total de las Especies de Animales: {peso_total_animales} kg\n"

            # Actualizar el contenido del Texto
            tab_produccion_texto.config(state=tk.NORMAL)
            tab_produccion_texto.delete("1.0", tk.END)
            tab_produccion_texto.insert(tk.END, reporte_texto)
            tab_produccion_texto.config(state=tk.DISABLED)

            conexion.close()
    except pyodbc.Error as error:
        messagebox.showerror("Error", f"No se pudo generar el reporte de producción: {error}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Granja")

# Crear pestañas
pestanas = ttk.Notebook(ventana)

# Pestaña de Cultivos
pestana_cultivos = ttk.Frame(pestanas)
pestanas.add(pestana_cultivos, text="Cultivos")

# Marco para los campos de entrada de cultivos
marco_campos_cultivos = ttk.LabelFrame(pestana_cultivos, text="Agregar Cultivo")
marco_campos_cultivos.grid(row=0, column=0, padx=10, pady=5, sticky="we")

# Campos de entrada de cultivos
etiqueta_nombre_cultivo = ttk.Label(marco_campos_cultivos, text="Nombre:")
etiqueta_nombre_cultivo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_nombre_cultivo = ttk.Entry(marco_campos_cultivos)
entry_nombre_cultivo.grid(row=0, column=1, padx=5, pady=5, sticky="we")

etiqueta_tipo_cultivo = ttk.Label(marco_campos_cultivos, text="Tipo:")
etiqueta_tipo_cultivo.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_tipo_cultivo = ttk.Entry(marco_campos_cultivos)
entry_tipo_cultivo.grid(row=1, column=1, padx=5, pady=5, sticky="we")

etiqueta_area_cultivo = ttk.Label(marco_campos_cultivos, text="Área:")
etiqueta_area_cultivo.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_area_cultivo = ttk.Entry(marco_campos_cultivos)
entry_area_cultivo.grid(row=2, column=1, padx=5, pady=5, sticky="we")

etiqueta_rendimiento_cultivo = ttk.Label(marco_campos_cultivos, text="Rendimiento:")
etiqueta_rendimiento_cultivo.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_rendimiento_cultivo = ttk.Entry(marco_campos_cultivos)
entry_rendimiento_cultivo.grid(row=3, column=1, padx=5, pady=5, sticky="we")

# Botones para acciones de cultivos
btn_agregar_cultivo = ttk.Button(marco_campos_cultivos, text="Agregar Cultivo", command=agregar_cultivo)
btn_agregar_cultivo.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

btn_consultar_cultivos = ttk.Button(pestana_cultivos, text="Consultar Cultivos", command=consultar_cultivos)
btn_consultar_cultivos.grid(row=1, column=0, padx=10, pady=5, sticky="we")

btn_modificar_cultivo = ttk.Button(pestana_cultivos, text="Modificar Cultivo", command=modificar_cultivo)
btn_modificar_cultivo.grid(row=2, column=0, padx=10, pady=5, sticky="we")

btn_eliminar_cultivo = ttk.Button(pestana_cultivos, text="Eliminar Cultivo", command=eliminar_cultivo)
btn_eliminar_cultivo.grid(row=3, column=0, padx=10, pady=5, sticky="we")

# Tabla para mostrar los cultivos
tabla_cultivos = ttk.Treeview(pestana_cultivos, columns=("Nombre", "Tipo", "Área", "Rendimiento"))
tabla_cultivos.heading("#0", text="ID")
tabla_cultivos.column("#0", width=50)
tabla_cultivos.heading("Nombre", text="Nombre")
tabla_cultivos.heading("Tipo", text="Tipo")
tabla_cultivos.heading("Área", text="Área")
tabla_cultivos.heading("Rendimiento", text="Rendimiento")
tabla_cultivos.grid(row=0, column=1, rowspan=4, padx=10, pady=5, sticky="nsew")

# Configurar el gestor de geometría de la pestaña de cultivos
pestana_cultivos.rowconfigure(0, weight=1)
pestana_cultivos.columnconfigure(1, weight=1)

# Pestaña de Ganado
pestana_ganado = ttk.Frame(pestanas)
pestanas.add(pestana_ganado, text="Ganado")

# Marco para los campos de entrada de ganado
marco_campos_ganado = ttk.LabelFrame(pestana_ganado, text="Agregar Animal")
marco_campos_ganado.grid(row=0, column=0, padx=10, pady=5, sticky="we")

# Campos de entrada de ganado
etiqueta_especie = ttk.Label(marco_campos_ganado, text="Especie:")
etiqueta_especie.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_especie = ttk.Entry(marco_campos_ganado)
entry_especie.grid(row=0, column=1, padx=5, pady=5, sticky="we")

etiqueta_raza = ttk.Label(marco_campos_ganado, text="Raza:")
etiqueta_raza.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_raza = ttk.Entry(marco_campos_ganado)
entry_raza.grid(row=1, column=1, padx=5, pady=5, sticky="we")

etiqueta_edad = ttk.Label(marco_campos_ganado, text="Edad:")
etiqueta_edad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_edad = ttk.Entry(marco_campos_ganado)
entry_edad.grid(row=2, column=1, padx=5, pady=5, sticky="we")

etiqueta_peso = ttk.Label(marco_campos_ganado, text="Peso:")
etiqueta_peso.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_peso = ttk.Entry(marco_campos_ganado)
entry_peso.grid(row=3, column=1, padx=5, pady=5, sticky="we")

# Botones para acciones de ganado
btn_agregar_ganado = ttk.Button(marco_campos_ganado, text="Agregar Animal", command=agregar_animal)
btn_agregar_ganado.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

btn_consultar_ganado = ttk.Button(pestana_ganado, text="Consultar Animales", command=consultar_animales)
btn_consultar_ganado.grid(row=1, column=0, padx=10, pady=5, sticky="we")

btn_modificar_ganado = ttk.Button(pestana_ganado, text="Modificar Animal", command=modificar_animal)
btn_modificar_ganado.grid(row=2, column=0, padx=10, pady=5, sticky="we")

btn_eliminar_ganado = ttk.Button(pestana_ganado, text="Eliminar Animal", command=eliminar_animal)
btn_eliminar_ganado.grid(row=3, column=0, padx=10, pady=5, sticky="we")

# Tabla para mostrar los animales
tabla_animales = ttk.Treeview(pestana_ganado, columns=("Especie", "Raza", "Edad", "Peso"))
tabla_animales.heading("#0", text="ID")
tabla_animales.column("#0", width=50)
tabla_animales.heading("Especie", text="Especie")
tabla_animales.heading("Raza", text="Raza")
tabla_animales.heading("Edad", text="Edad")
tabla_animales.heading("Peso", text="Peso")
tabla_animales.grid(row=0, column=1, rowspan=4, padx=10, pady=5, sticky="nsew")

# Configurar el gestor de geometría de la pestaña de ganado
pestana_ganado.rowconfigure(0, weight=1)
pestana_ganado.columnconfigure(1, weight=1)

# Pestaña de Producción Total
tab_produccion = ttk.Frame(pestanas)
pestanas.add(tab_produccion, text="Producción Total")

# Texto para mostrar el reporte de producción total
tab_produccion_texto = tk.Text(tab_produccion, wrap="word", state=tk.DISABLED)
tab_produccion_texto.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Botones para calcular producción total y generar reporte
btn_generar_reporte = ttk.Button(tab_produccion, text="Generar Reporte", command=generar_reporte_produccion)
btn_generar_reporte.grid(row=1, column=0, padx=5, pady=5, sticky="we")

# Agregar pestañas al gestor de geometría de la ventana principal
pestanas.pack(expand=1, fill="both")

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
