
// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// const FoodDetectionApp = () => {
//     const [image, setImage] = useState(null);

//     useEffect(() => {
//         const fetchData = async () => {
//             const stream = await navigator.mediaDevices.getUserMedia({ video: true });
//             const video = document.createElement('video');
//             const canvas = document.createElement('canvas');
//             const ctx = canvas.getContext('2d');

//             video.srcObject = stream;
//             video.addEventListener('loadedmetadata', () => {
//                 canvas.width = video.videoWidth;
//                 canvas.height = video.videoHeight;
//             });

//             const detectObjects = async () => {
//                 ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
//                 const imageData = canvas.toDataURL('image/jpeg');
//                 const response = await axios.post('/api/detect', { image: imageData });
//                 setImage(response.data);
//                 requestAnimationFrame(detectObjects);
//             };

//             video.play();
//             requestAnimationFrame(detectObjects);
//         };

//         fetchData();

//         return () => {
//             // Clean up resources if needed
//         };
//     }, []);

//     return (
//         <div>
//             {image && <img src={image} alt="Detected Objects" />}
//         </div>
//     );
// };

// export default FoodDetectionApp;


import React, { useEffect, useRef } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

function App() {


    const webcamRef = useRef(null);

    useEffect(() => {
      const fetchImage = async () => {
        const response = await axios.get('http://127.0.0.1:5000/video_feed', {
          responseType: 'arraybuffer',
        });
        const image = Buffer.from(response.data, 'binary').toString('base64');
        const imageSrc = `data:image/jpeg;base64,${image}`;
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        const img = new Image();
        img.onload = function () {
          canvas.width = img.width;
          canvas.height = img.height;
          context.drawImage(img, 0, 0, img.width, img.height);
          context.font = '16px Arial';
          context.fillStyle = 'red';
          context.fillText('Detected Object', 10, 50); // Adjust text position as needed
          const webcamVideo = document.querySelector('video');
          webcamVideo.srcObject = canvas.captureStream();
        };
        img.src = imageSrc;
      };
  
      const intervalId = setInterval(fetchImage, 100); // Adjust the interval as needed
  
      return () => clearInterval(intervalId);
    }, []);







  return (
    <div>
        <div>
      <Webcam ref={webcamRef} />
    </div>
    </div>
  )
}

export default App



