import pytest
from product import get_product_info

def test_default_values():
    expected = (
        "Product ID:P001\n"
        "Product Name:Laptop\n"
        "Quantity:5\n"
        "Price:1200.50"
    )
    assert get_product_info("P001", "Laptop", "5", "1200.50") == expected

      




