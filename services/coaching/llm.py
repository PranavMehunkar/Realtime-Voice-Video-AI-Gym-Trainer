from groq import Groq
import traceback

class LLMCoach:
    def __init__(self, client):
        self.client = client

        self.system_prompt = """
        You are a professional AI gym trainer.
        Give short, motivational, human-like workout coaching feedback.
        Keep responses under 2 sentences.
        """

    def give_feedback(self, event, issue):

        prompt = f"""
        Event: {event}
        Issue: {issue}

        Give coaching feedback.
        """

        try:
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",
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
                temperature=0.7,
                max_tokens=60
            )

            return response.choices[0].message.content

        except Exception as e:
            traceback.print_exc()

            return "Keep going! Focus on proper form and breathing."
