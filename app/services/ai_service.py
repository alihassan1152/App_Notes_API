import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

OMNIROUTE_KEY = os.getenv("OMNIROUTE_KEY")
OMNIROUTE_URL = os.getenv("OMNIROUTE_URL")

client = AsyncOpenAI(
    base_url=OMNIROUTE_URL,
    api_key=OMNIROUTE_KEY
)

async def generate_summary(content):
    response = await client.chat.completions.create(
        model="combo/free-fallback",
        messages=[
            {"role": "user", "content": f"is note ka 2-3 line main summary banao:\n\n{content}"}
            ]
    )
    return response.choices[0].message.content


async def ask_about_notes(notes, question):
    notes_text = ""
    for note in notes:
        notes_text += note["content"] + "\n"
    response = await client.chat.completions.create(
        model="combo/free-fallback",
        messages=[
            {
                "role": "user", "content": f"ye user ke notes hain:\n{notes_text} sirf in notes ki bunyad par is sawal ka jawab do:{question}"
            }
        ]
    )
    return response.choices[0].message.content