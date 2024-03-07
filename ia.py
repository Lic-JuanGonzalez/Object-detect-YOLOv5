import datetime
import torch
import cv2
import numpy as np
import pandas as pd
import sys  # Importamos el módulo sys para redirigir la salida

# Redireccionamos la salida estándar y los errores a un archivo
with open("Registro.txt", "w") as archivo:
    sys.stdout = archivo
    sys.stderr = archivo

    # Cargamos el modelo
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/Projectos/Python/IA Detect/video/model/best.pt')

    # Habilitamos la cámara
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        detect = model(frame)

        info = detect.pandas().xyxy[0]

        hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(hora_actual, info)  # Esta salida se guardará en el archivo

        cv2.imshow('deteccion', np.squeeze(detect.render()))

        t = cv2.waitKey(5)
        if t == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Restablecemos la salida estándar y los errores a sus valores originales
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__