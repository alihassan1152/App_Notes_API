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
    try:
        response = await client.chat.completions.create(
            model="combo/free-fallback",
            messages=[
                {"role": "user", "content": f"is note ka 2-3 line main summary banao:\n\n{content}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Summary banane mein masla: {e}")
        return None
    

async def ask_about_notes(notes, question):
        notes_text = ""
        for note in notes:
            notes_text += note["content"] + "\n"
        try:
            response = await client.chat.completions.create(
                model="combo/free-fallback",
                messages=[
                    {"role": "user", "content": f"ye user ke notes hain:\n{notes_text} sirf in notes ki bunyad par is sawal ka jawab do:{question}"}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Sawal ka jawab daine main masla:{e}")
            return "Maaf kijiye, abhi jawab nahi de sakta. Baad mein koshish karein."



async def summarize_all_notes(notes):
        notes_text = ""
        for note in notes:
            notes_text += note["content"] + "\n"
        try:    
            response = await client.chat.completions.create(
                model="combo/free-fallback",
                messages=[
                    {"role": "user", "content": f"ye user ke sare notes hain:\n {notes_text}\n\n in sab ka aik milta julta khulasa (overall summary) banao:"}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Khulasa banane main masla:{e}")
            return "Maaf kejye abhi khulasa nahe ban sakta kuch dair bad koshish karain."

