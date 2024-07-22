import tkinter as tk
from tkinter import messagebox

def aplicar_limite():
    try:
        limit_download = int(download_entry.get())
        limit_upload = int(upload_entry.get())
        app_name = app_entry.get()
        # Aquí deberías incluir la lógica para aplicar los límites usando los valores recogidos
        messagebox.showinfo("Éxito", f"Límites aplicados:\nDownload: {limit_download}bps\nUpload: {limit_upload}bps\nApp: {app_name}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos para los límites.")

# Crear la ventana principal
root = tk.Tk()
root.title("UnalBandit")

# Crear y posicionar los campos de entrada y sus etiquetas
tk.Label(root, text="Limite de Bajada (KB/s):").grid(row=0, column=0)
download_entry = tk.Entry(root)
download_entry.grid(row=0, column=1)

tk.Label(root, text="Limite de Subida (KB/s):").grid(row=1, column=0)
upload_entry = tk.Entry(root)
upload_entry.grid(row=1, column=1)

tk.Label(root, text="Nombre de la Aplicación:").grid(row=2, column=0)
app_entry = tk.Entry(root)
app_entry.grid(row=2, column=1)

# Crear y posicionar el botón para aplicar los límites
apply_button = tk.Button(root, text="Aplicar Límite", command=aplicar_limite)
apply_button.grid(row=3, column=0, columnspan=2)

# Iniciar el bucle principal
root.mainloop()