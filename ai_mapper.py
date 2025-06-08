from config import GROQ_API_KEY, GROQ_MODEL
import openai
import json

# Setup Groq client
client = openai.OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def map_labels_to_values(template_labels, source_data):
    # Create a summarized CSV snippet from source files
    csv_summary = "\n\n".join([
        f"Source File {i+1}:\n{df.head(20).to_csv(index=False)}"
        for i, df in enumerate(source_data)
    ])
    labels_text = "\n".join(f"- {label}" for label in template_labels)

    prompt = f"""
You are a financial data extraction AI.

You are given a list of labels from an Excel financial template and CSV source data. 
Your task is to extract numeric values from the source data that correspond to each label.

Instructions:
- Match each label (e.g., "◦ Registered nurses") to the most relevant numeric value in the source data.
- Use semantic understanding to find closest matches — even if wording differs.
- Respond with a JSON object that only includes labels for which data was found.
- If no good match is found for a label, do not include it in the output.
- Return only JSON and no explanation.

Labels:
{labels_text}

Source data (sampled rows from CSVs):
{csv_summary}

Output format:
{{
  "◦ Registered nurses": 123456.78,
  "◦ Enrolled nurses (registered with the NMBA)": 23456.90
}}
"""

    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        content = response.choices[0].message.content.strip()

        # DEBUG: raw model output
        print("\n🧠 Raw model output:\n", content)

        mapped_data = json.loads(content)
        if isinstance(mapped_data, dict):
            return mapped_data
        else:
            raise ValueError("Parsed JSON is not a dictionary.")

    except Exception as e:
        print("🚨 Error in Groq response:", e)
        return {}
