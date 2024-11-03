# crud_operations.py

from models.customer import Customer
from models.project import Project
from database import SessionLocal

# Create a new customer
def create_customer(name, email, phone=None):
    session = SessionLocal()
    new_customer = Customer(name=name, email=email, phone=phone)
    session.add(new_customer)
    session.commit()
    session.close()
    return new_customer

# Get all customers
def get_customers():
    session = SessionLocal()
    customers = session.query(Customer).all()
    session.close()
    return customers

# Update a customer's information
def update_customer(customer_id, name=None, email=None, phone=None):
    session = SessionLocal()
    customer = session.query(Customer).get(customer_id)
    if customer:
        customer.name = name if name else customer.name
        customer.email = email if email else customer.email
        customer.phone = phone if phone else customer.phone
        session.commit()
    session.close()

# Delete a customer
def delete_customer(customer_id):
    session = SessionLocal()
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
    session.close()

# Create a new project for a customer
def create_project(title, description, customer_id):
    session = SessionLocal()
    new_project = Project(title=title, description=description, customer_id=customer_id)
    session.add(new_project)
    session.commit()
    session.close()
    return new_project

# Get all projects for a specific customer
def get_projects_by_customer(customer_id):
    session = SessionLocal()
    projects = session.query(Project).filter(Project.customer_id == customer_id).all()
    session.close()
    return projects
