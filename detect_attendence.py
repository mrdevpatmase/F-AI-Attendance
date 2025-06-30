import cv2
import face_recognition
import pickle
from datetime import datetime
import csv
import os

# Function to mark attendance

# def mark_attendance(name):
    # with open("attendance.csv", "a", newline="") as file:
    #     writer = csv.writer(file)
    #     now = datetime.now()
    #     date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    #     if name not in open("attendance.csv").read():
    #         writer.writerow([name, date_time])
    #         print(f"Attendance marked for name {name} at {date_time}")

def mark_attendance(name):
    names = []

    # Read all existing names from the file
    if os.path.exists("attendance.csv"):
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            names = [row[0] for row in reader if row]

    # If name not in list, add it
    if name not in names:
        with open("attendance.csv", "a", newline="") as file:
            writer = csv.writer(file)
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([name, date_time])
            print(f"✅ Marked attendance for {name} at {date_time}")
    else:
        print(f"ℹ️ {name} already marked.")


with open("encodings.pkl", "rb") as file:
    data = pickle.load(file)

known_encodings = data["encodings"]
known_names = data["names"]

cap = cv2.VideoCapture(0)

while cap.isOpened():
    r, frame = cap.read()
    if r:
        frame = cv2.resize(frame, (500, 300))
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # moved before key check

        face_locations = face_recognition.face_locations(rgb)
        face_encodings = face_recognition.face_encodings(rgb, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"        
            if True in matches:
                matched_indices = [i for (i, match) in enumerate(matches) if match]
                counts = {}
                for i in matched_indices:
                    name = known_names[i]
                    counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)

            # Draw the face bounding box and label on the frame
            (top, right, bottom, left) = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Mark attendance for recognized faces
            if name != "Unknown":
                mark_attendance(name)

        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):   
            break

cap.release()
cv2.destroyAllWindows()

