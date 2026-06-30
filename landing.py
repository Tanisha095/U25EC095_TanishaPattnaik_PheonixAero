import cv2
import numpy as np

image = cv2.imread("D:/vscode/MYCODE/pheonix/img.png") # Load img 

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale the  input img

_, thresh = cv2.threshold(grayscale, 200, 255, cv2.THRESH_BINARY)  # Threshold to detect white region

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours
found = False

for cnt in contours:
    # Approximate contour shape
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    if len(approx) == 4:
        found = True
        
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)    # Draw rectangle on img
        
        print("Landing")
        break

if not found:
    print("No landing pad detected")

cv2.imwrite("sahi.jpg", image)