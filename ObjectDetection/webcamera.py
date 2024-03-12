import cv2

def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame is read correctly
        if not ret:
            print("Error: Could not read frame")
            break

        # Display the frame
        cv2.imshow("Webcam Feed", frame)

        # Check for the 'q' key to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()