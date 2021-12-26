from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from prediction import get_prediction
import uvicorn

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
    uvicorn.run("app:app", host="127.0.0.1", port=5049, reload=True)