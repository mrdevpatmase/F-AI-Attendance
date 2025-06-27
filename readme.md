# 🎯 Face Recognition Attendance System

This project uses **face recognition** to automatically mark attendance using a webcam. It captures face images, generates encodings, and detects students in real-time — storing attendance records in a `.csv` file.

---

## 📁 Project Structure

├── 01_Project/
│ ├── capture_faces.py # Capture face images for each person
│ ├── gen_encoding.py # Generate face encodings from images
│ ├── detect_attendence.py # Real-time face detection & attendance
│ ├── encodings.pkl # Pickle file storing encoded face data
├── dataset/
│ ├── name_1/
│ └── name_2/
│ ├── name_3/
│ └── name_4/
├── attendance.csv # Output attendance log

---

## 🚀 How It Works

1. **Capture Face Images**

   - Run `capture_faces.py` to store face images of each person in `dataset/<person_name>/`.

2. **Generate Encodings**

   - Run `gen_encoding.py` to convert those images into encodings and save them in `encodings.pkl`.

3. **Mark Attendance**
   - Run `detect_attendence.py` to detect faces using a webcam.
   - If the face matches, it logs the name, date, and time in `attendance.csv`.

---

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/) – for capturing and processing images
- [face_recognition](https://github.com/ageitgey/face_recognition) – for facial feature detection
- [pickle](https://docs.python.org/3/library/pickle.html) – for storing encodings
- [CSV](https://docs.python.org/3/library/csv.html) – for attendance logs

---

## ✅ Requirements

Install required packages using:

```bash
pip install opencv-python face_recognition numpy
```
