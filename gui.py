import tkinter as tk
from tkinter import ttk, messagebox
from database import DBManager
from invoice_generator import generate_invoice_pdf

class BillingApp:
    def __init__(self, root):
        self.db = DBManager()
        self.root = root
        self.root.title("Billing Software")
        self.root.geometry("800x600")

        self.setup_ui()

    def setup_ui(self):
        # Customer Info
        ttk.Label(self.root, text="Customer Name").grid(row=0, column=0)
        self.customer_name = ttk.Entry(self.root)
        self.customer_name.grid(row=0, column=1)

        # Product Info
        ttk.Label(self.root, text="Product").grid(row=1, column=0)
        self.product_name = ttk.Entry(self.root)
        self.product_name.grid(row=1, column=1)

        ttk.Label(self.root, text="Price").grid(row=2, column=0)
        self.price = ttk.Entry(self.root)
        self.price.grid(row=2, column=1)

        ttk.Label(self.root, text="Quantity").grid(row=3, column=0)
        self.quantity = ttk.Entry(self.root)
        self.quantity.grid(row=3, column=1)

        # Buttons
        ttk.Button(self.root, text="Add Transaction", command=self.add_transaction).grid(row=4, column=0)
        ttk.Button(self.root, text="Generate Invoice", command=self.generate_invoice).grid(row=4, column=1)

    def add_transaction(self):
        # Save to DB
        self.db.add_transaction(
            self.customer_name.get(),
            self.product_name.get(),
            float(self.price.get()),
            int(self.quantity.get())
        )
        messagebox.showinfo("Success", "Transaction added!")

    def generate_invoice(self):
        data = self.db.get_latest_transaction()
        generate_invoice_pdf(data)
        messagebox.showinfo("Invoice", "Invoice generated!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
