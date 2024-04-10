#!/usr/bin/python3
""" a function that multiplies 2 matrices by using the module NumPy"""
import numpy as np
""" the numerical python module called numpy that counts numbers faster"""


def lazy_matrix_mul(m_a, m_b):
    """ a function that multiplies 2 matrices"""
    return np.matmul(m_a, m_b)
