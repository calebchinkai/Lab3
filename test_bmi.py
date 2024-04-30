import Lab2.bmi as bmi
import pytest

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(height=1.75, weight=70) == 0
    return 0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(height=1.75, weight=85) == 1
    return 1

def test_bmi_under_weight():
    assert bmi.calculate_bmi(height=1.75, weight=50) == -1
    return -1