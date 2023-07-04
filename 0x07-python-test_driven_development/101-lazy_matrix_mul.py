#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as succy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b using
    matmul, and returns the result.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (succy.matmul(m_a, m_b))
