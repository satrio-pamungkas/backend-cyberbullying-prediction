from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from prediction import get_prediction
import uvicorn
import os

load_dotenv()
port = int(os.environ["PORT"])

app = FastAPI()

class Item(BaseModel):
    text: str


@app.get("/dokumentasi")
async def docs_redirect():
    return RedirectResponse(url='/docs')


@app.post("/prediksi") 
async def run_predict(item: Item):
    result = get_prediction(item.text)
    return {"prediksi": result}
    

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)