# -*- coding: utf-8 -*-
# Description: Detects bodies in a live video stream from a network camera.
# Author: Pat Langlois


import cv2

# Replace with your network camera's stream URL
camera_url = "rtsp://<camera_ip>:<port>/stream"  # Example RTSP URL
# camera_url = "http://<camera_ip>:<port>/video"  # Example HTTP URL

# Load the pre-trained Haar Cascade for body detection
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Connect to the network camera
video_feed = cv2.VideoCapture(camera_url)

# Check if the connection is successful
if not video_feed.isOpened():
    print("Error: Could not open network camera feed.")
    exit()

print("Press 'q' to exit the feed.")

try:
    while True:
        # Capture a frame from the network camera
        ret, frame = video_feed.read()
        if not ret:
            print("Error: Failed to retrieve frame from network camera.")
            break

        # Resize the frame for faster processing (optional)
        frame = cv2.resize(frame, (640, 480))

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect bodies in the frame
        bodies = body_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        # Draw rectangles around detected bodies
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the frame with detections
        cv2.imshow("Body Detection - Network Camera", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nFeed interrupted.")

finally:
    # Release the video feed and close windows
    video_feed.release()
    cv2.destroyAllWindows()
    print("Feed stopped.")
