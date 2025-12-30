from fastapi import FastAPI
from .controller.modelController import model_controller


app = FastAPI(name="model service")
app.include_router(model_controller)
