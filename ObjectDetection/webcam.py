

# from ultralytics import YOLO
# import cv2
# # Load a model
# model = YOLO(r'D:\Python\ObjectDetection\best.pt')  # load an official model

# result=model(source=0,show=True)
# cv2.waitKey(0)


from flask import Flask, Response
from ultralytics import YOLO
import cv2
import math

app = Flask(__name__)
cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

model = YOLO(r'D:\Python\ObjectDetection\best.pt')
classNames = ["Egg","Meat"]

@app.route('/')
def index():
    return Response(detect_objects(), mimetype='multipart/x-mixed-replace;boundary=frame')

def detect_objects(path_x=''):
    while True:
        success, img = cap.read()
        if not success:
            break

        results = model(img, stream=True)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(detect_objects(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

