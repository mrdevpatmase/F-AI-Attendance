import os
import cv2
import numpy as np
import face_recognition
import pickle


dataset_path = r"C:\Users\devpa\OneDrive\Desktop\F-AI Attendance\dataset"              ## stored images
encodings_path = r"C:\Users\devpa\OneDrive\Desktop\F-AI Attendance\encodings.pkl"      ## stored encodings from images

known_encodings = []
known_names = []

def generate_encodings(dataset_path, encodings_path):
    for person_name in os.listdir(dataset_path):
        person_folder = os.path.join(dataset_path,person_name)

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


generate_encodings(dataset_path, encodings_path)


# data = {"name": "dev", "age": 22}
# with open("encodings.pkl", "wb") as file:
#     pickle.dump(data, file)


# with open("data.pkl", "rb") as file:
#     loaded_data = pickle.load(file)

# print(loaded_data)  # Output: {'name': 'Dev', 'age': 22}

