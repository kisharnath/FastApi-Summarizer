from typing import Union
from typing import Annotated
from transformers import pipeline
from .resources.scrap import scrape_text
from fastapi import FastAPI ,Form

app = FastAPI()
summarizer = pipeline("summarization", model="Falconsai/text_summarization")


@app.get("/")
def read_root(name: Annotated[str, Form()], url: Annotated[str, Form()]):
    ARTICLE = scrape_text(url)
    texts = summarizer(ARTICLE, max_length=1000, min_length=30, do_sample=False)
    return {"Hello": texts}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}