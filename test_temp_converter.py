import unittest
from temp_converter import convert_celcius_to_fareinheit

class TempConverterTest(unittest.TestCase):
    #given temp in celcius = correct value in F
    #data type for input
    #if it throws an exception when data type is incorrect
    #check for null values -> throw an error
    def test_Celcius_to_Fareinheight(self):
       #F = c * 9/5 + 32
       actual = convert_celcius_to_fareinheit(10)
       expected = 50
       self.assertEqual(actual,expected,"celcius should convert to correct Farenheit")

if __name__ == "__main__":
    unittest.main()