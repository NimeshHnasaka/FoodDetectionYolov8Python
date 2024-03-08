# import tkinter as tk
# import cv2
# from PIL import Image, ImageTk

# class FoodDetectionApp:
#     def __init__(self, window, window_title):
#         self.window = window
#         self.window.title(window_title)

#         self.camera = cv2.VideoCapture(0)
#         _, self.frame = self.camera.read()

#         self.canvas = tk.Canvas(window, width=self.frame.shape[1], height=self.frame.shape[0])
#         self.canvas.pack()

#         self.btn_detect = tk.Button(window, text="Detect", command=self.detect_food)
#         self.btn_detect.pack(fill="both", expand=True)

#         self.lbl_result = tk.Label(window, text="")
#         self.lbl_result.pack()

#         self.delay = 10
#         self.update()

#         self.window.mainloop()

#     def detect_food(self):
#         # Food detection logic goes here
#         # Replace the following line with your actual detection algorithm
#         detected_food = "Pizza"
#         self.lbl_result.config(text=f"Detected food: {detected_food}")

#     def update(self):
#         _, self.frame = self.camera.read()
#         self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)))
#         self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
#         self.window.after(self.delay, self.update)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FoodDetectionApp(root, "Food Detection and Billing System")




# import tkinter as tk
# import cv2
# from PIL import Image, ImageTk
# from ultralytics import YOLO

# class FoodDetectionApp:
#     def __init__(self, window, window_title):
#         self.window = window
#         self.window.title(window_title)

#         self.camera = cv2.VideoCapture(0)
#         _, self.frame = self.camera.read()

#         self.canvas = tk.Canvas(window, width=self.frame.shape[1], height=self.frame.shape[0])
#         self.canvas.pack()

#         self.btn_detect = tk.Button(window, text="Detect", command=self.detect_food)
#         self.btn_detect.pack(fill="both", expand=True)

#         self.lbl_result = tk.Label(window, text="")
#         self.lbl_result.pack()

#         self.delay = 10
#         self.update()

#         self.model = YOLO(r'D:\Python\ObjectDetection\best.pt')  # Load YOLOv5 model

#         self.window.mainloop()

#     def detect_food(self):
#         # Perform food detection
#         detected_food = self.perform_food_detection(self.frame)
#         self.lbl_result.config(text=f"Detected food: {detected_food}")

#     def update(self):
#         _, self.frame = self.camera.read()
#         self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)))
#         self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
#         self.window.after(self.delay, self.update)

#     def perform_food_detection(self, frame):
#         # Convert frame to PIL image
#         pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

#         # Perform food detection using YOLOv5 model
#         results = self.model(pil_image)

#         # Extract detected food labels
#         labels = results.names
#         detected_food = ", ".join(labels)

#         return detected_food

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FoodDetectionApp(root, "Food Detection and Billing System")


# import tkinter as tk
# import cv2
# from PIL import Image, ImageTk
# from ultralytics import YOLO

# class FoodDetectionApp:
#     def __init__(self, window, window_title):
#         self.window = window
#         self.window.title(window_title)

#         self.camera = cv2.VideoCapture(0)
#         _, self.frame = self.camera.read()

#         self.canvas = tk.Canvas(window, width=self.frame.shape[1], height=self.frame.shape[0])
#         self.canvas.pack()

#         self.btn_detect = tk.Button(window, text="Detect", command=self.detect_food)
#         self.btn_detect.pack(fill="both", expand=True)

#         self.lbl_result = tk.Label(window, text="")
#         self.lbl_result.pack()

#         self.delay = 10
#         self.update()

#         self.class_names = ["Egg", "banana", "orange", "pizza", "burger", "fries", "salad", "cake", "cookie", "sandwich"]
#         self.model = YOLO(r'D:\Python\ObjectDetection\best.pt', names=self.class_names)  # Load YOLOv5 model with class names

#         self.window.mainloop()

#     def detect_food(self):
#         # Perform food detection
#         detected_food = self.perform_food_detection(self.frame)
#         self.lbl_result.config(text=f"Detected food: {detected_food}")

#     def update(self):
#         _, self.frame = self.camera.read()
#         self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)))
#         self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
#         self.window.after(self.delay, self.update)

#     def perform_food_detection(self, frame):
#         # Convert frame to PIL image
#         pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

#         # Perform food detection using YOLOv5 model
#         results = self.model(pil_image)

#         # Extract detected food labels
#         labels = results.names
#         detected_food = ", ".join(labels)

#         return detected_food

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FoodDetectionApp(root, "Food Detection and Billing System")


import tkinter as tk
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO
import math

class FoodDetectionApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Food Detection and Billing System")

        self.canvas = tk.Canvas(self, width=640, height=480)
        self.canvas.pack()

        self.delay = 10

        # Define the YOLO model without names argument
        self.model = YOLO(r'D:\Python\ObjectDetection\best.pt')

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        self.update()

    def update(self):
        ret, frame = self.cap.read()

        if ret:
            # Perform object detection using YOLO model
            results = self.model(frame, stream=True)

            for r in results:
                boxes = r.boxes

                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    confidence = math.ceil((box.conf[0]*100))/100
                    cls = int(box.cls[0])
                    object_name = self.model.names[cls]  # Access class names from YOLO model

                    cv2.putText(frame, object_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.after(self.delay, self.update)

    def destroy(self):
        self.cap.release()
        super().destroy()

if __name__ == "__main__":
    app = FoodDetectionApp()
    app.mainloop()