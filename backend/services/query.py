# backend/services/query.py

from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.Models.models import InventoryTransaction

def get_item_balance(db_session, item_id):
    # Aggregate the quantity for the given item_id
    balance = db_session.query(func.sum(InventoryTransaction.quantity)).filter(InventoryTransaction.item_id == item_id).scalar()
    return balance

# Example usage:
# session = Session()
# balance = get_item_balance(session, item_id)
