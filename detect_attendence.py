import cv2
import face_recognition
import pickle
from datetime import datetime
import csv
import os
import pyttsx3
from playsound import playsound
import pandas as pd

def play_sound():
    SOUND_PATH = r"C:\Users\devpa\OneDrive\Desktop\F-AI Attendance\Sample Files\ding-36029.mp3"
    if os.path.exists(SOUND_PATH):
        playsound(SOUND_PATH)

def csv_to_excel():
    csv_file = "Attendance_" + datetime.now().strftime("%Y-%m-%d") + ".csv"
    excel_file = "Attendance_" + datetime.now().strftime("%Y-%m-%d") + ".xlsx"

    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        df.to_excel(excel_file, index=False)
        print(f"Converted {csv_file} to {excel_file}")

def mark_attendance(name):
    names = []
    now = datetime.now()
    file_name = now.strftime("%Y-%m-%d")

    if os.path.exists(f"Attendance_{file_name}.csv"):
        with open(f"Attendance_{file_name}.csv", "r") as file:
            reader = csv.reader(file)
            names = [row[0] for row in reader if row]

    if name not in names:
        with open(f"Attendance_{file_name}.csv", "a", newline="") as file:
            writer = csv.writer(file)
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([name, date_time])
            engine = pyttsx3.init()
            engine.say(f"Welcome {name}")
            engine.runAndWait()
            play_sound()
    else:
        engine = pyttsx3.init()
        engine.say(f"{name} already marked")
        engine.runAndWait()

def mark_attendance_with_face():
    with open("encodings.pkl", "rb") as file:
        data = pickle.load(file)

    known_encodings = data["encodings"]
    known_names = data["names"]

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        r, frame = cap.read()
        if r:
            frame = cv2.resize(frame, (500, 300))
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb)
            face_encodings = face_recognition.face_encodings(rgb, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    matched_indices = [i for i, match in enumerate(matches) if match]
                    counts = {}
                    for i in matched_indices:
                        name = known_names[i]
                        counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)

                (top, right, bottom, left) = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                if name != "Unknown":
                    mark_attendance(name)

            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()

    response = input("Do you want to convert this file to Excel? (y/n): ")
    if response.lower() == "y":
        csv_to_excel()
    else:
        print("Exiting without conversion.")
if __name__ == "__main__":
    mark_attendance_with_face()