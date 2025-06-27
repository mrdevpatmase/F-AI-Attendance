import cv2
import os

name =  input("Enter your name: \n")
folder_path = f"01_Project/dataset/{name}"

os.makedirs(folder_path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0
print("Press 's' to capture the image. Press 'q' to quit.")

while cap.isOpened():
    r, frame = cap.read()

    if not r:
        break

    frame = cv2.resize(frame, (500, 300))
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        img_name = os.path.join(folder_path, f"{name}_{count}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"[INFO] Image saved: {img_name}")
        count += 1

    elif key == ord("q"):
        print("[INFO] Quitting...")
        break


cap.release()