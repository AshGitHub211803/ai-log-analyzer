import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_logs(logs):

    prompt = f"""
    You are a senior software engineer.

    Analyze the following application logs and identify:
    1. Possible root cause
    2. Error type
    3. Suggested fixes

    Logs:
    {logs}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You analyze system logs."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error analyzing logs: {str(e)}"