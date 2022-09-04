import unittest
from unittest import result
import LeapYear


class TestLeapYear(unittest.TestCase):
    
    def test_NegativeYear(self):  ## Checking the year is negative or not 
        result=LeapYear.LeapYear(-2000)
        stri="Year cannot be negative"
        self.assertEqual(result,stri) 

    def test_divisblebyfour(self): ## checking the year is divisible by 4
        result=LeapYear.LeapYear(2000)
        self.assertEqual(result,True)


