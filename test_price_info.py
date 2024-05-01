import pytest
from price_info import total_cost_shopping, cost_of_fruits

def test_total_cost_shopping():
    expected_total_cost = 46.75
    assert total_cost_shopping() == expected_total_cost

def test_cost_of_fruits():
    expected_cost_apple = 12.0
    assert cost_of_fruits('apple', 10) == expected_cost_apple