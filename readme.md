# 🎯 Face Recognition Attendance System

This project uses **face recognition** to automatically mark attendance using a webcam. It captures face images, generates encodings, and detects students in real-time — storing attendance records in a `.csv` file.

---

## 🚀 How It Works

1. **Capture Face Images**

   - Run `capture_faces.py` to store face images of each person in `dataset/<person_name>/`.

2. **Generate Encodings**

   - Run `gen_encoding.py` to convert the stored images into facial encodings.
   - These encodings are saved in `encodings.pkl`.

3. **Mark Attendance**

   - Run `detect_attendence.py` to start the webcam and detect faces in real-time.
   - If a face matches a known encoding, it logs the name, date, and time in `attendance.csv`.

4. **Send Attendance Report via Email**
   - Run `attendence_on_email.py` to send the attendance CSV via email (make sure to configure your email settings in the script).

---

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/) – for capturing and processing images
- [face_recognition](https://github.com/ageitgey/face_recognition) – for facial feature detection
- [pickle](https://docs.python.org/3/library/pickle.html) – for storing facial encodings
- [CSV](https://docs.python.org/3/library/csv.html) – for attendance logging

---

## ✅ Requirements

Install the required packages:

```bash
pip install opencv-python face_recognition numpy
```
