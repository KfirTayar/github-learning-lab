import unittest

from forecast import forecast_population


class ForecastTests(unittest.TestCase):
    def test_partial_realization(self):
        self.assertEqual(forecast_population(1000, 200, 0.5), 1100)

    def test_invalid_realization(self):
        with self.assertRaises(ValueError):
            forecast_population(1000, 200, 1.2)
