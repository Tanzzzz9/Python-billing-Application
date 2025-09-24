import tkinter as tk
from tkinter import ttk, messagebox
from database import DBManager
from invoice_generator import generate_invoice_pdf

db = DBManager()

def add_customer():
    name = customer_name.get()
    contact = customer_contact.get()
    db.add_customer(name, contact)
    messagebox.showinfo("Success", "Customer added!")

def add_product():
    name = product_name.get()
    price = float(product_price.get())
    db.add_product(name, price)
    messagebox.showinfo("Success", "Product added!")

def generate_invoice():
    customer = customer_select.get()
    product = product_select.get()
    quantity = int(product_quantity.get())

    customer_id = int(customer.split(":")[0])
    product_id = int(product.split(":")[0])
    price = float(product.split("$")[1])
    total = price * quantity

    db.add_transaction(customer_id, product_id, quantity, total)
    generate_invoice_pdf(customer, product, quantity, total)
    messagebox.showinfo("Invoice", "Invoice generated!")

root = tk.Tk()
root.title("Billing Software")
root.geometry("600x400")

# Customer Entry
ttk.Label(root, text="Customer Name").grid(row=0, column=0)
customer_name = ttk.Entry(root)
customer_name.grid(row=0, column=1)

ttk.Label(root, text="Contact").grid(row=1, column=0)
customer_contact = ttk.Entry(root)
customer_contact.grid(row=1, column=1)

ttk.Button(root, text="Add Customer", command=add_customer).grid(row=2, column=1)

# Product Entry
ttk.Label(root, text="Product Name").grid(row=3, column=0)
product_name = ttk.Entry(root)
product_name.grid(row=3, column=1)

ttk.Label(root, text="Price").grid(row=4, column=0)
product_price = ttk.Entry(root)
product_price.grid(row=4, column=1)

ttk.Button(root, text="Add Product", command=add_product).grid(row=5, column=1)

# Transaction
ttk.Label(root, text="Select Customer").grid(row=6, column=0)
customer_select = ttk.Combobox(root, values=[f"{c[0]}: {c[1]}" for c in db.get_customers()])
customer_select.grid(row=6, column=1)

ttk.Label(root, text="Select Product").grid(row=7, column=0)
product_select = ttk.Combobox(root, values=[f"{p[0]}: {p[1]} ${p[2]}" for p in db.get_products()])
product_select.grid(row=7, column=1)

ttk.Label(root, text="Quantity").grid(row=8, column=0)
product_quantity = ttk.Entry(root)
product_quantity.grid(row=8, column=1)

ttk.Button(root, text="Generate Invoice", command=generate_invoice).grid(row=9, column=1)

root.mainloop()
