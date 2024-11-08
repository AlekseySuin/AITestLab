import unittest
from main import emotions
class emotionsTester(unittest.TestCase):
    def setUp(self):
        self.emotions = emotions()

    def test_positive(self):
        string1 = "Я очень доволен! И РАД!"
        return_data = [{'label': 'POSITIVE', 'score': 0.9800326228141785}]
        self.assertEqual(emotions.takeEmotion(string1), 'POSITIVE')


    def test_negative(self):
        string2 = "Я ТЕБЯ НЕНАВИЖУ!"
        self.assertEqual(emotions.takeEmotion(string2), 'NEGATIVE')

    def test_netrual(self):
        string3 = "Книга была написана в 1999 году"
        self.assertEqual(emotions.takeEmotion(string3), 'NEUTRAL')

if __name__ == "__main__":
  unittest.main()
