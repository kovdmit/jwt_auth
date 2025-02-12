from fastapi import FastAPI


myapp = FastAPI()


@myapp.post('/calculate')
async def root(num1: int, num2: int):
    return {'result': num1 + num2}
