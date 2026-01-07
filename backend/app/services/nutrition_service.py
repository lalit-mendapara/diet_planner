import os
import json
from config import OPENROUTER_API_KEY,OPENROUTER_MODEL_NAME
from openai import OpenAI
from app.utils.calculators import calculate_targets
from fastapi import HTTPException
from app.core.llm_client import get_openrouter_client

# For Gemini implementation later:
# import google.generativeai as genai

def generate_diet_plan(user_data):
    # 1. Calculate the core nutritional math
    calories = calculate_targets(user_data)
    protein = int(user_data.weight * 2) 
    
    # 2. Setup the OpenRouter Client
    # OpenRouter requires the base_url to be changed to their endpoint
    client = get_openrouter_client()

    # 3. Define the Prompt
    prompt = f"""
SYSTEM: You are a JSON-only response engine. Do not include any analysis, thoughts, or markdown commentary.
USER: Create a Phase 1 diet plan for a {user_data.dietary_preference} individual.
Goal: {user_data.goal}
Daily Calories: {calories} kcal

REQUIRED JSON STRUCTURE (STRICT):
{{
  "phase_info": {{ "phase_number": 1, "phase_name": "Foundation", "duration_weeks": 4 }},
  "user_profile": {{ "goal": "{user_data.goal}", "dietary_preference": "{user_data.dietary_preference}", "activity_level": "{user_data.activity_level}" }},
  "nutrition_targets": {{ "daily_calories": {calories}, "macros": {{ "protein_g": {protein}, "carbs_g": 300, "fats_g": 80 }}, "hydration_liters": 3.5 }},
  "meal_plan": [
    {{ 
      "meal_id": "M1", 
      "label": "Breakfast", 
      "is_veg": true, 
      "dish_name": "example", 
      "portion_size": "example", 
      "nutrients": {{"p": 20, "c": 40, "f": 10}}, 
      "alternatives": ["alt1"] 
    }}
  ],
  "phase_1_guidelines": ["string1", "string2"]
}}
"""

    try:
        # --- OPENROUTER (Current Implementation) ---
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a professional nutritionist. Always output strictly valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" } # Ensures structured output
        )
        raw_content = response.choices[0].message.content
        data = json.loads(raw_content) # 4. Parse and return JSON

        return data

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="AI returned invalid JSON format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Error: {str(e)}")