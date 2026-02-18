from openai import OpenAI
import config
import json

client = OpenAI(api_key=config.OPENAI_API_KEY)

def parse_announcement(text):
    prompt = f"""
Extract acquisition/investment structured data.
Return JSON with:
Acquirer, Target, Shares, Percent, Cost, Date, Control, Related Party, Financials
If not acquisition return: {{"type":"other"}}
TEXT:
{text}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return json.loads(response.choices[0].message.content)
