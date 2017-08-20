import unittest

from src.main.domain.encoder import Encoder


class TestEncoder(unittest.TestCase):
    def test_should_return_input_encoder_Value(self):
        expected_encoder_value = 300
        current_encoder_value = 300

        encoder = Encoder(current_encoder_value)

        self.assertEquals(expected_encoder_value, encoder._value)


if __name__ == '__main__':
    unittest.main()
