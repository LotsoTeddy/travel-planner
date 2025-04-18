import httpx


async def call_agent(url, payload):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, timeout=600.0)
        response.raise_for_status()
        return response.json()
