# CCTV-Entry-Detection
A YOLOv8-based CCTV entry detection system with timestamp verification


This project uses **YOLOv8** and **Tesseract OCR** to detect people from CCTV footage and verify their entry time.

## 📌 Features:
- **Real-time person detection** using YOLOv8.
- **Extracts timestamp** from CCTV footage using OCR.
- **Compares entry time** with a predefined cutoff (e.g., 6:30 AM).
- **Saves detected frame** with a bounding box.

## 🚀 How to Run:
1. Install dependencies:
   
   !pip install ultralytics opencv-python pytesseract
   !apt-get install -y tesseract-ocr
   
Run the script:
python main.py
Upload a video and check the result in detected_entry.jpg.



🤖 Technologies Used:
Python
OpenCV
YOLOv8
Tesseract OCR
