import pytest
from inventory import Inventory

def test_criterion_1_import():
    try:
        from inventory import Inventory
    except ImportError:
        pytest.fail("Inventory class cannot be imported")

def test_criterion_2_add_item():
    inv = Inventory()
    inv.add_item("widget", 100)
    assert inv.get_stock("widget") == 100

def test_criterion_3_get_stock():
    inv = Inventory()
    inv.add_item("widget", 10)
    assert inv.get_stock("widget") == 10

def test_criterion_4_check_low_stock():
    inv = Inventory()
    inv.add_item("widget", 2)
    inv.add_item("thing", 50)
    low = inv.check_low_stock(threshold=10)
    assert "widget" in low
    assert "thing" not in low
