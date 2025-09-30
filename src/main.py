from face_detector_display import detect_green_box
from image_drawing import image_PIL_convert
from webcam_loop import webcamLoop
import cv2


#Initialisation et ouverture de la webcam + boucle
webcam = cv2.VideoCapture(0)
webcamLoop(webcam, detect_green_box)


#Libération de la webcam et fermeture des fenêtres
webcam.release()
cv2.destroyAllWindows()



