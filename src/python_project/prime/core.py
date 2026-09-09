"""Primality helpers, kept free of any UI code so they stay testable."""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Every prime above 3 is of the form 6k +/- 1, so step through those only.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def next_prime(n: int) -> int:
    candidate = max(n + 1, 2)
    while not is_prime(candidate):
        candidate += 1
    return candidate


def prev_prime(n: int) -> int | None:
    """Largest prime below n, or None when there is none (n <= 2)."""
    candidate = n - 1
    while candidate >= 2:
        if is_prime(candidate):
            return candidate
        candidate -= 1
    return None
