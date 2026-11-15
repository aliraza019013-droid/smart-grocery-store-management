# Smart Grocery Store Management System

## Overview
A beginner-friendly, menu-driven Python application for managing grocery products, inventory, customer sales, and a store summary report.

## Files
- `smart_grocery_store.py` — complete application.
- `README.md` — project description and instructions.

## Features
1. Add products using dictionaries stored in a list. Duplicate product IDs are rejected.
2. View all product details.
3. Search by product ID or part/all of a product name.
4. Add stock or set a new stock quantity.
5. Process sales only when the product exists and enough stock is available.
6. Keep completed sales in a separate list of dictionaries.
7. Generate a report with product count, total stock, sales transactions, revenue, low-stock items, and highest/lowest-priced products.

The program starts with three sample products (Milk, Bread, and Rice). You can change or remove these sample records in `main()`.

## Python concepts used
- Lists of dictionaries for products and sales records.
- Dictionary keys and values to access product and transaction information.
- `.append()` to add products and completed sales.
- Custom functions to keep each operation organized.
- `for` and `while` loops to process records and keep the menu running.
- `if` / `elif` / `else` conditions for menu choices and validation.
- `try` / `except ValueError` for invalid numeric input.
- `len()`, `sum()`, `max()`, and `min()` for the store report.
- List comprehensions to identify products with low stock.

## Requirements
- Python 3.8 or newer
- No external libraries

## How to run
1. Extract the ZIP file.
2. Open a terminal or command prompt in the extracted project folder.
3. Run:

```bash
python smart_grocery_store.py
```

If your system uses `python3`, run:

```bash
python3 smart_grocery_store.py
```

## Sample interaction

```text
SMART GROCERY STORE SYSTEM
1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice: 5
Enter product ID: 101
Enter purchase quantity: 2

Purchase Summary
Product        : Milk
Quantity       : 2
Unit price     : Rs. 250.00
Total amount   : Rs. 500.00
Remaining stock: 18
Sale completed successfully.
```

## Important note
This assignment version keeps data in memory while the program is running. Products and sales records return to their sample starting state when the program is restarted. File/database saving can be added as a future improvement.
