import cv2
import pytesseract
from ultralytics import YOLO
from datetime import datetime

# Load YOLOv8 model (pretrained)
model = YOLO("yolov8l.pt")

# Upload CCTV footage manually in Colab
from google.colab import files
uploaded = files.upload()

# Get the uploaded file name
video_path = list(uploaded.keys())[0]

# Open the uploaded video
cap = cv2.VideoCapture(video_path)

# Define the cut-off time (6:30 AM)
CHECK_TIME = datetime.strptime("06:30:00", "%H:%M:%S")

# Set Tesseract OCR path (for Colab, it's already installed)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Function to extract timestamp from the frame
def extract_time_from_frame(frame):
    """Extracts timestamp from the frame using OCR."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    x, y, w, h = (335, 38, 276, 57)  # Adjust coordinates based on timestamp position
    roi = gray[y:y+h, x:x+w]  

    text = pytesseract.image_to_string(roi, config='--psm 6').strip()
    
    try:
        entry_time = datetime.strptime(text, "%H:%M:%S")  # Adjust format if needed
        return entry_time
    except ValueError:
        return None

person_detected = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit if video ends

    # Detect objects in the frame
    results = model(frame)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            if class_id == 0:  # Class 0 = 'person' in YOLO
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, "Person", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Extract timestamp from the locked frame
                entry_time = extract_time_from_frame(frame)
                
                if entry_time:
                    status = "✅ ON TIME" if entry_time < CHECK_TIME else "❌ LATE"
                    cv2.putText(frame, f"Detected at {entry_time.strftime('%H:%M:%S')} - {status}",
                                (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    print(f"Person detected at {entry_time.strftime('%H:%M:%S')} - {status}")
                    
                    # Save the detected frame
                    cv2.imwrite("detected_entry.jpg", frame)
                    
                    person_detected = True
                else:
                    print("❌ Time could not be extracted from frame.")

                break  # Stop detecting once we find the first person

    # Show the video with bounding boxes
    # cv2.imshow("Object Detection", frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break  # Exit on pressing 'q'

    if person_detected:
        break  # Stop processing after detecting a person

cap.release()
cv2.destroyAllWindows()
print("Processing complete. Check 'detected_entry.jpg' for the saved frame.")
