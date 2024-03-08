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

#         self.invoice_text = tk.Text(self, height=10, width=40)
#         self.invoice_text.pack()

#         self.delay = 10

#         # Define the YOLO model without names argument
#         self.model = YOLO(r'D:\Python\ObjectDetection\best.pt')

#         self.cap = cv2.VideoCapture(0)
#         self.cap.set(3, 640)
#         self.cap.set(4, 480)

#         self.total_bill = 0
#         self.items_detected = []

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

#                     # Add detected item and price
#                     if object_name not in self.items_detected:
#                         self.items_detected.append(object_name)
#                         self.total_bill += self.get_item_price(object_name)

#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
#             self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

#             self.update_invoice()

#         self.after(self.delay, self.update)

#     def get_item_price(self, item_name):
#         # Function to get the price of detected items
#         # This is a placeholder function, you should replace it with your own logic
#         prices = {
#             "Egg": 1.00,
#             "Meat": 0.50,
#             "Noodles": 0.75,
#             # Add more items and their prices as needed
#         }
#         return prices.get(item_name, 0)  # Return 0 if item not found

#     def update_invoice(self):
#         self.invoice_text.delete('1.0', tk.END)
#         self.invoice_text.insert(tk.END, "Invoice\n\n")
#         for item in self.items_detected:
#             self.invoice_text.insert(tk.END, f"{item}: ${self.get_item_price(item):.2f}\n")
#         self.invoice_text.insert(tk.END, f"\nTotal Bill: ${self.total_bill:.2f}")

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

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        self.total_bill = 0
        self.items_detected = []

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

                    # Add detected item and price
                    if object_name not in self.items_detected:
                        self.items_detected.append(object_name)

                        # Update detected items text widget
                        self.detected_items_text.insert(tk.END, f"{object_name}\n")

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

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

    def destroy(self):
        self.cap.release()
        super().destroy()

if __name__ == "__main__":
    app = FoodDetectionApp()
    app.mainloop()