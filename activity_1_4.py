# -*- coding: utf-8 -*-
"""Activity 1.4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z-k-TrhSSwyVCDF5itynMwm_P5L3bzhd
"""

triangle_area = lambda b, h: 1/2 * b * h

def triangle_area (b,h):
    """compute the area of a right triangle using its base and height"""
    output =1/2 * b * h
    return output

def test_triangle_area():
    assert triangle_area(10,4) == 20
    assert triangle_area(6,4) == 12
    assert triangle_area(5,6) == 15
test_triangle_area()

def triangle_area (b,h):
    """compute the area of a right triangle using its base and height"""
    output =1/2 * b * h
    return output
def test_triangle_area():
    assert triangle_area(10,4) == 20
    assert triangle_area(6,4) == 12
    assert triangle_area(5,6) == 15
test_triangle_area()

help(triangle_area)