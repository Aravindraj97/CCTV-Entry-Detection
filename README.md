# 🚀 YOLOv8 CCTV Entry Detection with Timestamp Verification

This project uses **YOLOv8** and **Tesseract OCR** to detect individuals entering a workspace via CCTV footage. The script extracts a timestamp from the video, verifies if the person arrived on time (before 6:30 AM), and saves the detected frame.

## 📌 Features:
✔ **Real-time person detection** using YOLOv8  
✔ **Extracts timestamp** from CCTV footage using OCR  
✔ **Compares entry time** with a predefined cutoff (6:30 AM)  
✔ **Saves detected frame** with a bounding box  

---

## ⚡ How to Run This Project on Google Colab

### **1️⃣ Open the Project in Google Colab**



---

### **2️⃣ Upload a CCTV Video**
Since Google Colab does not have direct access to local files, **you need to manually upload your video** when prompted.  

In the Colab notebook, run the following command to upload the video:  
```python
from google.colab import files
uploaded = files.upload()  # Select and upload the CCTV footage


3️⃣ Install Dependencies
Run the following command inside the Colab notebook to install required packages:

!pip install ultralytics opencv-python pytesseract

4️⃣ Run the Detection Script
Once the dependencies are installed, execute the detection script:

!python main.py 

5️⃣ View the Detection Results
The detected frame will be saved as detected_entry.jpg.
You can download the image using:
from google.colab import files
files.download("detected_entry.jpg")
