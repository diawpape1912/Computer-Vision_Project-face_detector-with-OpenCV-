from PIL import Image, ImageDraw
import cv2
import numpy as np


#Dessiner un rectangle autour du visage 
def image_PIL_convert(vid, faces):
    #Convertion OpenCV -> PIL
    image_PIL = Image.fromarray(cv2.cvtColor(vid, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image_PIL)
    # Dessiner un rectangle sur le visage 
    for (x, y, w, h) in faces:
        T_left = (x, y)
        B_right = (x + w, y + h)

        draw.rectangle([T_left, B_right], outline = "red", width = 3)

    #Reconvertion de PIL -> OpenCV
    return cv2.cvtColor(np.array(image_PIL), cv2.COLOR_RGB2BGR)
    