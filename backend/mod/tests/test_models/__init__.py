import unittest

def suite():
    """Discovers all the test cases within the directory and subdirectories
    Returns a unittest.TestSuite containing the tests"""
    return unittest.TestLoader().discover('.', path='test_*.py')