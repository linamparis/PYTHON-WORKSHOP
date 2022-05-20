from fastapi import FastAPI
from app.controllers import school_controller

app=FastAPI(title='fastAPI self training', version='1.0.0', root_path='')

app.include_router(school_controller.router)
