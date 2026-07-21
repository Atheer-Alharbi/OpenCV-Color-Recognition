#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0)

# Function to detect and label colors
def detect_color(hsv, frame, lower, upper, color_name, box_color):

    # Create a mask for the selected color
    mask = cv2.inRange(hsv, lower, upper)

    # Remove noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    count = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 1000:

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)

            cv2.putText(frame,
                        color_name,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        box_color,
                        2)

            count += 1

    return count


while True:

    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    total = 0

    # -------- Red --------
    total += detect_color(
        hsv,
        frame,
        np.array([0, 120, 70]),
        np.array([10, 255, 255]),
        "Red",
        (0, 0, 255)
    )

    total += detect_color(
        hsv,
        frame,
        np.array([170, 120, 70]),
        np.array([180, 255, 255]),
        "Red",
        (0, 0, 255)
    )

    # -------- Green --------
    total += detect_color(
        hsv,
        frame,
        np.array([35, 50, 50]),
        np.array([85, 255, 255]),
        "Green",
        (0, 255, 0)
    )

    # -------- Blue --------
    total += detect_color(
        hsv,
        frame,
        np.array([90, 80, 50]),
        np.array([130, 255, 255]),
        "Blue",
        (255, 0, 0)
    )

    # -------- Yellow --------
    total += detect_color(
        hsv,
        frame,
        np.array([18, 80, 80]),
        np.array([40, 255, 255]),
        "Yellow",
        (0, 255, 255)
    )

    # -------- Orange --------
    total += detect_color(
        hsv,
        frame,
        np.array([8, 120, 120]),
        np.array([18, 255, 255]),
        "Orange",
        (0, 165, 255)
    )

    # -------- Purple --------
    total += detect_color(
        hsv,
        frame,
        np.array([130, 60, 60]),
        np.array([160, 255, 255]),
        "Purple",
        (255, 0, 255)
    )

    # Project title
    cv2.putText(frame,
                "OpenCV Color Recognition",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2)

    # Number of detected objects
    cv2.putText(frame,
                f"Detected Objects: {total}",
                (10, 65),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2)

    cv2.imshow("OpenCV Color Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




