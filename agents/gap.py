from agents.gemini_client import client
from agents.utils import handle_gemini_error


def generate_research_gap(analyses):

    if not analyses:
        return "⚠️ Please analyze at least one paper before generating research gaps."

    prompt = f"""
You are an expert Research Gap Detection Agent.

Based on the following research paper analyses:

{analyses}

Identify the following in Markdown format:

# Research Gaps

# Unexplored Areas

# Future Research Opportunities

# Suggested Research Topics

Provide clear bullet points under each heading.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return handle_gemini_error(e)