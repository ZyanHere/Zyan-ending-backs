#Sync call blocking the event loop — inside async def

#INTERVIEWER
#This FastAPI endpoint is declared async def but the service still falls over under load. What's wrong?

# Given code — looks async, isn't really
@app.get("/users/{user_id}")
async def get_user(user_id: int):
user = requests.get(f"http://internal-api/users/{user_id}")  # BUG
return user.json()

# solution
# async def alone doesn't make anything non-blocking — it just means the function can be awaited. The 
# requests library is synchronous; calling it inside an async def still blocks the single event loop thread
# for the full duration of that HTTP call. 

import httpx
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    async with httpx.AsyncClient() as Client:
        response = await client.get(f"http://internal-api/users/{user_id}")  # non-blocking
    return response.json()