



# Invoice Generator

A Python-based tool for generating professional, itemized invoices. This project provides a flexible way to create invoices for services and products with customer details, due dates, and calculated totals.



## Features

- **Dynamic Invoice Generation**: Automatically generate invoices with invoice numbers, customer information, and due dates.
- **Customizable Items**: Add multiple items or services with descriptions, quantities, and unit prices.
- **Automatic Totals**: Calculate the total amount based on the items added.
- **Professional Formatting**: Produces a clear and structured invoice layout ready for printing or saving.



## How It Works

1. **Initialize Invoice**: Create an invoice by providing:
   - Invoice number
   - Customer name and address
   - Optional issue date (defaults to today) and due date.
2. **Add Items**: Use the `add_item` method to add descriptions, quantities, and prices for each item or service.
3. **Generate Invoice**: Call the `generate_invoice` method to produce the invoice in a formatted output.



## Sample Output

```
        Invoice #20231101-001

        Bill to:
        Sourabh Vamdevan
        Minal Residency, Bhopal 462023

        Issue Date: 2023-11-01
        Due Date: 2023-11-15

        --------------------------------------------------
        | Description     | Quantity | Unit Price | Amount |
        --------------------------------------------------
        | Consulting Services |       20 | $   168.00 | $3360.00 |
        | Website Design      |        1 | $  4590.00 | $4590.00 |
        | Travel Expenses     |      500 | $    25.50 | $12750.00 |
        --------------------------------------------------
        | Total:                                      $20670.00 |
        --------------------------------------------------
```





## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/invoice generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd invoice generator
   ```
3. Run the script:
   ```bash
   python invoice generator.py
   ```
4. Customize the invoice details in the script, including:
   - Customer information
   - Items and services using the `add_item` method.
5. (Optional) Save the invoice to a file:
   Uncomment the code snippet in the script to save the generated invoice as a `.txt` file.

---

## Example Usage

```python
invoice = Invoice("20231101-001", "Sourabh Vamdevan", "Minal Residency, Bhopal 462023", due_date="2023-11-15")
invoice.add_item("Consulting Services", 20, 168.00)
invoice.add_item("Website Design", 1, 4590.00)
invoice.add_item("Travel Expenses", 500, 25.5)
print(invoice.generate_invoice())
```

---



## License

This project is licensed under the [MIT License](LICENSE).



