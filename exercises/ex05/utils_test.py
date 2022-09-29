"""EX 5 Test Utils."""

__author__: str = "730575704"

from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Edge case of empty list."""
    assert only_evens([]) == []


def test_only_evens_one_even() -> None:
    """Case with only one even."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_no_evens() -> None:
    """Long list with no evens case."""
    assert only_evens([21, 35, 43, 3, 5, 7]) == []


def test_concat_empty() -> None:
    """Edge case with empty lists."""
    assert concat([], []) == []


def test_concat_equal_lists() -> None:
    """Concatenating lists of equal length."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_concat_unequal_lists() -> None:
    """Concatenating lists of unequal lengths."""
    assert concat([1, 2], [3, 4, 5]) == [1, 2, 3, 4, 5]


def test_sub_empty() -> None:
    """Edge case with empty list and 0 range values."""
    assert sub([], 0, 0) == []


def test_sub_range_two() -> None:
    """Case with a range of 2 in a list of 3."""
    assert sub([1, 2, 3], 1, 3) == [2, 3]


def test_sub_range_5_start_3() -> None:
    """Case with a range of 5 in a list of 10 starting at index 3."""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 8) == [4, 5, 6, 7, 8]