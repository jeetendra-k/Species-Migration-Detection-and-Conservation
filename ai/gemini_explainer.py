
import google.generativeai as genai

genai.configure(api_key="AIzaSyDyuGFmvqzCHYJmLE-FDyz4kz-2GM7rhCc")

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def generate_detailed_explanation(temp, rain, ndvi):
    try:
        prompt = f"""
You are a wildlife ecologist analyzing elephant migration in India.

Conditions:
Temperature: {temp}
Rainfall: {rain}
NDVI: {ndvi}
Population: 1500

Write a detailed scientific explanation (~150–200 lines) covering:
- migration reasons
- habitat constraints
- ecological impact
- climate influence
"""

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"LLM Error: {str(e)}"