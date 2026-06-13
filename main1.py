from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()
@app.get('/dictionary/{word}')
def get_word(word:str):
    wd = httpx.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    
    data = wd.json()
    if isinstance(data, dict) and "title" in data:
        return {"error": f"'{word}' not found"}
    else:
        return data