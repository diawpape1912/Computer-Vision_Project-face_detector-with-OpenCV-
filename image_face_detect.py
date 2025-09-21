import cv2

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

imagePath = 'pictures/visage.jpeg'
imageRead = cv2.imread(imagePath)
if imageRead is None:
    print("Erreur : impossible de lire l'image ! Vérifie le chemin.")
    exit()

# Redimensionner pour affichage
new_size = (600, 400)
img_Display = cv2.resize(imageRead, new_size)

# Convertir en niveaux de gris pour la détection
gray_img = cv2.cvtColor(img_Display, cv2.COLOR_BGR2GRAY)

# Détecter les visages
faces = face_detector.detectMultiScale(
    gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
)

print("Nombre de visages détectés :", len(faces))

# Dessiner les rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img_Display, (x, y), (x + w, y + h), (0, 255, 0), 4)

# Afficher l'image finale
cv2.namedWindow('Visages détectés', cv2.WINDOW_NORMAL)
cv2.imshow('Visages détectés', img_Display)

cv2.waitKey(0)
cv2.destroyAllWindows()
