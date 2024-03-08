import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO

class YOLOGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLOv8 Object Detection")
        
        # Initialize YOLO model
        self.model = YOLO(r'D:\Python\ObjectDetection\best.pt')  # Use raw string literal
        
        # Frame for displaying image
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        # Buttons
        self.select_image_btn = tk.Button(self.frame, text="Select Image", command=self.select_image)
        self.select_image_btn.grid(row=0, column=0, padx=5, pady=5)
        self.detect_btn = tk.Button(self.frame, text="Detect Objects", command=self.detect_objects)
        self.detect_btn.grid(row=0, column=1, padx=5, pady=5)
        
        # Canvas for displaying image
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()
        
    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if self.image_path:
            self.display_image()
    
    def display_image(self):
        self.img = Image.open(self.image_path)
        self.img.thumbnail((400, 300))
        self.img_tk = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
    
    def detect_objects(self):
        if hasattr(self, 'image_path'):
            result = self.model.predict(source=self.image_path, show=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = YOLOGUI(root)
    root.mainloop()