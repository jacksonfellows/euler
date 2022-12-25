from functools import lru_cache

@lru_cache(None)
def num_ascending(first_digit, n_digits_remaining):
    if n_digits_remaining == 0:
        return 1
    return sum(num_ascending(d, n_digits_remaining-1) for d in range(first_digit, 10))

@lru_cache(None)
def num_descending(first_digit, n_digits_remaining):
    if n_digits_remaining == 0:
        return 1
    return sum(num_descending(d, n_digits_remaining-1) for d in range(first_digit, -1, -1))

def num_ascending_descending_under(max_n_digits):
    return sum(sum(num_ascending(d, n_digits) + num_descending(d, n_digits) for d in range(1,10)) for n_digits in range(max_n_digits)) - 9*max_n_digits
