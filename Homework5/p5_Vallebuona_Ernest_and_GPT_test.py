# p5_Vallebuona_Ernest_and_GPT_test.py

import unittest
from p5_Vallebuona_Ernest_and_GPT import (
    caesar_cipher,
    caesar_decipher,
    letter_frequency
)


class TestCaesarCipher(unittest.TestCase):

    def test_cipher(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")
        self.assertEqual(caesar_cipher("Hello World!", 3), "Khoor Zruog!")

    def test_cipher_wrap(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc")
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")

    def test_decipher(self):
        self.assertEqual(caesar_decipher("def", 3), "abc")
        self.assertEqual(
            caesar_decipher("Khoor Zruog!", 3),
            "Hello World!"
        )

    def test_frequency(self):
        result = letter_frequency("Hello World!")

        self.assertEqual(result["h"], 1)
        self.assertEqual(result["e"], 1)
        self.assertEqual(result["l"], 3)
        self.assertEqual(result["o"], 2)
        self.assertEqual(result["w"], 1)
        self.assertEqual(result["r"], 1)
        self.assertEqual(result["d"], 1)

    def test_frequency_ignores_non_letters(self):
        result = letter_frequency("A! A? 123")

        self.assertEqual(result["a"], 2)
        self.assertEqual(result["b"], 0)


if __name__ == "__main__":
    unittest.main()