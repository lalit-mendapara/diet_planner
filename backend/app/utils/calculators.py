from app.models.diet_schema import UserSurvey


def calculate_targets(user: UserSurvey):
    # Mifflin-St Jeor Equation
    if user.gender.lower() == "male":
        bmr = (10 * user.weight) + (6.25 * user.height) - (5 * user.age) + 5
    else:
        bmr = (10 * user.weight) + (6.25 * user.height) - (5 * user.age) - 161

    # Activity Multipliers
    multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }
    tdee = bmr * multipliers.get(user.activity_level, 1.2)

    # Goal Adjustments
    if user.goal == "Build Muscle":
        calories = tdee + 300
    elif user.goal == "Lose Weight":
        calories = tdee - 500
    else:
        calories = tdee
        
    return int(calories)