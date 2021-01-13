from email.policy import default
from sqlalchemy import Column, Integer

from database import Base


class ViewsCount(Base):
    __tablename__ = "views_count"
    id = Column(Integer, primary_key=True)
    count = Column(Integer, default=0)

    def __init__(self):
        self.count = 0

    def __repr__(self):
        return f"<ViewsCount: {self.count}>"
