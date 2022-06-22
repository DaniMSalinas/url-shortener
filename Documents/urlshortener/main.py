from fastapi import FastAPI, Form
from starlette.requests import Request
from database import database as dbconnection, Url
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from changebase64 import change2base64

app = FastAPI(title="prueba TIER",
				description="probar a montar una API",
				version='0.0.1')

@app.on_event('startup')
def startup():
    if dbconnection.is_closed():
        dbconnection.connect()
    dbconnection.create_tables([Url])

@app.on_event('shutdown')
def shutdown():
    if dbconnection.is_open():
        dbconnection.close()

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):    
	return templates.TemplateResponse("index.html", {"request": request})

@app.post('/submit')
async def submit(urlinput: str = Form(...)):
    url = Url.create(
        full_url = urlinput,
        short_url = change2base64(urlinput)
    )
    return url

templates = Jinja2Templates(directory="templates")