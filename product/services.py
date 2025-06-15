from fastapi import FastAPI

product = FastAPI(prefix="/product")


@product.get("/get-item")
def get_item():
    return {"message": "GET tracked"}


@product.post("/create-item")
def create_item():
    return {"message": "POST tracked"}


@product.put("/update-item")
def update_item():
    return {"message": "PUT tracked"}


@product.delete("/delete-item")
def update_item():
    return {"message": "DELETE tracked"}
