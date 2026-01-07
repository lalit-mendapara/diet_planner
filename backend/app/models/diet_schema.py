from pydantic import BaseModel
from typing import List, Optional

class UserSurvey(BaseModel):
    weight: float
    height: float
    age: int
    gender: str  # "male" or "female"
    goal: str    # "Build Muscle", "Lose Weight", etc.
    activity_level: str
    dietary_preference: str
    allergies: List[str] = []

class Meal(BaseModel):
    meal_id: str
    label: str
    is_veg: bool
    dish_name: str
    portion_size: str
    nutrients: dict
    alternatives: List[str]

class DietPlanResponse(BaseModel):
    phase_info: dict
    user_profile: dict
    nutrition_targets: dict
    meal_plan: List[Meal]
    phase_1_guidelines: List[str]