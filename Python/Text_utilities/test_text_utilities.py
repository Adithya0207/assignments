import unittest
from text_utilities import word_count, unique_words, reverse_string


class TestTextUtilities(unittest.TestCase):

    # Test 1: Word Count
    def test_word_count(self):
        self.assertEqual(word_count("Hello World"), 2)

    # Test 2: Unique Words
    def test_unique_words(self):
        result = unique_words("apple apple banana")
        self.assertEqual(sorted(result), ["apple", "banana"])

    # Test 3: String Reversal
    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")

    # Test 4: Empty String
    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)
        self.assertEqual(unique_words(""), [])
        self.assertEqual(reverse_string(""), "")

    # Test 5: Single Word
    def test_single_word(self):
        self.assertEqual(word_count("Python"), 1)
        self.assertEqual(unique_words("Python"), ["python"])

    # Test 6: Case Sensitive
    def test_case_sensitive(self):
        result = unique_words("Hello hello", True)
        self.assertEqual(sorted(result), ["Hello", "hello"])

    # Test 7: Case Insensitive
    def test_case_insensitive(self):
        result = unique_words("Hello hello", False)
        self.assertEqual(result, ["hello"])


if __name__ == "__main__":
    unittest.main()