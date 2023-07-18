from fastapi import FastAPI, HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from lmqg import TransformersQG
import en_core_web_sm


class Item(BaseModel):
    context: str


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def home():
    return {"<b> It's works </b>"}


@app.post("/generation/")
def generation(data: Item):

    error=""

    if len(data.context)<512:

        try:
            nlp = en_core_web_sm.load()
            token =""
            model="lmqg/t5-small-squad-qg-ae"
            language="en"
            model = TransformersQG(language=language, model=model)
            question_answer = model.generate_qa(data.context)
        except Exception as e:
            error = str(e)
            raise HTTPException(status_code=500, detail=error)
    else:
        error="exceed length 512 characters"
        raise HTTPException(status_code=500, detail=error)

    
    return question_answer


