from fuzzy_compare import compare_english_words
import unittest


class TestCompareStrings(unittest.TestCase):

    def test_full_range(self):
        self.assertTrue(compare_english_words(
        "abcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqrstuvwxyz") == 1)
    
    def test_case_insensitivity(self):
        self.assertEqual(compare_english_words(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "abcdefghijklmnopqrstuvwxyz"), 1)
    
    def test_decreasing_similarity(self):
        self.assertTrue(1 >= compare_english_words("hello", "hello") 
            > compare_english_words("hello", "hell") 
            > compare_english_words("hello", "hel") 
            > compare_english_words("hello", "he") 
            > compare_english_words("hello", "h")
            > 0)


if __name__ == "__main__":
    unittest.main()