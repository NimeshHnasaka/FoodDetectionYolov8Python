
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


import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [image, setImage] = useState(null);

    const handleFileChange = async (event) => {
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await axios.post('http://127.0.0.1:5000/detect', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });

            setImage(response.data);
        } catch (error) {
            console.error('Error detecting objects:', error);
        }
    };

    return (
        <div>
            <input type="file" accept="image/*" onChange={handleFileChange} />
            {image && (
                <div>
                    {image.map((result, index) => (
                        <div key={index}>
                            <p>Class: {result.class_name}</p>
                            <p>Confidence: {result.confidence}</p>
                            <p>Bbox: {result.bbox.join(', ')}</p>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default App;