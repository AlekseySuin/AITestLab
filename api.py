from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

from transformers import pipeline
model = "blanchefort/rubert-base-cased-sentiment"
classifier = pipeline("sentiment-analysis", model)
list = classifier("Я доволен инженерией машинного обучения!")
list = list[0]

class Item(BaseModel):
 text : str

@app.get("/")
async def root():
 return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
 list = classifier(item.text)
 list = list[0]
 return list['label']