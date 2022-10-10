"""EX07 Dictionary Utils Test."""

__author__: str = "730575704"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Invert empty case."""
    assert invert({}) == {}


def test_invert_one_keypair() -> None:
    """Invert 1 key pair case."""
    assert invert({"Civilization": "VI"}) == {"VI": "Civilization"}


def test_invert_three_keypairs() -> None:
    """Invert 3 key pairs case."""
    assert invert({"cats": "rain", "dogs": "hail", "poisonous frogs": "weather report"}) == {"rain": "cats", "hail": "dogs", "weather report": "poisonous frogs"}


def test_favorite_color_empty() -> None:
    """Empty dict test case."""
    assert favorite_color({}) == ""


def test_favorite_color_one_max() -> None:
    """Only one highest color."""
    assert favorite_color({"Bob": "Blue", "Builder": "Red", "John": "Blue", "Williams": "Green"}) == "Blue"


def test_favorite_color_tie() -> None:
    """A tie of highest colors."""
    assert favorite_color({"Bob": "Red", "Builder": "Blue", "John": "Blue", "Williams": "Red"}) == "Red"


def test_count_empty() -> None:
    """Count empty list."""
    assert count([]) == {}


def test_count_unique() -> None:
    """Count of no repeats."""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_many() -> None:
    """Count of some repeats."""
    assert count(["A", "B", "A", "C", "B", "A", "D", "C", "E"]) == {"A": 3, "B": 2, "C": 2, "D": 1, "E": 1}
