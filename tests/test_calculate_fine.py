from src.library_fine import calculate_fine 
import pytest

@pytest.mark.parametrize(
    "overdue_days, fine",
    [
        (0, 0),
        (1, 50),
        (5, 250),
        (10, 500),
        (11, 550),
    ],
)
def test_calculate_fine(overdue_days, fine):
    assert calculate_fine(overdue_days) == fine

def test_negative_days():
    with pytest.raises(ValueError):
        calculate_fine(-1)

@pytest.mark.parametrize(
    "overdue_days",
    ["5", 5.0, True],
)
def test_calculate_fine_type_error(overdue_days):
    with pytest.raises(TypeError):
        calculate_fine(overdue_days)

