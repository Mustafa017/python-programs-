def remove_duplicates(string):
  unique = set(string.strip())
  dropped = len(string) - len(unique)
  return unique,dropped #''.join(sorted(unique)),dropped
print(remove_duplicates("aaabbbac"))

import unittest;

class Test(unittest.TestCase):
    def test_output_is_correct(self):
        result1 = remove_duplicates('aaabbbac')
        result2 = remove_duplicates('a')
        result3 = remove_duplicates('thelexash')

        self.assertIsInstance(result1, tuple, msg='Incorrect output type')
        self.assertEqual(result1, ('abc', 5), msg='Incorrect output')

        self.assertIsInstance(result2, tuple, msg='Incorrect output type')
        self.assertEqual(result2, ('a', 0), msg='Incorrect output')

        self.assertIsInstance(result3, tuple, msg='Incorrect output type')
        self.assertEqual(result3, ('aehlstx', 2), msg='Incorrect output')

    def test_output_is_correct_hidden(self):
        result1 = remove_duplicates('thisisateststring')
        result2 = remove_duplicates('letsseehowthisgoes')
        result3 = remove_duplicates('hiddenhiddenhiddenhaha')

        self.assertIsInstance(result1, tuple, msg='Incorrect output type')
        self.assertEqual(result1, ('aeghinrst', 8), msg='Incorrect output')

        self.assertIsInstance(result2, tuple, msg='Incorrect output type')
        self.assertEqual(result2, ('eghilostw', 9), msg='Incorrect output')

        self.assertIsInstance(result3, tuple, msg='Incorrect output type')
        self.assertEqual(result3, ('adehin', 16), msg='Incorrect output')
