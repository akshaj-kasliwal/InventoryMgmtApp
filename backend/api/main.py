# backend/api/main.py

from fastapi import FastAPI, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from backend.config.dependencies import get_db
from backend.services.query import get_item_balance

app = FastAPI()

templates = Jinja2Templates(directory="frontend/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/inventory/{item_id}/balance")
def inventory_balance(item_id: int, db: Session = Depends(get_db)):
    balance = get_item_balance(db, item_id)
    if balance is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "balance": balance}

# Additional routing and app setup logic as needed.
