import React, { useState } from 'react';

const SurveyForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    weight: 70, height: 175, age: 25, gender: 'male',
    goal: 'Build Muscle', activity_level: 'Moderately Active',
    dietary_preference: 'Non-Veg', allergies: []
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <form onSubmit={(e) => { e.preventDefault(); onSubmit(formData); }}>
      <h2>Personal Details</h2>
      <input name="weight" type="number" onChange={handleChange} placeholder="Weight (kg)" />
      <input name="height" type="number" onChange={handleChange} placeholder="Height (cm)" />
      <select name="goal" onChange={handleChange}>
        <option value="Build Muscle">Build Muscle</option>
        <option value="Lose Weight">Lose Weight</option>
        <option value="Just Being Fit">Just Being Fit</option>
      </select>
      <button type="submit">Generate My Plan</button>
    </form>
  );
};

export default SurveyForm;