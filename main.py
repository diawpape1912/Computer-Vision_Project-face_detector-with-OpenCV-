#Importations des bibliothèques nécessaires
import numpy as np 
import matplotlib.pyplot as plt
import cv2
import sys


#Chargement du classificateur en cascade pour la détection de visage
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

#Initialisation et ouverture de la webcam
webcam = cv2.VideoCapture(0)

#Implementation d'une fonction pour la detection de visage
def detect_green_box(vid):
    #Convertion de l'image capturée en niveaux de gris
    gray_frame=cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    #Detection des visages dans l'image en niveaux de gris
    faces = face_detector.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=( 10, 10)
    )
    print("Nombre de visages détectés :", len(faces))
    #Dessiner les rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle( vid, (x, y), (x + w, y + h), (50, 255, 20), 2)
    return faces

#Boucle de recuperation et d'affichage des images de la webcam
while (True):
    ret, frame = webcam.read()
    #Si la capture a échoué, on quitte la boucle
    if ret is False:
        break
        print("Erreur de capture d'image")
    #Appel de la fonction de detection de visage
    faces = detect_green_box(frame)
    #Affichage de l'image traitée dans une fenêtre nommée "Face Detection"
    cv2.imshow("Face Detection", frame)
    #Sortie de la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()
        
#Récupération et affichage des valeurs (RGB) de la capture initiale
ini_size = frame.shape
#Redimensionnement de l'image capturée pour affichage
new_size = (500, 600)
frame_resized = cv2.resize(frame, new_size)
#Affichage de l'image redimensionnée
cv2.imshow('Resized frame', frame_resized)


#Libération de la webcam et fermeture des fenêtres
webcam.release()
cv2.destroyAllWindows()

