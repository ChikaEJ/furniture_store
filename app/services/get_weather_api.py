import httpx

async def get_weather_api():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url="https://weatherapi-com.p.rapidapi.com/current.json",
            headers={
                "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
            },
            params={
                "q": "53.1%2C-0.13"
            }
        )
        return response.json()