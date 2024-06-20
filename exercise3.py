#creating a list of a product names and price
products =[("banana",2.24),("apple",2.60),("orange",3.40)]

#displaying the product in a table format
print("product catalog:")
print(f"{'product':<20}{'price':>12}")
for product, price in products:
    print(f"{product:<20} shs {price:>10.5f}")

