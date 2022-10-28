# Use for Lesson 7 - unit testing example

import unittest
import unit_test_cap as cap

class TestCap(unittest.TestCase):
	
	def test_one_word(self):
		text = "python"
		result = cap.cap_text(text)

		self.assertEqual(result,"Python")


	def test_multiple_words(self):
		text = "multiple words python"
		result = cap.cap_text(text)

		self.assertEqual(result, "Multiple Words Python")
		# There is an error here because capitalize() only works on the first letter of a string
		# Use title() instead to capitalize first letters on the string

if __name__ == '__main__':
	unittest.main()