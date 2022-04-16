import cv2
import numpy as np
import winsound
from datetime import datetime

# Determine the center point of the given shape
def calc_center(indexes, points, img, draw=False):
    (cx, cy), radius = cv2.minEnclosingCircle(
            points[indexes])

    center = np.array([cx, cy], dtype=np.int32)

    if draw:
        cv2.circle(img, center, int(radius),
            (0, 0, 255), 1, cv2.LINE_AA)

    return center

# Determine the direction of the eye
def eye_direction(iris_center, eye_center):
    if abs(iris_center[0] - eye_center[0]) < 5:
        return "CENTER"
    elif iris_center[0] - eye_center[0] < 0:
        return "LEFT"
    elif iris_center[0]-eye_center[0] > 0:
        return "RIGHT"

# Play the audio file
def play_sound():
    audio_file = "warning.wav"
    winsound.PlaySound(audio_file, winsound.SND_FILENAME)

# Warn the user and the supervisor that their attention is elsewhere 
# and should pay attention to the screen
def warn(img):
    h, w, c = img.shape
    cv2.rectangle(img, (0,0), (w, h), (0, 0, 255), -1)
    cv2.putText(img, "You have lost focus", (150, 250), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 4)
    cv2.imshow("ADHD Aid", img)
    cv2.waitKey(1)

    play_sound()

    # Record when the user first loses focus into log.txt
    now = datetime.now()
    cur_time = now.strftime("%H:%M:%S")

    with open("log.txt", "a") as f:
        f.write("User has lost focus from " + cur_time + " to ")
