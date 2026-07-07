from agents.gemini_client import client
from agents.utils import handle_gemini_error


def compare_papers(papers):

    if not papers:
        return "⚠️ No papers selected for comparison."

    prompt = f"""
You are an expert research comparison agent.

Compare the following research papers.

{papers}

Return the answer in Markdown.

Create a comparison table with these columns:

| Feature | Paper 1 | Paper 2 | Paper 3 |

Include:

- Problem Statement
- Methodology
- Dataset
- Key Contributions
- Strengths
- Limitations

After the table write:

## Overall Comparison

## Best Paper

## Final Recommendation
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return handle_gemini_error(e)