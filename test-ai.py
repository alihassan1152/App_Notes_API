import asyncio
from app.services.ai_service import generate_summary

note = "Aaj main ne FastAPI Seekhi. Endpoints banaye GET, POST, PUT, DELETE. Mongodb se connect kiya. bahut maza aaya"

async def test():

    result = await generate_summary(note)
    print("AI KI SUMMARY:")
    print(result)


asyncio.run(test())
