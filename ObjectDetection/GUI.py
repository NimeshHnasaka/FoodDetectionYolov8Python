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








# import tkinter as tk
# import cv2
# from PIL import Image, ImageTk
# from ultralytics import YOLO
# import math

# class FoodDetectionApp(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title("Food Detection and Billing System")

#         self.canvas = tk.Canvas(self, width=640, height=480)
#         self.canvas.pack()

#         self.delay = 10

#         # Define the YOLO model without names argument
#         self.model = YOLO(r'D:\Python\ObjectDetection\best.pt')

#         self.cap = cv2.VideoCapture(0)
#         self.cap.set(3, 640)
#         self.cap.set(4, 480)

#         self.update()

#     def update(self):
#         ret, frame = self.cap.read()

#         if ret:
#             # Perform object detection using YOLO model
#             results = self.model(frame, stream=True)

#             for r in results:
#                 boxes = r.boxes

#                 for box in boxes:
#                     x1, y1, x2, y2 = map(int, box.xyxy[0])

#                     cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

#                     confidence = math.ceil((box.conf[0]*100))/100
#                     cls = int(box.cls[0])
#                     object_name = self.model.names[cls]  # Access class names from YOLO model

#                     cv2.putText(frame, object_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
#             self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

#         self.after(self.delay, self.update)

#     def destroy(self):
#         self.cap.release()
#         super().destroy()

# if __name__ == "__main__":
#     app = FoodDetectionApp()
#     app.mainloop()

import tkinter as tk
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO
import math
import cloudinary
import numpy as np

class FoodDetectionApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Food Detection and Billing System")

        self.canvas = tk.Canvas(self, width=640, height=480)
        self.canvas.pack()

        self.invoice_text = tk.Text(self, height=10, width=40)
        self.invoice_text.pack()

        self.detected_items_label = tk.Label(self, text="Detected Items:")
        self.detected_items_label.pack()

        self.detected_items_text = tk.Text(self, height=5, width=40)
        self.detected_items_text.pack()

        # Button to calculate bill
        self.calculate_bill_button = tk.Button(self, text="Calculate Bill", command=self.calculate_bill)
        self.calculate_bill_button.pack()

        self.delay = 10

        # Define the YOLO model without names argument
        self.model = YOLO(r'D:\Python\ObjectDetection\best.pt')

        self.total_bill = 0
        self.items_detected = []

        self.update()

    def update(self):
        # Generate Cloudinary URL
        image_url, options = cloudinary.utils.cloudinary_url("ewktdq1vvbxulisml4vv.jpg", secure=True)

        # Retrieve image from Cloudinary
        image = cv2.imread(image_url)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Perform object detection using YOLO model
        results = self.model(frame)

        # Display detected objects on the image
        for item in results.xyxy[0]:
            x1, y1, x2, y2 = map(int, item[:4])
            object_name = self.model.names[int(item[5])]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.putText(frame, object_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Add detected item to the list
            if object_name not in self.items_detected:
                self.items_detected.append(object_name)
                self.detected_items_text.insert(tk.END, f"{object_name}\n")

        # Convert image to Tkinter format and display on canvas
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # Schedule the next update
        self.after(self.delay, self.update)

    def get_item_price(self, item_name):
        # Function to get the price of detected items
        # This is a placeholder function, you should replace it with your own logic
        prices = {
            "Egg": 1.00,
            "Meat": 0.50,
            "Noodles": 0.75,
            # Add more items and their prices as needed
        }
        return prices.get(item_name, 0)  # Return 0 if item not found

    def update_invoice(self):
        self.invoice_text.delete('1.0', tk.END)
        self.invoice_text.insert(tk.END, "Invoice\n\n")
        for item in self.items_detected:
            self.invoice_text.insert(tk.END, f"{item}: ${self.get_item_price(item):.2f}\n")
        self.invoice_text.insert(tk.END, f"\nTotal Bill: ${self.total_bill:.2f}")

    def calculate_bill(self):
        # Calculate the bill
        self.total_bill = sum(self.get_item_price(item) for item in self.items_detected)
        self.update_invoice()

if __name__ == "__main__":
    cloudinary.config(
        cloud_name = "dhnfyb9bw",
        api_key = "377977664553313",
        api_secret = "aDFluxAwYLUgfmgQlU11oIpMmGI"
    )
    app = FoodDetectionApp()
    app.mainloop()