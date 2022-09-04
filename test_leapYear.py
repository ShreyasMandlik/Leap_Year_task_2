import unittest
from unittest import result
import LeapYear


class TestLeapYear(unittest.TestCase):
    
    def test_NegativeYear(self):                 ## Checking the year is negative or not 
        result=LeapYear.LeapYear(-2000)
        stri="Year cannot be negative"
        self.assertEqual(result,stri) 

    def test_divisble_by_four(self):             ## checking the year is divisible by 4
        result=LeapYear.LeapYear(2000)
        self.assertEqual(result,True)

    def test_Not_divisble_by_four(self):         ## checking the year not is divisible by 4
        result=LeapYear.LeapYear(2018)
        self.assertEqual(result,False)

        result1=LeapYear.LeapYear(2019) 
        self.assertEqual(result1,False)

    def test_Divisible_by_4_not_by_100(self):    ## checking the year is divisible by 4 but not by
        result=LeapYear.LeapYear(2016)
        self.assertEqual(result,True)

    def test_Divisible_400(self):                ## checking the year is divisible by 400    
        result=LeapYear.LeapYear(2000)
        self.assertEqual(result,True)

    def test_Divisible_by_100_but_not_400(self): ## checking the year divisible by 100 but not by 400
        result=LeapYear.LeapYear(1900)
        self.assertEqual(result,False)

    



