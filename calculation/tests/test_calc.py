from utils import division
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 2, 10),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division(a, b, expected_result):
    assert division(a, b) == expected_result

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)