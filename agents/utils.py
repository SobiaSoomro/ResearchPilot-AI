def handle_gemini_error(e):

    error = str(e)

    if "429" in error or "RESOURCE_EXHAUSTED" in error:

        return """
## ⚠️ Gemini API Quota Exceeded

You have reached the free Gemini API request limit.

Please:

- Wait for the quota to reset.
- Use another Gemini API key.
- Upgrade your Gemini API plan.
"""

    return f"""
## ❌ Gemini API Error

{error}
"""