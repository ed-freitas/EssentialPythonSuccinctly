# models/customer.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    
    projects = relationship('Project', back_populates='customer', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, email={self.email})>"
