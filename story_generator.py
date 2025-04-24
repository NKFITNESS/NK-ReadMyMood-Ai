import openai

# TEMP KEY – Replace with your real OpenAI API key
openai.api_key = "sk-..."  # Replace with your actual key

def generate_story(mood):
    prompts = {
        "Happy": "Write a fun, light-hearted short story that makes the reader smile.",
        "Sad": "Write a touching and emotional short story that reflects sadness or loss.",
        "Romantic": "Write a romantic story with dreamy, heartwarming emotions.",
        "Horny": "Write a sensual and steamy short romantic scene (keep it tasteful).",
        "Comfortable": "Write a cozy love story like 'To All the Boys I've Loved Before'.",
        "Thriller": "Write a suspenseful thriller with a dramatic plot twist.",
        "Dark": "Write a gritty, twisted psychological story with a haunting vibe.",
        "Motivated": "Write an inspiring story of someone overcoming obstacles.",
        "Fantasy": "Write a magical fantasy story with dragons or spells.",
        "Philosophical": "Write a deep, thought-provoking story exploring the meaning of life."
    }

    prompt = prompts.get(mood, f"Write a story based on mood: {mood}")

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=500
    )

    return response.choices[0].message.content
