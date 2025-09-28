import numpy as np
import cv2

# Créer une image 300x300 pixels, remplie de blanc (255)
img = np.ones((300, 300), dtype=np.uint8) * 255

# Dessiner un carré noir (0)
img[100:200, 100:200] = 0

cv2.imshow("Image NumPy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


 #Ce programme vise a creer un rectangle noir au milieu d'un
 # ecran en utilisant le module "numpy" et la bibliotheque "OpenCV"
