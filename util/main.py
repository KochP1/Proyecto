from tkinter import *
from PIL import Image, ImageTk
import qrcode
import cv2
import webbrowser

# Creación de la ventana
app = Tk()
# Título de la ventana
app.title("Qr Generator")
# No permitir redimenzionar 
app.resizable(False, False)
# Icono de la ventana
app.iconbitmap("C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/241528.ico")
# Tamaño de la ventana en px (ancho x largo)
app.geometry("900x600")

# Funciones para los botones del menu
def generar_boton():
    
    # Eliminar widgets existentes en el cuerpo principal
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()
    
    framegen = Frame(cuerpo_principal, bg="#3489E5", width=300, height=200)
    framegen.pack(fill="both", expand=False)
    
    imgFrame = Image.open('C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/qr-code.jpg')
    imgFrame = imgFrame.resize((300, 200))  # Redimensionar (Ancho, Alto)
    imgFrame = ImageTk.PhotoImage(imgFrame)

    labelimg = Label(framegen, image=imgFrame)
    labelimg.image = imgFrame  # Asignar la imagen al atributo image del Label
    labelimg.grid(row=0, column=0, padx=(230, 0), pady=(1, 0))
    
    label_ruta = Label(cuerpo_principal, text="Ingresa la ruta donde se guardará la imagen del qr\n(C:\\Users\\USUARIO\\OneDrive\\Documents\\nombre.jpg)", font=("Arial", 15), bg="#3489E5")
    label_ruta.pack(side=TOP, anchor="center", pady=30)
    
    entry_ruta = Entry(cuerpo_principal, width=66)
    entry_ruta.pack(side=TOP, anchor="center", pady=5)
    
    label_data = Label(cuerpo_principal, text="Ingresa lo que va a contener el codigo qr", font=("Arial", 15), bg="#3489E5")
    label_data.pack(side=TOP, anchor="center", pady=30)
    
    entry_data = Entry(cuerpo_principal, width=66)
    entry_data.pack(side=TOP, anchor="center", pady=5)
    
    boton_generar = Button(cuerpo_principal, text="Generar", bg="purple", font=("Arial", 12), fg="black", command=lambda:generar_qr(entry_ruta.get(), entry_data.get()))
    boton_generar.pack(side=TOP, anchor="center", pady=10)
    


def volver_a_principal():
    
    # Eliminar widgets existentes en el cuerpo principal
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()

    # Volver a mostrar el contenido original en el cuerpo principal
    imgFrame2 = Image.open('C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/Presentacion.png')
    imgFrame2 = imgFrame2.resize((600, 400))  # Redimensionar (Ancho, Alto)
    imgFrame2 = ImageTk.PhotoImage(imgFrame2)

    labelPrinc = Label(cuerpo_principal, image=imgFrame2, width=600, height=400)
    labelPrinc.image = imgFrame2  # Asignar la imagen al atributo image del Label
    labelPrinc.grid(row=0, column=0, padx=(85, 0), pady=(40, 0))
    
def leer_boton():
    # Eliminar widgets existentes en el cuerpo principal
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()

    # Volver a mostrar el contenido original en el cuerpo principal
    imgFrame3 = Image.open('C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/readQr.jpg')
    imgFrame3 = imgFrame3.resize((600, 400))  # Redimensionar (Ancho, Alto)
    imgFrame3 = ImageTk.PhotoImage(imgFrame3)

    labelRead = Label(cuerpo_principal, image=imgFrame3, width=600, height=400, bg="#144B9E")
    labelRead.image = imgFrame3  # Asignar la imagen al atributo image del Label
    labelRead.pack(anchor="center")
    
    boton_leer = Button(cuerpo_principal, bg="#144B9E", image=img4, width=100, height=100, command=leer_Qr)
    boton_leer.pack(side=TOP, anchor="center")

# funciones para generar y leer un Qr
def leer_Qr(): 
    capture = cv2.VideoCapture(0)

    while capture.isOpened(): 
        ret, frame = capture.read()

        if cv2.waitKey(1) == ord("s"): 
            break

        qrDetector = cv2.QRCodeDetector()
        data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)

        if len(data) > 0: 
            print(f"Dato: {data}")
            abrir_enlace(data)
            cv2.imshow("webcam", rectifiedImage)
        else: 
            cv2.imshow("webcam", frame)

    capture.release()
    cv2.destroyAllWindows()

def abrir_enlace(enlace):
    webbrowser.open(enlace)
    
def generar_qr(ruta, data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    ruta = ruta.replace("\\", "/")
    img = qr.make_image(fill_color="blue", back_color="white")
    img.save(ruta)
    
def cambiar_color(color):
    cuerpo_principal.configure(background=color)

# Funciones para generar widgets y cambiar de color 

def generar_boton_y_cambiar_color():
    generar_boton()
    cambiar_color("#3489E5")

def home_boton_y_cambiar_color(): 
    volver_a_principal()
    cambiar_color("#1EA292")
    
def leer_boton_y_cambiar_color(): 
    leer_boton()
    cambiar_color("#144B9E")
    
    
# Imagen para el botón home
img = Image.open('C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/home.jpg')
img = img.resize((100, 100))  # Redimensionar (Ancho, Alto)
img = ImageTk.PhotoImage(img)

# Imagen para el boton de generar 
img2 = Image.open('C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/BotonQR.png')
img2 = img2.resize((100, 100))  # Redimensionar (Ancho, Alto)
img2 = ImageTk.PhotoImage(img2)

# Imagen para el boton leer 
img3 = Image.open('C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/Botonleer.png')
img3 = img3.resize((100, 100))  # Redimensionar (Ancho, Alto)
img3 = ImageTk.PhotoImage(img3)

# Imagen para el boton leer
img4 = Image.open('C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/camara2.jpg')
img4 = img4.resize((100, 100))  # Redimensionar (Ancho, Alto)
img4 = ImageTk.PhotoImage(img4)

# Barra colocada arriba
top_bar = Frame(app, bg="#1f2329", height=50)
top_bar.pack(side=TOP, fill="both")

# Menú de opciones
left_bar = Frame(app, bg="#2a3138", width=100)
left_bar.pack(side=LEFT, fill="both", expand=False)

# Frame principal
cuerpo_principal = Frame(app, bg="#1EA292")
cuerpo_principal.pack(side=RIGHT, fill="both", expand=True)

# Botón para el menú de opciones
boton_home = Button(left_bar, image=img, bg="#337EB3", width=100, height=100, command=home_boton_y_cambiar_color)
boton_home.pack(side=TOP, padx=10, pady=30)

boton_generar = Button(left_bar, image=img2, bg="#337EB3", width=100, height=100, command=generar_boton_y_cambiar_color)
boton_generar.pack(side=TOP, padx=10, pady=30)

boton_leer = Button(left_bar, image=img3, bg="#337EB3", width=100, height=100, command=leer_boton_y_cambiar_color)
boton_leer.pack(side=TOP, padx=10, pady=30)

# Label del widget principal 

imgFrame2 = Image.open('C:/Users/USUARIO/OneDrive/Documents/Proyecto/imagenes/Presentacion.png')
imgFrame2 = imgFrame2.resize((600, 400))  # Redimensionar (Ancho, Alto)
imgFrame2 = ImageTk.PhotoImage(imgFrame2)

labelPrinc = Label(cuerpo_principal, image=imgFrame2, width=600, height=400)
labelPrinc.image = imgFrame2  # Asignar la imagen al atributo image del Label
labelPrinc.grid(row=0, column=0, padx=(85, 0), pady=(40, 0))

app.mainloop()