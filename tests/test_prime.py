import pytest

from python_project.prime.core import is_prime, next_prime, prev_prime


@pytest.mark.parametrize("n", [2, 3, 5, 7, 13, 97, 7919, 104729])
def test_primes(n):
    assert is_prime(n)


@pytest.mark.parametrize("n", [-7, 0, 1, 4, 9, 25, 91, 7917, 104730])
def test_non_primes(n):
    assert not is_prime(n)


@pytest.mark.parametrize(
    ("n", "expected"), [(-5, 2), (0, 2), (1, 2), (2, 3), (7, 11), (13, 17), (100, 101)]
)
def test_next_prime(n, expected):
    assert next_prime(n) == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [(-5, None), (0, None), (2, None), (3, 2), (13, 11), (100, 97), (104729, 104723)],
)
def test_prev_prime(n, expected):
    assert prev_prime(n) == expected


def test_next_prime_is_strictly_greater():
    for n in range(-3, 60):
        p = next_prime(n)
        assert p > n and is_prime(p)
