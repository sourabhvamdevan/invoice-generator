from datetime import datetime

class Invoice:
    def __init__(self, invoice_number, customer_name, customer_address, issue_date=None, due_date=None):
        self.invoice_number = invoice_number
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.issue_date = issue_date or datetime.now().strftime("%Y-%m-%d")  
        self.due_date = due_date
        self.items = []

    def add_item(self, description, quantity, unit_price):
        self.items.append({"description": description, "quantity": quantity, "unit_price": unit_price})

    def calculate_total(self):
        return sum(item["quantity"] * item["unit_price"] for item in self.items)

    def generate_invoice(self):  
        invoice_str = f"""
        Invoice #{self.invoice_number}

        Bill to:
        {self.customer_name}
        {self.customer_address}

        Issue Date: {self.issue_date}
        Due Date: {self.due_date or "N/A"}

        --------------------------------------------------
        | Description | Quantity | Unit Price | Amount |
        --------------------------------------------------
        """

        for item in self.items:
            amount = item["quantity"] * item["unit_price"]
            invoice_str += f"| {item['description']:<12} | {item['quantity']:>8} | ${item['unit_price']:>10.2f} | ${amount:>6.2f} |\n"

        total = self.calculate_total()
        invoice_str += f"--------------------------------------------------\n"
        invoice_str += f"| Total:                                    ${total:>6.2f} |\n"
        invoice_str += "--------------------------------------------------\n"




        return invoice_str


invoice = Invoice("20231101-001", "Sourabh Vamdevan", "Minal Residency, Bhopal 462023", due_date="2023-11-15")
invoice.add_item("Consulting Services", 20, 168.00)
invoice.add_item("Website Design", 1, 4590.00)
invoice.add_item("Travel Expenses", 500, 25.5) 

print(invoice.generate_invoice())

