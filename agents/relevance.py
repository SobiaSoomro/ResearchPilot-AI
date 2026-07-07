from google import genai
from google.genai.errors import ClientError
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def is_relevant(topic, title, summary):

    prompt = f"""
You are a research paper relevance evaluator.

Research Topic:
{topic}

Paper Title:
{title}

Paper Abstract:
{summary}

Determine whether this paper is relevant to the research topic.

Return ONLY one word:

YES

or

NO
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        answer = response.text.strip().upper()

        if "YES" in answer:
            return "YES"

        return "NO"

    except ClientError as e:

        if e.status_code == 429:
            # Free quota exhausted
            return "NO"

        return "NO"

    except Exception:
        return "NO"