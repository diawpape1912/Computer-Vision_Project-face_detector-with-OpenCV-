import cv2

def resizing_frame(frame):
    global ini_size
    #Récupération et affichage des valeurs (RGB) de la capture initiale
    ini_size = frame.shape
    #Redimensionnement de l'image capturée pour affichage
    new_size = (500, 600)
    frame_resized = cv2.resize(frame, new_size)
    print(resizing_frame)
    #Affichage de l'image redimensionnée
    cv2.imshow('Resized frame', frame_resized)
    return frame_resized