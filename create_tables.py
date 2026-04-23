from db import engine
from models import Base
import models
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT DATABASE();"))
    print("Connected to DB:", list(result))

Base.metadata.create_all(bind=engine)

print("Tables created successfully")