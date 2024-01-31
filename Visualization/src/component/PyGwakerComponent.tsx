import React, { useState, useEffect } from 'react';

const PyGwakerComponent = () => {
  const [pygData, setPygData] = useState(null);

  useEffect(() => {
    // Make a GET request to your Flask API endpoint
    fetch('https://localhost:5000/get_pyg_data')
      .then((response) => response.json())
      .then((data) => {
        setPygData(data); // Set the fetched data to the state
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  // Render the data once it's available
  return (
    <div>
      {pygData ? (
        <div>
          {/* Render the data as needed */}
          <p>{pygData}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default PyGwakerComponent;
