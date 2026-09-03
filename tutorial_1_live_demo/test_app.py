import unittest

from app import convert_hkd_to_usd


class ConvertHKDToUSDTests(unittest.TestCase):
    def test_converts_100_hkd(self):
        self.assertEqual(convert_hkd_to_usd(100), 12.82)

    def test_zero_hkd_stays_zero(self):
        self.assertEqual(convert_hkd_to_usd(0), 0.0)

    def test_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            convert_hkd_to_usd(-1)


if __name__ == "__main__":
    unittest.main()
