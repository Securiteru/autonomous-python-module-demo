"""Tests for demo_app.math_ops."""

from demo_app.math_ops import multiply


def test_multiply_positives() -> None:
    assert multiply(3, 4) == 12
    assert multiply(1, 100) == 100


def test_multiply_zero() -> None:
    assert multiply(0, 5) == 0
    assert multiply(7, 0) == 0
    assert multiply(0, 0) == 0


def test_multiply_negatives() -> None:
    assert multiply(-2, 3) == -6
    assert multiply(4, -5) == -20
    assert multiply(-3, -3) == 9
