import os
import cv2
import numpy as np
import face_recognition
import pickle

def generate_encodings(dataset_path="dataset", encodings_path="encodings.pkl"):
    known_encodings = []
    known_names = []

    for person_name in os.listdir(dataset_path):
        person_folder = os.path.join(dataset_path, person_name)
        if not os.path.isdir(person_folder):
            continue

        for image_name in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_name)
            image = cv2.imread(image_path)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            encodings = face_recognition.face_encodings(rgb)

            for encoding in encodings:
                known_encodings.append(encoding)
                known_names.append(person_name)

    data = {"encodings": known_encodings, "names": known_names}
    with open(encodings_path, "wb") as file:
        pickle.dump(data, file)

    print(f"[INFO] Encodings saved to {encodings_path}")

# ✅ Prevents auto-execution on import
if __name__ == "__main__":
    generate_encodings()
