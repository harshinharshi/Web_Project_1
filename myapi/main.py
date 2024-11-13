from fastapi import FastAPI

app = FastAPI()

fakedatabase = {
    1:{'task':'clean'},
    2:{'task':'cook'},
    3:{'task':'eat'}
}

@app.get("/")
def get_item():
    return fakedatabase

@app.get("/{id}")
def getitem(id : int):
    return fakedatabase[id]


@app.post("/post_data")
def addItem(task : str):
    key_value = max(fakedatabase.keys())+1
    fakedatabase[key_value] = {'task':task}
    return fakedatabase