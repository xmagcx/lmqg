from fastapi import FastAPI, HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from lmqg import TransformersQG
#import es_core_news_sm
import en_core_web_sm
#import time
#start_time = time.time()


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
            #context = "William Turner was an English painter who specialised in watercolour landscapes. He is often known as William Turner of Oxford or just Turner of Oxford to distinguish him from his contemporary, J. M. W. Turner. Many of Turner's paintings depicted the countryside around Oxford. One of his best known pictures is a view of the city of Oxford from Hinksey Hill."
            #context ="THIS IS A LEGEND told and retold among the people of Argentina about powerful friendship between a girl and the puma.Five hundred years ago when the Spanish entered South America, Native American tribes often fought back against the invaders. One way tribes could put pressure on the Spanish was to surround their settlements. This is what happened in the early 1500's when Maldonado, a Spanish girl, was 15 years old.Hostile Native Americans of the Querandí tribe had encircled the Spanish settlement where Maldonado lived."
            question_answer = model.generate_qa(data.context)
        except Exception as e:
            error = str(e)
            raise HTTPException(status_code=500, detail=error)
    else:
        error="exceed length 512 characters"
        raise HTTPException(status_code=500, detail=error)

    
    return question_answer




#print("--- %s seconds ---" % (time.time() - start_time))
##nlp = es_core_news_sm.load()
#
#model = TransformersQG(language='es', model='lmqg/t5-large-squad-qg-ae')
#context = """
#Un asno y un caballo vivían juntos desde su más tierna infancia y, como buenos amigos que eran, utilizaban el mismo establo, compartían la bandeja de heno, y se repartían el trabajo equitativamente. Su dueño era molinero, así que su tarea diaria consistía en transportar la harina de trigo desde el campo al mercado principal de la ciudad.La rutina era la misma todas las mañanas: el hombre colocaba un enorme y pesado saco sobre el lomo del asno, y minutos después, otro igual de enorme y pesado sobre su lomo
#"""
#question_answer = model.generate_qa(context)
#print(question_answer)