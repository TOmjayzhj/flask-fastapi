from fastapi import FastAPI
import uvicorn
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM

from api.book import api_book
from api.author import api_author
from api.putout import api_putout
app = FastAPI()
#绑定TORTOISE_ORM
register_tortoise(
    app=app,
    config=TORTOISE_ORM
)

app.mount("/upimg", StaticFiles(directory="upimg"), name="upimg")

templates = Jinja2Templates(directory="templates")
app.include_router(api_book, prefix="/book",tags=["book"])
app.include_router(api_author, prefix="/author",tags=["author"])
app.include_router(api_putout,prefix="/putout",tags=["putout"])



@app.get('/')
async def root():
    return {'message':'Hello World'}

@app.get('/get')
def get_test():
    return {"method":"get"}

@app.post('/post')
def post_test():
    return {"method":"get"}

@app.put('/put')
def put_test():
    return {"method":"post"}

@app.delete('/delete')
def delete_test():
    return {"method":"delete"}
@app.get('/gettest')
async def get_test(request: Request):
    gettest = request.query_params
    print(gettest)
    return {'message' : 'get test'}

@app.post("/posttest")
async def post_test(request: Request):
    posttest = await request.json()
    print(posttest)
    return {"message" : "posttest"}

@app.get('/jinja2tem')
async def jinji2tem(request: Request):
    return templates.TemplateResponse('index.html',{'request':request, "books":["平凡的世界","活着","兄弟","文城"]})

if __name__ == '__main__':
    uvicorn.run( "first:app", host="127.0.0.1", port=8080, reload=True)