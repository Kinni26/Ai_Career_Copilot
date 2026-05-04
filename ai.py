

import os
import json
import re
import requests
from dotenv import load_dotenv
load_dotenv()


def analyze_resume(resume_text, user_goal):
    api_key = os.getenv("MISTRAL_API_KEY")
    
    prompt = f"""You are a career coach and technical recruiter. Analyze the following resume and provide structured feedback.

Resume:
{resume_text}

User's Goal: {user_goal}

Return ONLY a valid JSON object (no markdown, no extra text) with exactly this structure:
{{
    "skills": ["list of skills found in resume"],
    "missing_skills": ["list of important skills missing for the goal"],
    "roadmap": ["list of actionable steps to achieve the goal"],
    "interview_questions": ["list of likely interview questions based on profile and goal"]
}}"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-large-latest",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers,
        json=payload
    )

    response.raise_for_status()
    raw = response.json()["choices"][0]["message"]["content"].strip()

    # Strip markdown code fences if present
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    return json.loads(raw)