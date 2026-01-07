import React, { useState } from 'react';
import { generateDietPlan } from '../services/api';
import SurveyForm from '../components/SurveyForm';

const Dashboard = () => {
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSurveySubmit = async (data) => {
    setLoading(true);
    try {
      const result = await generateDietPlan(data);
      setPlan(result);
    } catch (err) {
      alert("Failed to generate plan. Check console.");
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>AI is generating your custom plan...</div>;

  return (
    <div className="container">
      {!plan ? (
        <SurveyForm onSubmit={handleSurveySubmit} />
      ) : (
        <div className="plan-results">
          <h1>{plan.phase_info.phase_name}</h1>
          <p>Target Calories: {plan.nutrition_targets.daily_calories} kcal</p>
          {plan.meal_plan.map((meal) => (
            <div key={meal.meal_id} className="meal-card">
              <h3>{meal.label}: {meal.dish_name}</h3>
              <p>Portion: {meal.portion_size}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Dashboard;