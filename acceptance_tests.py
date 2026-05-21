import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_criterion_1_module_import():
    try:
        import inventory
        assert True
    except ImportError:
        assert False

def test_criterion_2_add_item():
    try:
        import inventory
        inventory.add_item("item1", 10)
        assert True
    except AttributeError:
        assert False

def test_criterion_3_get_stock():
    try:
        import inventory
        qty = inventory.get_stock("item1")
        assert qty == 10
    except AttributeError:
        assert False

def test_criterion_4_check_low_stock():
    try:
        import inventory
        result = inventory.check_low_stock(threshold=5)
        assert isinstance(result, list)
    except AttributeError:
        assert False
