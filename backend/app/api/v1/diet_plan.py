from fastapi import APIRouter
from app.models.diet_schema import UserSurvey, DietPlanResponse
from app.services.nutrition_service import generate_diet_plan

router = APIRouter()

@router.post("/generate-plan", response_model=DietPlanResponse)
async def create_plan(survey: UserSurvey):
    plan = generate_diet_plan(survey)
    return plan