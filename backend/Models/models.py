# backend/Models/models.py

from sqlalchemy import create_engine, Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, nullable=False)
    quantity = Column(Float, nullable=False)
    date_production_start = Column(Date)
    date_received_into_inventory = Column(Date)
    date_shipped_from_inventory = Column(Date)

# Set up the database engine and session factory
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')
Session = sessionmaker(bind=engine)

# To create tables
Base.metadata.create_all(engine)
