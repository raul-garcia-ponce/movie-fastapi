from fastapi import FastAPI, Body, Path, Query, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from Models.UserModel import User
from Security.user_jwt import createToken, validateToken, BearerJWT
from Models.MovieModel import Movie
from bd.database import Session, engine, Base
from Models.movie import Movie as ModelMovie
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

routerMovie = APIRouter()


@routerMovie.get('/movies', tags=['Movies'], dependencies=[Depends(BearerJWT())])
def get_movies():
    db = Session()
    data = db.query(ModelMovie).all()
    return JSONResponse(content=jsonable_encoder(data))


@routerMovie.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int = Path(ge=1, le=100)):  #validamos el parametro recibido en el URL
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'Recurso no encontrado'})
    return JSONResponse(status_code=200, content= jsonable_encoder(data))

@routerMovie.get('/movies/',tags=['Movies'])
def get_movies_by_category(category: str = Query(min_length=3, max_length=100)):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.category == category).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(data))


@routerMovie.post('/movies', tags=['Movies'])
def create_movie(movie: Movie):
    db = Session()
    newMovie = ModelMovie(**movie.dict())
    db.add(newMovie)
    db.commit()
    return JSONResponse(content={'message': 'Se ha cargado la pelicula', 'movie': newMovie})


@routerMovie.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: Movie):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()

    if not data:
        return JSONResponse(status_code=404, content={'Message': 'No se encontro el recurso'})
    
    data.title = movie.title
    data.overview = movie.overview
    data.year = movie.year
    data.rating = movie.rating
    data.category = movie.category
    
    db.commit()
    
    return JSONResponse(status_code=200, content={'message': 'Se ha MODIFICADO la pelicula'})


@routerMovie.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
        db = Session()
        data = db.query(ModelMovie).filter(ModelMovie.id == id).first()

        if not data:
            return JSONResponse(status_code=404, content={'Message': 'No se encontro el recurso'})
        
        db.delete(data)
        db.commit()
    
        return JSONResponse(content={'message': 'Se ha ELIMINADO la pelicula'})
