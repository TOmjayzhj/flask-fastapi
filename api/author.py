from fastapi import APIRouter

api_author = APIRouter()

@api_author.get('/get')
async def get_test():
    return {"method":"get"}

@api_author.post('/post')
async def post_test():
    return {"method":"get"}

@api_author.put('/put')
async def put_test():
    return {"method":"post"}

@api_author.delete('/delete')
async def delete_test():
    return {"method":"delete"}
