import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""
    #start the function name with test always
    #and use appropriate names for the fn's so that when getting
    #an error you can easily find where the bug is.
    def test_first_last_name(self):
        """Do names like "monoarul islam" works?"""
        formatted_name = get_formatted_name('monoarul','islam')
        self.assertEqual(formatted_name,'Monoarul Islam')
        
    def test_first_middle_last_name(self):
        "Do names like 'Monoarul Islam Amit' works?"
        formatted_name = get_formatted_name('monoarul','amit','islam')
        self.assertEqual(formatted_name,'Monoarul Islam Amit')
        
unittest.main()
        

#in the output a single . means the program execute one test case