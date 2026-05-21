import pytest
from inventory import Inventory, add_item, get_item, get_total_value, get_low_stock_items


def test_criterion_1_module_import():
    import inventory
    assert inventory is not None


def test_criterion_2_add_item():
    inv = Inventory()
    add_item(inv, '1', 'Apple', 10, 1.5)
    assert inv.get_item('1') == {'name': 'Apple', 'quantity': 10, 'price': 1.5}


def test_criterion_3_get_total_value():
    inv = Inventory()
    add_item(inv, '1', 'Apple', 10, 1.5)
    add_item(inv, '2', 'Banana', 5, 0.5)
    assert get_total_value(inv) == 17.5


def test_criterion_4_get_low_stock_items():
    inv = Inventory()
    add_item(inv, '1', 'Apple', 2, 1.0)
    add_item(inv, '2', 'Banana', 10, 0.5)
    low = get_low_stock_items(inv, threshold=5)
    assert len(low) == 1
    assert low[0]['quantity'] == 2
