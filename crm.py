from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Step 1: Database setup
# ----------------------

# Initialize the database engine for SQLite
engine = create_engine("sqlite:///crm.db")
Base = declarative_base()

# Define the Customer model
class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    
    # Establish one-to-many relationship with projects
    projects = relationship("Project", back_populates="customer", cascade="all, delete-orphan")

# Define the Project model
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    # Establish link to the customer
    customer = relationship("Customer", back_populates="projects")

# Create tables
Base.metadata.create_all(engine)

# Set up session factory for database interaction
Session = sessionmaker(bind=engine)
session = Session()

# Step 2: CRUD functions
# ----------------------

# Create a new customer
def create_customer(name, email, phone=None):
    new_customer = Customer(name=name, email=email, phone=phone)
    session.add(new_customer)
    session.commit()
    print(f"Customer '{name}' created.")

# Read all customers
def read_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"{customer.id}: {customer.name} ({customer.email}, {customer.phone})")

# Update a customer
def update_customer(customer_id, name=None, email=None, phone=None):
    customer = session.query(Customer).get(customer_id)
    if customer:
        customer.name = name if name else customer.name
        customer.email = email if email else customer.email
        customer.phone = phone if phone else customer.phone
        session.commit()
        print(f"Customer '{customer.name}' updated.")
    else:
        print("Customer not found.")

# Delete a customer
def delete_customer(customer_id):
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
        print(f"Customer '{customer.name}' deleted.")
    else:
        print("Customer not found.")

# Create a new project
def create_project(title, description, customer_id):
    customer = session.query(Customer).get(customer_id)
    if customer:
        new_project = Project(title=title, description=description, customer=customer)
        session.add(new_project)
        session.commit()
        print(f"Project '{title}' created for customer '{customer.name}'.")
    else:
        print("Customer not found.")

# Read all projects for a customer
def read_projects(customer_id):
    customer = session.query(Customer).get(customer_id)
    if customer:
        for project in customer.projects:
            print(f"{project.id}: {project.title} ({project.description})")
    else:
        print("Customer not found.")

# Update a project
def update_project(project_id, title=None, description=None):
    project = session.query(Project).get(project_id)
    if project:
        project.title = title if title else project.title
        project.description = description if description else project.description
        session.commit()
        print(f"Project '{project.title}' updated.")
    else:
        print("Project not found.")

# Delete a project
def delete_project(project_id):
    project = session.query(Project).get(project_id)
    if project:
        session.delete(project)
        session.commit()
        print(f"Project '{project.title}' deleted.")
    else:
        print("Project not found.")

# Step 3: User Interface
# ----------------------

def main():
    while True:
        print("\n--- CRM System ---")
        print("1. Create Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Create Project")
        print("6. View Projects for Customer")
        print("7. Update Project")
        print("8. Delete Project")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone (optional): ")
            create_customer(name, email, phone)
        elif choice == "2":
            read_customers()
        elif choice == "3":
            customer_id = int(input("Enter customer ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            update_customer(customer_id, name, email, phone)
        elif choice == "4":
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)
        elif choice == "5":
            customer_id = int(input("Enter customer ID for new project: "))
            title = input("Enter project title: ")
            description = input("Enter project description (optional): ")
            create_project(title, description, customer_id)
        elif choice == "6":
            customer_id = int(input("Enter customer ID to view projects: "))
            read_projects(customer_id)
        elif choice == "7":
            project_id = int(input("Enter project ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            update_project(project_id, title, description)
        elif choice == "8":
            project_id = int(input("Enter project ID to delete: "))
            delete_project(project_id)
        elif choice == "9":
            print("Exiting CRM System.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()