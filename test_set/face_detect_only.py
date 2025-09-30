import cv2
from face_resizer_display import resizing_frame

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(0)

def detect_bounding_box(vid):
    scaleFactor = 1.1
    minNeighbors = 6
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors, minSize=(50, 50))
    for (x, y, w, h) in faces:
        # Dessiner des points aux 4 coins du rectangle
        cv2.circle(vid, (x, y), 5, (0, 0, 255), -1)           
        cv2.circle(vid, (x + w, y), 5, (0, 0, 255), -1)       
        cv2.circle(vid, (x, y + h), 5, (0, 0, 255), -1)      
        cv2.circle(vid, (x + w, y + h), 5, (0, 0, 255), -1)   

        # Dessiner un point au centre
        cv2.circle(vid, (x + w//2, y + h//2), 5, (255, 0, 0), -1)

    return faces

while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  

    faces = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    cv2.imshow(
        "My Face Detection Project", video_frame
    )  

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

resizing_frame(video_frame)

video_capture.release()
cv2.destroyAllWindows()

