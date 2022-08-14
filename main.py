from fastapi import Depends, FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from model import Users
import schema
from database import SessionLocal, engine
import model
from fastapi import FastAPI, Depends
app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def read_user(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(Users).all()
    return templates.TemplateResponse("index.html", {"request": request, "data": records})

@app.get("/login.html/")
def read_user(request: Request, email: schema.Users.email, password: schema.Users.password, db: Session = Depends(get_database_session)):
    item = db.query(Users).filter(Users.email == email,Users.password == password).first()
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.post("/login.html/")
async def create_user(request: Request,db: Session = Depends(get_database_session),fname: schema.Users.fname = Form(...), lname: schema.Users.lname = Form(...), email: schema.Users.email = Form(...), password: schema.Users.password = Form(...)):
    users = Users(fname=fname, lname=lname,email=email,password=password)
    db.add(users)
    db.commit()
    db.refresh(users)
    response = templates.TemplateResponse("login.html", {"request": request})
    return response 
