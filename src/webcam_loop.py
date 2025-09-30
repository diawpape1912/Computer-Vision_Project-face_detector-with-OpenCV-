import cv2
from image_drawing import image_PIL_convert
import numpy as np


def webcamLoop(webcam, detect_green_box):
    #Boucle de recuperation et d'affichage des images de la webcam
    while (True):
        ret, frame = webcam.read()
        #Si la capture a échoué, on quitte la boucle
        if ret is False:
            print("Erreur de capture d'image")
            break
        #Effet mirroir horizontal
        frame = np.fliplr(frame)
        #Appel de la fonction de detection de visage
        faces = detect_green_box(frame)
        frame = image_PIL_convert(frame, faces)
        #Affichage de l'image traitée dans une fenêtre nommée "Face Detection"
        cv2.imshow("My face detection ", frame)
        #Sortie de la boucle si la touche 'q' est pressée
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break