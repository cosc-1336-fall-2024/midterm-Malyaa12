#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_a.question_a import get_random_number

def test_get_random_number():
    for _ in range(100):
        num = get_random_number()
        assert 1 <= num <= 5, f"Generated number {num} is out of range!"
from src.question_b.question_b import get_assessment_value, get_tax_assessed

def test_get_assessment_value():
    assert get_assessment_value(10000) == 6000
    assert get_assessment_value(20000) == 12000

def test_get_tax_assessed():
    assert get_tax_assessed(6000) == 43.20
    assert get_tax_assessed(10000) == 72

from src.question_c.question_c import get_person_category

def test_get_person_category():
    assert get_person_category(1) == "Infant"
    assert get_person_category(2) == "Child"
    assert get_person_category(14) == "Teenager"
    assert get_person_category(20) == "Adult"
    assert get_person_category(-1) == "Invalid number"
    assert get_person_category(130) == "Invalid number"

from src.question_d.question_d import get_miles_per_hour

def test_get_miles_per_hour():
    assert get_miles_per_hour(32, 60) == 19.883872
    assert get_miles_per_hour(-10, 60) == "Invalid arguments"
    assert get_miles_per_hour(10, 0) == "Invalid arguments"


