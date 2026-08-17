### Where does data live in a FastAPI request?

### INTERVIEWER
## Write a PATCH endpoint /users/{user_id}/profile that reads a path param, a query flag 
## notify, an Authorization header, and a JSON body with name and bio. Show me how FastAPI
## knows which is which — there's no req.body here.

## solution

from fastapi import FastAPI, Header, query
from pydentic import BaseModel

app = fastAPI()

class ProfileUpdate(BaseModel):
    name: str
    bio: str

@app.patch("/users/{user_id}/profile")
async def update_profile(
    user_id: int,                        #path param — no decorator needed
    body: ProfileUpdate,                 #request body — inferred from Pydantic type
    notify: bool = Query(False),         #query string — Query() marks it explicitly
    authorization: str = Header(...),    #header — Header() marks it, ... = required
):
    # before this line runs. Bad user_id -> automatic 422, never reaches here.
    return {"user_id": user_id, "name": body.name, "notify": notify}
