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

            print("GROQ RESPONSE:", response)

            return response.choices[0].message.content

        except Exception as e:
            import traceback

            print("FULL GROQ ERROR:")
            traceback.print_exc()

            return f"ERROR: {str(e)}"
