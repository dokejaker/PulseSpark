# test_pulsespark.py
"""
Tests for PulseSpark module.
"""

import unittest
from pulsespark import PulseSpark

class TestPulseSpark(unittest.TestCase):
    """Test cases for PulseSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PulseSpark()
        self.assertIsInstance(instance, PulseSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PulseSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
