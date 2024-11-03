# models/project.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    
    customer = relationship('Customer', back_populates='projects')

    def __repr__(self):
        return f"<Project(id={self.id}, title={self.title}, customer_id={self.customer_id})>"
