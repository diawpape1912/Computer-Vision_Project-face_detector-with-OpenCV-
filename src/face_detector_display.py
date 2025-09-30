#Importations des bibliothèques nécessaires 
import cv2



#Chargement du classificateur en cascade pour la détection de visage
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

#Implementation d'une fonction pour la detection de visage
def detect_green_box(vid):
    #Convertion de l'image capturée en niveaux de gris
    gray_frame=cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    #Detection des visages dans l'image en niveaux de gris
    faces = face_detector.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=6, minSize=( 70, 70)
        )
    global_faces = len(faces)

    print("Nombre de visages détectés :", global_faces)
    return faces
    


