import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# load known faces

utkarsh_image = face_recognition.load_image_file("faces/utkarsh.jpg")
utkarsh_encoding = face_recognition.face_encoding(utkarsh_image)[0]

rohan_image = face_recognition.load_image_file("faces/rohan.jpg")
rohan_encoding = face_recognition.face_encoding(rohan_image)[0]

known_face_encoding = [utkarsh_encoding, rohan_encoding]
known_face_names = ["Utkarsh", "Rohan"]

# list of expected students
students = known_face_names.copy()

face_locations = []
face_encoding = []

# Get the current date and time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", newline = " ")
lnwriter = csv.writer(f)


while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Recognize faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encoding = face_recognition.face_encoding(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
         matches = face_recogination.compare_faces(know_face_encoding, face_encoding)

         face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)

         best_match_index = np.argmin(face_distance)

        if (matches[best_match_index]):
            name = known_face_names[best_match_index]
        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0*FF == ord("q"):
         break