from groq import Groq
import traceback

class LLMCoach:
    def __init__(self, client):
        self.client = client

        self.system_prompt = (
            "You are a motivational AI gym coach. "
            "Give short workout feedback in 1 sentence."
        )

    def give_feedback(self, event, issue=""):

        prompt = f"""
        Workout event: {event}
        Issue: {issue}

        Give short motivating feedback.
        """

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.4,
                max_tokens=60
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"API Error: {str(e)}"

        
