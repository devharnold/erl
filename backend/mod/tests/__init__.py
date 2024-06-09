import unittest

def suite():
    """Identifies all the tests in the directory and sub-directories
    Returns a unittest.TestSuite object containing the tests
    """
    return unittest.TestLoader().discover('.', pattern='test_*.py')