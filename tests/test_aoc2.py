import pytest
import aoc2


@pytest.mark.parametrize("test_input,expected", [
    ("5\t1\t9\t5\n7\t5\t3\n2\t4\t5\t6\t8", 18)
])
def test_aoc2_a(test_input, expected):
    assert expected == aoc2.aoc2_a(test_input)


@pytest.mark.parametrize("test_input,expected", [
    ("5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5", 9)
])
def test_aoc2_b(test_input, expected):
    assert expected == aoc2.aoc2_b(test_input)
