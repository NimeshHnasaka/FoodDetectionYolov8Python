

# from ultralytics import YOLO
# import cv2
# # Load a model
# model = YOLO(r'D:\Python\ObjectDetection\best.pt')  # load an official model

# result=model(source=0,show=True)
# cv2.waitKey(0)






# from flask import Flask, render_template, Response
# from flask import jsonify
# from ultralytics import YOLO
# import cv2

# app = Flask(__name__)

# # Load YOLO model
# model = YOLO(r'D:\Python\ObjectDetection\best.pt')



# clasNames=[
#     "Egg","White-Rice","Meat"
# ]


# @app.route('/')
# def index():
#     return render_template('index.html')

# def detect_objects():
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             # Perform object detection
#             results = model(frame, show=False)
#             # Convert the image to JPEG
#             ret, jpeg = cv2.imencode('.jpg', results.render())
#             # Convert the image to bytes
#             frame_bytes = jpeg.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
#         else:
#             break
#     cap.release()

# @app.route('/video_feed')
# def video_feed():
#     return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')


#     @app.route('/webcam')
# def wedcam():
#     return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, Response
# from ultralytics import YOLO
# import cv2


# cap=cv2.VideoCapture(0)
# framewidth=int(cap.get(3))
# frame_height=int(cap.get(4))

# # app = Flask(__name__)

# # Load YOLO model
# model = YOLO(r'D:\Python\ObjectDetection\best.pt')




# clasNames=[
#     "Egg","White-Rice","Meat"
# ]




# while True:
#     success. img = cap.read()

#     results=model(img,stream=True)

#     for r in results:
#         boxes=r.boxes
#         for box in boxes:    
#             x1,y1,x2,y2=box.xyxy[0]
#             #print(x1,y1,x2,y2)
#             cv2.rectangle(img, (x1,y1),(x2,y2),(255,0,255),3)



#  cv2.waitKey(0)& 0xFF==ord('1'):
#     break


# # @app.route('/webcam')
# # def webcam():
# #    return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

#  if __name__ == '__main__':
#       app.run(debug=True)





# from ultralytics import YOLO
# import cv2
# import math
# cap=cv2.VideoCapture(0)

# frame_width=int(cap.get(3))
# frame_height = int(cap.get(4))

# out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# model=YOLO(r'D:\Python\ObjectDetection\best.pt')
# classNames = ["Egg"
#               ]
# while True:
#     success, img = cap.read()
#     # Doing detections using YOLOv8 frame by frame
#     #stream = True will use the generator and it is more efficient than normal
#     results=model(img,stream=True)
#     #Once we have the results we can check for individual bounding boxes and see how well it performs
#     # Once we have have the results we will loop through them and we will have the bouning boxes for each of the result
#     # we will loop through each of the bouning box
#     for r in results:
#         boxes=r.boxes
#         for box in boxes:
#             x1,y1,x2,y2=box.xyxy[0]
#             #print(x1, y1, x2, y2)
#             x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
#             print(x1,y1,x2,y2)
#             cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,255),3)
#             #print(box.conf[0])
#             conf=math.ceil((box.conf[0]*100))/100
#             cls=int(box.cls[0])
#             class_name=classNames[cls]
#             label=f'{class_name}{conf}'
#             t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
#             #print(t_size)
#             c2 = x1 + t_size[0], y1 - t_size[1] - 3
#             cv2.rectangle(img, (x1,y1), c2, [255,0,255], -1, cv2.LINE_AA)  # filled
#             cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)
#     out.write(img)
#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF==ord('1'):
#         break
# out.release()


from flask import Flask, Response
from ultralytics import YOLO
import cv2
import math

app = Flask(__name__)
cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

model = YOLO(r'D:\Python\ObjectDetection\best.pt')
classNames = ["Egg"]

@app.route('/')
def index():
    return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

def detect_objects():
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
    return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)