import unittest
from unittest.mock import patch
from calcapi import Calculator

class TestCalculatorWithAPI(unittest.TestCase):
    
    @patch("calculator_with_api.requests.get")
    def test_get_random_number(self, mock_get):
        """Mock the API call and test get_random_number."""
        calc = Calculator()
        
        # Define mock response data
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'number': 42}

        # Test the method with the mocked response
        self.assertEqual(calc.get_random_number(), 42)

if __name__ == "__main__":
    unittest.main()