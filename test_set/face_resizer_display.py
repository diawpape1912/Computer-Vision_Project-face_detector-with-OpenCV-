import cv2

def resizing_frame(video_frame):
    #Récupération et affichage des valeurs (RGB) de la capture initiale
    ini_size = video_frame.shape
    #Redimensionnement de l'image capturée pour affichage
    new_size = (500, 600)
    frame_resized = cv2.resize(video_frame, new_size)
    print("Initial size (Height, Width, Channels): ", ini_size)
    print("Resized image shape (Height, Width, Channels): ", frame_resized.shape)
    print(resizing_frame)
    #Affichage de l'image redimensionnée
    cv2.imshow('Resized frame', frame_resized)