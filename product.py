import sys

def get_product_info(product_id, name, quantity, price):
    return (
        f"Product ID:{product_id}\n"
        f"Product Name:{name}\n"
        f"Quantity:{quantity}\n"
        f"Price:{price}"
    )

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("product details\n")
        product_id = "P001"
        name = "Laptop"
        quantity = "5"
        price = "1200.50"
    else:
        product_id = sys.argv[1]
        name = sys.argv[2]
        quantity = sys.argv[3]
        price = sys.argv[4]
        
print(get_product_info(product_id, name, quantity, price))




    




