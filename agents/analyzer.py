from agents.gemini_client import client
from agents.utils import handle_gemini_error


def analyze_paper(title, summary):

    if not title or not summary:
        return "⚠️ Invalid paper data."

    prompt = f"""
You are an expert research paper analyzer.

Analyze this paper and return the answer in Markdown.

Paper Title:
{title}

Paper Abstract:
{summary}

Return the following sections:

# Problem Statement

# Methodology

# Key Contributions

# Strengths

# Limitations

# Future Work
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return handle_gemini_error(e)