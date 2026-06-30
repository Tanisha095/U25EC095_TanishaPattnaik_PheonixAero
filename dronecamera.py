import cv2
import numpy as np

camera = cv2.VideoCapture(0) # webcam 

while True:
    success, frame = camera.read()

    if not success:  #if error occurs stop camera
        print("Couldn't access camera")
        break

    blue, green, red = cv2.split(frame)     # Split BGR channels

    red_mask = (red > 150) & (green < 100) & (blue < 100)     # Create a mask for red: Red should be high, Blue & Green should be low

    red_mask = red_mask.astype(np.uint8) * 255      # Convert boolean mask to uint8 image

    red_mask = cv2.GaussianBlur(red_mask, (5, 5), 0)       # Bluring

    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)      # Find contours

    object_found = False

    if contours:
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > 500:
            (x, y), radius = cv2.minEnclosingCircle(largest)

            if radius > 10:
                object_found = True

                # Draw circle
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)

                cv2.putText(frame, "Object Detected", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if not object_found:
        cv2.putText(frame, "Object Lost", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Drone Camera (BGR Detection)", frame)
    cv2.imshow("Red Mask", red_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()