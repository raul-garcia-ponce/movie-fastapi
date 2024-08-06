from fastapi import FastAPI, Body, Path, Query, Depends
from fastapi.responses import HTMLResponse
from bd.database import  engine, Base
from routers.movieroutes import routerMovie #Routes related to Movies
from routers.usersroutes import routerLogin #Routes related to Login


app = FastAPI(
    title='Aprendiendo FastAPI',
    description='Una API en los primeros pasos',
    version='0.0.1'
)

app.include_router(routerLogin) #Include routes related to Login
app.include_router(routerMovie) #Include routes related to Movies

Base.metadata.create_all(bind=engine)

# @app.get('/', tags=['Inicio'])
# def read_root():
#     return HTMLResponse('<h2> Hola Mundo Cruel </h2>')




