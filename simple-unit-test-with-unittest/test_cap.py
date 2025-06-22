import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multi_word(self):
        text = 'learning unit test with unittest library!'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Learning Unit Test With Unittest Library!')
        
if __name__ == "__main__":
    unittest.main()