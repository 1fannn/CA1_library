from src.library_eligibility import can_borrow
import pytest


@pytest.mark.parametrize(
    "active_loans, overdue_books, expected",
    [
        (0, 0, True),
        (3, 0, True),
        (5, 0, True),
        (6, 0, False),
        (4, 1, False),
        (6, 2, False),
    ],
)
def test_can_borrow(active_loans, overdue_books, expected):
    assert can_borrow(active_loans, overdue_books) is expected


@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
    ],
)
def test_value_error(active_loans, overdue_books):
    with pytest.raises(ValueError, match="argument outside permitted range"):
        can_borrow(active_loans, overdue_books)


@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        ("3", 0),
        (3, "0"),
        (3.0, 0),
        (3, 0.0),
        (True, 0),
        (3, False),
        ],
)
def test_type_error(active_loans, overdue_books):
    with pytest.raises(TypeError, match="invalid argument type"):
        can_borrow(active_loans, overdue_books)