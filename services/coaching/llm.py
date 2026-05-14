from groq import APIConnectionError

class LLMCoach:
    def __init__(self, client):
        self.client = client

    def give_feedback(self, event, issue):

        prompt = f"""
        Workout Event: {event}
        Issue: {issue}

        Give short motivating gym feedback.
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
                max_tokens=50
            )

            return response.choices[0].message.content

        except APIConnectionError as e:
            print("GROQ CONNECTION ERROR:", e)
            return "Great work! Stay focused and keep your posture correct."

        except Exception as e:
            print("GROQ GENERAL ERROR:", e)
            return "Keep pushing! You're doing well."
