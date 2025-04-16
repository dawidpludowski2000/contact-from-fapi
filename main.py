from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

@app.post("/contact/")
async def submit_contact(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # Tu byłoby zapisanie do bazy danych - na razie tylko print
    print(f"New contact: {name} ({email}): {message}")
    return {"status": "ok", "message": "Message received!"}
