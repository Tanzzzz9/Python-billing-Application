from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas



def generate_invoice_pdf(customer, product, quantity, total):
    c = canvas.Canvas("invoice.pdf")
    c.drawString(100, 800, f"Customer: {customer}")
    c.drawString(100, 780, f"Product: {product}")
    c.drawString(100, 760, f"Quantity: {quantity}")
    c.drawString(100, 740, f"Total: ${total}")
    c.save()
