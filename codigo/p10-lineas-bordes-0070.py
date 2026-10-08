# Axel Guzman 0070
import cv2
import numpy as np

# Cargar imagen del delfin
imagen = cv2.imread("imagenes/delfin.jpg")

# Verificar si la imagen se cargo correctamente
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a tipo float32
gris = np.float32(gris)

# Detectar esquinas con Harris
esquinas = cv2.cornerHarris(gris, 2, 3, 0.04)

# Dilatar las esquinas para hacerlas visibles
esquinas = cv2.dilate(esquinas, None)

# Crear una copia de la imagen original
resultado = imagen.copy()

# Marcar las esquinas detectadas en rojo
resultado[esquinas > 0.01 * esquinas.max()] = [0, 0, 255]

# Mostrar la imagen original
cv2.imshow("Delfin original 0070", imagen)

# Mostrar las esquinas detectadas
cv2.imshow("Esquinas detectadas 0070", resultado)

# Guardar el resultado
cv2.imwrite("resultados/delfin_esquinas.jpg", resultado)

print("Deteccion de esquinas terminada.")
print("Resultado guardado en resultados/delfin_esquinas.jpg")


# Esperar una tecla
cv2.waitKey(0)

# Cerrar las ventanas
cv2.destroyAllWindows()
print("Programa realizado por Axel Guzman 0070")