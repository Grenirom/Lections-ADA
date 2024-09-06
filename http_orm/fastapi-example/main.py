from fastapi import FastAPI


app = FastAPI()


@app.get('/test-get-request')
def get_request():
    return {"message": "hello world"}


@app.post('/create')
def create():
    return {"message": "created"}

@app.delete('/delete')
def delete():
    return {"message": "deleted"}
