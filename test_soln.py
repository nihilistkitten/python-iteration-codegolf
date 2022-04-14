from copy import deepcopy
from math import factorial

from hypothesis import assume, given
from hypothesis import strategies as st

from soln import (
    char_count,
    counts,
    down_up,
    filter,
    has_duplicates,
    inverse,
    make_even,
    primes_list,
)

MAX = 100  # primes quickly hits recursion depth issues higher than this


def down_up_soln(n):
    """Compute `down_up(n)`."""
    if n < 1:
        return []
    if n == 1:
        return [1]
    return [n] + down_up(n - 1) + [n]


@given(st.integers(min_value=0, max_value=MAX))
def test_down_up(n):
    """Test `down_up`."""
    assert down_up_soln(n) == down_up(n)


def filter_soln(pred, xs):
    """Compute `filter(pred, xs)`."""
    return [x for x in xs if pred(x)]


@given(
    st.functions(like=lambda x: x < 1.0),
    st.lists(st.floats(max_value=MAX), max_size=MAX),
)
def test_filter(pred, xs):
    """Test `filter`.

    Only tested on floats currently.
    """
    assert filter_soln(pred, xs) == filter(pred, xs)


def make_even_soln(xs):
    """Compute `make_even(xs)`."""
    xs[:] = [x - x % 2 for x in xs]


@given(st.lists(st.integers(max_value=MAX), max_size=MAX))
def test_make_even(xs):
    """Test `make_even`."""
    ys = deepcopy(xs)
    make_even_soln(xs)
    make_even(ys)
    assert xs == ys


def char_count_soln(s):
    """Compute `char_count(s)`."""
    return {c: s.count(c) for c in s}


@given(st.text(max_size=MAX))
def test_char_count(s):
    """Test `char_count`."""
    assert char_count_soln(s) == char_count(s)


def counts_soln(n, xs):
    """Compute `counts(n, xs)`."""
    ret = [0] * n
    for i in xs:
        if 0 <= i < n:
            ret[i] += 1

    return ret


@given(
    st.integers(min_value=0, max_value=MAX),
    st.lists(st.integers(max_value=MAX), max_size=MAX),
)
def test_counts(n, xs):
    """Test `char_count`."""
    assert counts_soln(n, xs) == counts(n, xs)


def primes_list_soln(n):
    """Compute `primes_list(n)`."""
    ret = []
    i = 2
    while len(ret) < n:
        if factorial(i - 1) % i == i - 1:
            ret.append(i)
        i += 1

    return ret


@given(st.integers(min_value=0, max_value=MAX))
def test_primes_list(n):
    """Test `primes_list`."""
    assert primes_list_soln(n) == primes_list(n)


def has_duplicates_soln(xs):
    """Compute `has_duplicates(xs)`."""
    return len(set(xs)) != len(xs)


@given(st.lists(st.one_of(st.integers(max_value=MAX), st.text(max_size=MAX))))
def test_has_duplicates(xs):
    """Test `has_duplicates`.

    Only tested on lists of integers and strings.
    """
    assert has_duplicates_soln(xs) == has_duplicates(xs)


def inverse_soln(d):
    """Compute `inverse(d)`."""
    ret = {}
    for k in d:
        if d[k] not in ret:
            ret[d[k]] = []
        ret[d[k]].append(k)

    return ret


@given(
    st.dictionaries(
        st.one_of(st.integers(max_value=MAX), st.text(max_size=MAX)),
        st.one_of(st.integers(max_value=MAX), st.text(max_size=MAX)),
    )
)
def test_inverse(xs):
    """Test `inverse`.

    Only tested on dictionaries of integers and strings.
    """
    assert inverse_soln(xs) == inverse(xs)
