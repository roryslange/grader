from fastapi import APIRouter

model_controller = APIRouter(prefix="/model", tags=["model"])

@model_controller.get("/")
def hello():
    return {'hello', "rory"}