import summarizer

class TestSummarizer(unittest.TestCase):
    def test_summarizer(self):
        input_str = 'This is a test string.'
        expected_output_str = 'This is a test string.'
        output_str = summarizer.summarize(input_str)
        self.assertEqual(expected_output_str, output_str)

class TestSummarizer(unittest.TestCase):
    def test_summarizer(self):
        pass
