from fastapi import APIRouter
from models import Publish
api_putout = APIRouter()

@api_putout.get("/")
async def getAllPublish():
    publish_obj = await Publish.all()
    #publish_obj = Publish.all()
    print(publish_obj)
    return {"message":"Hello putout"}
@api_putout.get('/get')
async def get_test():
    return {"method":"get"}

@api_putout.post('/post')
async def post_test():
    return {"method":"get"}

@api_putout.put('/put')
async def put_test():
    return {"method":"post"}

@api_putout.delete('/delete')
async def delete_test():
    return {"method":"delete"}
