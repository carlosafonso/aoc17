import pytest
import aoc1_a
import aoc1_b


@pytest.mark.parametrize("test_input,expected", [
    ("1122", 3),
    ("1111", 4),
    ("1234", 0),
    ("91212129", 9)
])
def test_aoc1_a(test_input, expected):
    assert expected == aoc1_a.aoc1_a(test_input)


@pytest.mark.parametrize("test_input,expected", [
    ("1212", 6),
    ("1221", 0),
    ("123425", 4),
    ("123123", 12),
    ("12131415", 4)
])
def test_aoc1_b(test_input, expected):
    assert expected == aoc1_b.aoc1_b(test_input)
