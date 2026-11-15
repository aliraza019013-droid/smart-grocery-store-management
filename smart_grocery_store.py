"""Smart Grocery Store Management System.

Products and completed sales are stored in lists of dictionaries while the
program is running. This beginner-friendly version does not use a database.
"""


def get_integer(prompt, minimum=None):
    # Read a whole number and keep asking until it meets the optional minimum.
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_number(prompt, minimum=None):
    # Read a numeric value and validate its optional minimum.
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a value greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def find_product_by_id(products, product_id):
    # Return the product dictionary matching an ID, or None if it is absent.
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def display_product(product):
    # Print every field of one product in a consistent readable layout.
    print("-" * 42)
    print(f"Product ID : {product['id']}")
    print(f"Name       : {product['name']}")
    print(f"Category   : {product['category']}")
    print(f"Price      : Rs. {product['price']:.2f}")
    print(f"Stock      : {product['stock']} units")
    print("-" * 42)


def add_product(products):
    # Collect product details and append a new dictionary if its ID is unique.
    print("\n--- Add New Product ---")
    product_id = get_integer("Enter product ID: ", 1)

    if find_product_by_id(products, product_id) is not None:
        print("A product with this ID already exists. Product not added.")
        return

    name = input("Enter product name: ").strip()
    while not name:
        print("Product name cannot be empty.")
        name = input("Enter product name: ").strip()

    category = input("Enter category: ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    price = get_number("Enter price (Rs.): ", 0)
    stock = get_integer("Enter available stock: ", 0)

    product = {
        "id": product_id,
        "name": name.title(),
        "category": category.title(),
        "price": price,
        "stock": stock
    }
    products.append(product)
    print("Product added successfully.")


def view_products(products):
    # Display all products currently held in the products list.
    print("\n--- All Products ---")
    if not products:
        print("No products are available.")
        return

    for product in products:
        display_product(product)


def search_product(products):
    # Search by numeric product ID or by a case-insensitive product name.
    print("\n--- Search Product ---")
    search_text = input("Enter product name or ID: ").strip()
    if not search_text:
        print("Search value cannot be empty.")
        return

    matches = []
    if search_text.isdigit():
        product = find_product_by_id(products, int(search_text))
        if product is not None:
            matches.append(product)
    else:
        matches = [
            product for product in products
            if search_text.casefold() in product["name"].casefold()
        ]

    if matches:
        for product in matches:
            display_product(product)
    else:
        print("Product not found.")


def update_stock(products):
    # Add units to a product's stock or replace its available quantity.
    print("\n--- Update Product Stock ---")
    product_id = get_integer("Enter product ID: ", 1)
    product = find_product_by_id(products, product_id)

    if product is None:
        print("Product not found.")
        return

    print(f"Current stock for {product['name']}: {product['stock']}")
    print("1. Add stock")
    print("2. Set available stock")
    choice = get_integer("Choose an option: ", 1)

    if choice == 1:
        quantity = get_integer("Enter quantity to add: ", 1)
        product["stock"] += quantity
    elif choice == 2:
        quantity = get_integer("Enter new available quantity: ", 0)
        product["stock"] = quantity
    else:
        print("Invalid stock update option.")
        return

    print(f"Updated stock for {product['name']}: {product['stock']} units")


def process_sale(products, sales_records):
    # Validate a sale, calculate its total, reduce stock, and record the sale.
    print("\n--- Process Customer Sale ---")
    product_id = get_integer("Enter product ID: ", 1)
    product = find_product_by_id(products, product_id)

    if product is None:
        print("Product not found. Sale cancelled.")
        return

    quantity = get_integer("Enter purchase quantity: ", 1)

    if quantity > product["stock"]:
        print(
            f"Insufficient stock. Available stock is {product['stock']} "
            f"unit(s). Sale cancelled."
        )
        return

    total_amount = product["price"] * quantity
    product["stock"] -= quantity

    sale = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity_sold": quantity,
        "total_amount": total_amount
    }
    sales_records.append(sale)

    print("\n--- Purchase Summary ---")
    print(f"Product       : {product['name']}")
    print(f"Quantity      : {quantity}")
    print(f"Unit price    : Rs. {product['price']:.2f}")
    print(f"Total amount  : Rs. {total_amount:.2f}")
    print(f"Remaining stock: {product['stock']}")
    print("Sale completed successfully.")


def view_sales(sales_records):
    # Display every completed transaction stored in the sales list.
    print("\n--- Sales Records ---")
    if not sales_records:
        print("No completed sales yet.")
        return

    for number, sale in enumerate(sales_records, start=1):
        print(
            f"{number}. ID: {sale['product_id']} | "
            f"Product: {sale['product_name']} | "
            f"Quantity: {sale['quantity_sold']} | "
            f"Total: Rs. {sale['total_amount']:.2f}"
        )


def generate_report(products, sales_records):
    # Calculate and display the requested inventory and sales summary.
    print("\n========== STORE REPORT ==========")
    total_products = len(products)
    total_stock = sum(product["stock"] for product in products)
    total_transactions = len(sales_records)
    total_revenue = sum(sale["total_amount"] for sale in sales_records)

    print(f"Total number of products : {total_products}")
    print(f"Total available stock    : {total_stock} units")
    print(f"Total sales transactions : {total_transactions}")
    print(f"Total revenue generated  : Rs. {total_revenue:.2f}")

    low_stock_products = [product for product in products if product["stock"] < 5]
    print("\nProducts with stock below 5 units:")
    if low_stock_products:
        for product in low_stock_products:
            print(f"- {product['name']} (ID: {product['id']}): {product['stock']} units")
    else:
        print("- None")

    if products:
        highest_price = max(product["price"] for product in products)
        lowest_price = min(product["price"] for product in products)

        print("\nProduct(s) with the highest price:")
        for product in products:
            if product["price"] == highest_price:
                print(f"- {product['name']} (Rs. {product['price']:.2f})")

        print("Product(s) with the lowest price:")
        for product in products:
            if product["price"] == lowest_price:
                print(f"- {product['name']} (Rs. {product['price']:.2f})")
    else:
        print("\nNo product price information is available.")

    print("=" * 36)


def show_menu():
    # Display the main application menu.
    print("\n====================================")
    print("       SMART GROCERY STORE SYSTEM")
    print("====================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")


def main():
    # Run the menu until the user chooses to exit.
    products = [
        {"id": 101, "name": "Milk", "category": "Dairy", "price": 250.0, "stock": 20},
        {"id": 102, "name": "Bread", "category": "Bakery", "price": 120.0, "stock": 15},
        {"id": 103, "name": "Rice", "category": "Grains", "price": 300.0, "stock": 4}
    ]
    sales_records = []

    while True:
        show_menu()
        choice = get_integer("Enter your choice: ", 1)

        if choice == 1:
            add_product(products)
        elif choice == 2:
            view_products(products)
        elif choice == 3:
            search_product(products)
        elif choice == 4:
            update_stock(products)
        elif choice == 5:
            process_sale(products, sales_records)
        elif choice == 6:
            view_sales(sales_records)
        elif choice == 7:
            generate_report(products, sales_records)
        elif choice == 8:
            print("Thank you for using Smart Grocery Store System.")
            break
        else:
            print("Invalid menu choice. Please select 1 to 8.")


if __name__ == "__main__":
    main()
