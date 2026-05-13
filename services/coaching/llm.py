from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):
        messages = [
            {
                "role": "system",
                "content": "You are a motivational AI gym coach."
            },
            {
                "role": "user",
                "content": f"Workout event: {event}. Issue: {issue}"
            }
        ]

        try:
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=messages,
                temperature=0.7,
                max_tokens=60
            )

            return response.choices[0].message.content

        except Exception as e:
        print("GROQ API ERROR:", e)

        # fallback response
        if event == "workout_started":
            return "Workout started. Stay focused and keep your form correct."

        elif event == "workout_completed":
            return "Great workout session. Recovery is important too."

        return "Keep going. Maintain proper posture and breathing."
