# pip install pytest
# python3 -m pytest

import pytest
from delivery import get_cost


@pytest.mark.parametrize(
    'a,expected',
    (
        (9, '200'),
        (12, '500'),
    )
)
def test_get_coast_with_params(a, expected):
    assert expected in get_cost(a)