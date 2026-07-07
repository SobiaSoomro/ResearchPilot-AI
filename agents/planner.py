from agents.gemini_client import client
from agents.utils import handle_gemini_error


def research_planner(topic):

    if not topic.strip():
        return "⚠️ Please enter a research topic."

    prompt = f"""
You are an expert Research Planning Agent.

Research Topic:
{topic}

Generate the following in Markdown format:

# Research Objective

# Important Keywords

# Research Questions

# Search Queries

# Important Subtopics

Provide clear bullet points and well-structured headings.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return handle_gemini_error(e)