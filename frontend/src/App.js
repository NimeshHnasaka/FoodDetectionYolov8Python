// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// function App() {
//   const [detectedItems, setDetectedItems] = useState([]);

//   useEffect(() => {
//     fetchDetectedItems();
//   }, []);

//   const fetchDetectedItems = async () => {
//     try {
//       const response = await axios.post('http://localhost:5000/detected-items', {
//         detected_items: ["Apple", "Banana", "Orange"] // Replace with actual detected items
//       });
//       console.log(response.data.message);
//     } catch (error) {
//       console.error('Error:', error);
//     }
//   };

//   return (
//     <div>
//       <h1>Detected Items</h1>
//       <ul>
//         {detectedItems.map((item, index) => (
//           <li key={index}>{item}</li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default App;

import React, { useState } from "react";
const Cam = () => {
return (
  <div>
   <img
    src="http://localhost:5000/video_feed"
    alt="Video"
   />
  </div>
 );
};
export default Cam;