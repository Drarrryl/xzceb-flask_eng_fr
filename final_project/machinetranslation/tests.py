import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()