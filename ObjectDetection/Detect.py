from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('best.pt')
# #model.predict(source='egg.jpg',imgsz=640,conf=0.6,save=True)

# model.predict(source=0,imgsz=640,conf=0.6,save=True)
result = model.predict(source="0",show=True)


# import cv2

# # Open the webcam
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Display the frame
#     cv2.imshow('Webcam', frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# cap.release()
# cv2.destroyAllWindows()



