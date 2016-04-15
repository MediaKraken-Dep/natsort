# -*- coding: utf-8 -*-
"""\
This module is intended to replicate some of the functionality
from the fastnumbers module in the event that module is not
installed.
"""
from __future__ import (
    print_function,
    division,
    unicode_literals,
    absolute_import
)

# Std. lib imports.
import sys
import unicodedata
if sys.version[0] != '2':
    long = int


nan_inf = set(['INF', 'INf', 'Inf', 'inF', 'iNF', 'InF', 'inf', 'iNf',
               'NAN', 'nan', 'NaN', 'nAn', 'naN', 'NAn', 'nAN', 'Nan'])
nan_inf.update(['+'+x[:2] for x in nan_inf] + ['-'+x[:2] for x in nan_inf])


def fast_float(x, key=None, nan=None, uni=unicodedata.numeric, nan_inf=nan_inf):
    """\
    Convert a string to a float quickly, return input as-is if not possible.
    We don't need to accept all input that the real fast_int accepts because
    the input will be controlled by the splitting algorithm.
    """
    if x[0] in '0123456789+-.' or x.lstrip()[:3] in nan_inf:
        try:
            x = float(x)
            return nan if nan is not None and x != x else x
        except ValueError:
            if key is not None:
                return uni(x, key(x)) if len(x) == 1 else key(x)
            else:
                return uni(x, x) if len(x) == 1 else x
    else:
        if key is not None:
            return uni(x, key(x)) if len(x) == 1 else key(x)
        else:
            return uni(x, x) if len(x) == 1 else x


def fast_int(x, key=None, nan=None, uni=unicodedata.digit):
    """\
    Convert a string to a int quickly, return input as-is if not possible.
    We don't need to accept all input that the real fast_int accepts because
    the input will be controlled by the splitting algorithm.
    """
    if x[0] in '0123456789+-':
        try:
            return int(x)
        except ValueError:
            if key is not None:
                return uni(x, key(x)) if len(x) == 1 else key(x)
            else:
                return uni(x, x) if len(x) == 1 else x
    else:
        if key is not None:
            return uni(x, key(x)) if len(x) == 1 else key(x)
        else:
            return uni(x, x) if len(x) == 1 else x
