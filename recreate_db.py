from database import Base, engine
from models import Message

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("Tables recreated successfully!")
