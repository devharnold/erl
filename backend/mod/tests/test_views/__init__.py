import unittest

def suite():
    """
    Discovers all the test cases within
    the directories and sub-directories
    Return unittest.TestSuite objects containing the discovered tests
    """
    return unittest.TestCase().discover('.', pattern="test*.py")