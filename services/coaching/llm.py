from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):

        prompt = f"""
        You are an AI gym coach.

        Event: {event}
        Issue: {issue}

        Give short motivational feedback.
        """

        try:
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=60
            )

            print("GROQ RESPONSE:", response)

            text = response.choices[0].message.content

            print("LLM TEXT:", text)

            return text

        except Exception as e:
            print("FULL GROQ ERROR:", str(e))
            return f"ERROR: {str(e)}"
