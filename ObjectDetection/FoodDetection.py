from flask import Flask, request, jsonify
from ultralytics import YOLO

app = Flask(__name__)

# Load the YOLO model
#model = YOLO('best.pt')
model = YOLO(r'D:\Python\ObjectDetection\best.pt')

@app.route('/detect_objects', methods=['POST'])
def detect_objects():
    # Receive image data from the request
    image_data = request.files['image']

    # Perform object detection
    results = model.predict(image_data, show=False)

    # Format the results as needed
    # For example, you can return JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)



