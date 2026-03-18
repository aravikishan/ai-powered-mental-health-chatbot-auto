from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

# Database setup
DATABASE_URL = "sqlite:///./mental_health_chatbot.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    mood = Column(String)
    conversations = relationship("Conversation", back_populates="user")

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    messages = relationship("Message", back_populates="conversation")
    user = relationship("User", back_populates="conversations")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    sender = Column(String)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    conversation = relationship("Conversation", back_populates="messages")

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    link = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Seed data
def seed_data():
    db = SessionLocal()
    if not db.query(User).first():
        user = User(name="John Doe", email="john@example.com", age=30, mood="happy")
        db.add(user)
        db.commit()
        db.refresh(user)

    if not db.query(Resource).first():
        resource = Resource(title="Mental Health Support", description="A guide to mental health support.", link="https://example.com")
        db.add(resource)
        db.commit()

    db.close()

seed_data()

# FastAPI app
app = FastAPI()

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
async def chat_interface(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
async def user_profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@app.get("/resources", response_class=HTMLResponse)
async def resources_page(request: Request):
    return templates.TemplateResponse("resources.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.post("/api/chat")
async def chat_endpoint(message: str):
    # Mock response
    return {"response": "This is a mock response to your message: " + message}

@app.get("/api/resources")
async def get_resources():
    db = SessionLocal()
    resources = db.query(Resource).all()
    db.close()
    return resources

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/api/users/{user_id}")
async def update_user(user_id: int, name: str = None, email: str = None, age: int = None, mood: str = None):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")
    if name:
        user.name = name
    if email:
        user.email = email
    if age:
        user.age = age
    if mood:
        user.mood = mood
    db.commit()
    db.refresh(user)
    db.close()
    return user
