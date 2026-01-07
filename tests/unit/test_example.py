"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from pyospackage_rnliang.example import normal_pdf_value

def test_add_numbers():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = normal_pdf_value(0, 1, 1)
    expected_out = 0.2419707245
    assert abs(out - expected_out) < 1e-5, f"Expected {expected_out} but got {out}"
