from agents.gemini_client import client
from agents.utils import handle_gemini_error


def generate_literature_review(plan, analyses, gap):

    if not plan:
        return "⚠️ Please generate a research plan first."

    if not analyses:
        return "⚠️ Please analyze at least one research paper."

    if not gap:
        return "⚠️ Please generate research gaps first."

    prompt = f"""
You are an expert academic research writer.

Using the following information:

Research Plan:
{plan}

Paper Analyses:
{analyses}

Research Gap:
{gap}

Write a professional literature review.

Return the answer in Markdown.

Use the following structure:

# Introduction

# Related Work

# Current Research Trends

# Research Gap

# Future Directions

# Conclusion
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return handle_gemini_error(e)