import tkinter as tk
from tkinter import messagebox

# Funciones
def registrar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    año = entry_año.get()
    genero = genero_var.get()
    categorias = [categoria.get() for categoria in categorias_vars if categoria.get()]
    estado = estado_var.get()
    copias = entry_copias.get()
    resumen = text_resumen.get("1.0", tk.END).strip()
    idioma = idioma_var.get()

    detalles_libro = f"""
    Título: {titulo}
    Autor: {autor}
    Año de publicación: {año}
    Género: {genero}
    Categorías: {', '.join(categorias)}
    Estado: {estado}
    Número de copias: {copias}
    Resumen: {resumen}
    Idioma: {idioma}
    """
    print(detalles_libro)
    messagebox.showinfo("Registro exitoso", "El libro ha sido registrado exitosamente.")

def limpiar_formulario():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_año.delete(0, tk.END)
    for categoria in categorias_vars:
        categoria.set(0)
    genero_var.set(None)
    estado_var.set(None)
    entry_copias.delete(0, tk.END)
    text_resumen.delete("1.0", tk.END)
    idioma_var.set("Seleccione un idioma")

# Ventana principal
root = tk.Tk()
root.title("Registro de Libros - Biblioteca SaberX")
root.geometry("400x500")

# Frame de detalles del libro
frame_detalles = tk.Frame(root)
frame_detalles.pack(pady=10)

tk.Label(frame_detalles, text="Título:").grid(row=0, column=0)
entry_titulo = tk.Entry(frame_detalles)
entry_titulo.grid(row=0, column=1)

tk.Label(frame_detalles, text="Autor:").grid(row=1, column=0)
entry_autor = tk.Entry(frame_detalles)
entry_autor.grid(row=1, column=1)

tk.Label(frame_detalles, text="Año de publicación:").grid(row=2, column=0)
entry_año = tk.Entry(frame_detalles)
entry_año.grid(row=2, column=1)

# Frame de Género y Categoría
frame_genero_categoria = tk.LabelFrame(root, text="Género y Categoría")
frame_genero_categoria.pack(pady=10)

genero_var = tk.StringVar()

tk.Radiobutton(frame_genero_categoria, text="Ficción", variable=genero_var, value="Ficción").grid(row=0, column=0)
tk.Radiobutton(frame_genero_categoria, text="No Ficción", variable=genero_var, value="No Ficción").grid(row=0, column=1)

categorias_vars = [tk.StringVar() for _ in range(3)]
tk.Checkbutton(frame_genero_categoria, text="Novela", variable=categorias_vars[0], onvalue="Novela", offvalue="").grid(row=1, column=0)
tk.Checkbutton(frame_genero_categoria, text="Ciencia", variable=categorias_vars[1], onvalue="Ciencia", offvalue="").grid(row=1, column=1)
tk.Checkbutton(frame_genero_categoria, text="Historia", variable=categorias_vars[2], onvalue="Historia", offvalue="").grid(row=1, column=2)

# Frame de estado
frame_estado = tk.LabelFrame(root, text="Estado")
frame_estado.pack(pady=10)

estado_var = tk.StringVar()
tk.Radiobutton(frame_estado, text="Disponible", variable=estado_var, value="Disponible").pack(side=tk.LEFT)
tk.Radiobutton(frame_estado, text="Prestado", variable=estado_var, value="Prestado").pack(side=tk.LEFT)

# Frame de número de copias
frame_copias = tk.Frame(root)
frame_copias.pack(pady=10)

tk.Label(frame_copias, text="Número de copias:").grid(row=0, column=0)
entry_copias = tk.Entry(frame_copias)
entry_copias.grid(row=0, column=1)

# Frame de resumen
frame_resumen = tk.Frame(root)
frame_resumen.pack(pady=10)

tk.Label(frame_resumen, text="Resumen:").pack()
text_resumen = tk.Text(frame_resumen, height=5, width=40)
text_resumen.pack()

# Menú desplegable de idioma
idioma_var = tk.StringVar(value="Seleccione un idioma")
menu_idioma = tk.OptionMenu(root, idioma_var, "Español", "Inglés")
menu_idioma.pack(pady=10)

# Botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_registrar = tk.Button(frame_botones, text="Registrar Libro", command=registrar_libro)
btn_registrar.grid(row=0, column=0)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_formulario)
btn_limpiar.grid(row=0, column=1)

# Ejecutar la ventana
root.mainloop()
