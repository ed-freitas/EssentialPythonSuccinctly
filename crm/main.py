# main.py

from database import init_db
from crud_operations import create_customer, get_customers, update_customer, delete_customer
from crud_operations import create_project, get_projects_by_customer

# Initialize the database
init_db()

def main_menu():
    print("Welcome to the CRM CLI App")
    print("1. Add a new customer")
    print("2. View all customers")
    print("3. Update a customer")
    print("4. Delete a customer")
    print("5. Add a project to a customer")
    print("6. View projects for a customer")
    print("0. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone (optional): ")
            create_customer(name, email, phone)
            print("Customer added successfully!")

        elif choice == "2":
            customers = get_customers()
            for customer in customers:
                print(f"{customer.id}: {customer.name} - {customer.email}")

        elif choice == "3":
            customer_id = int(input("Enter customer ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            phone = input("Enter new phone (leave blank to skip): ")
            update_customer(customer_id, name, email, phone)
            print("Customer updated successfully!")

        elif choice == "4":
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)
            print("Customer deleted successfully!")

        elif choice == "5":
            customer_id = int(input("Enter customer ID for new project: "))
            title = input("Enter project title: ")
            description = input("Enter project description (optional): ")
            create_project(title, description, customer_id)
            print("Project added successfully!")

        elif choice == "6":
            customer_id = int(input("Enter customer ID to view projects: "))
            projects = get_projects_by_customer(customer_id)
            for project in projects:
                print(f"{project.id}: {project.title} - {project.description}")

        elif choice == "0":
            print("Exiting the CRM CLI App.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
