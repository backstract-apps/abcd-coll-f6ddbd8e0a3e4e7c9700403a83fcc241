from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - abcd-coll-f6ddbd8e0a3e4e7c9700403a83fcc241',debug=False,docs_url='/heuristic-davinci-3eeb9cd0a03111efa6050242ac12000399/docs',openapi_url='/heuristic-davinci-3eeb9cd0a03111efa6050242ac12000399/openapi.json')

app.include_router(router, prefix='/heuristic-davinci-3eeb9cd0a03111efa6050242ac12000399/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()