import React from 'react';

const viz_comp = ({ data }) => {
  // Example: Assuming walker data contains name, surname, age, child_name, and relation
  const { name, surname, age, child_name, relation } = data;

  return (
    <div className="visualization">
      <h2>Walker Information</h2>
      <ul>
        <li>
          <strong>Name:</strong> {name}
        </li>
        <li>
          <strong>Surname:</strong> {surname}
        </li>
        <li>
          <strong>Age:</strong> {age}
        </li>
        <li>
          <strong>Child Name:</strong> {child_name}
        </li>
        <li>
          <strong>Relation:</strong> {relation}
        </li>
        {/* Add more visualization elements based on your data */}
      </ul>
      {/* Add your custom visualization components here */}
    </div>
  );
};

export default viz_comp;
